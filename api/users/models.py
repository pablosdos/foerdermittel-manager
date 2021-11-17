from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError("Der Benutzer muss ein Email eingeben")
        user = self.model(email=self.normalize_email(email), first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, password=None):
        user = self.create_user(email=email, first_name=first_name, password=password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    This will be the user model used by the application
    It has all the information regarding The User, inclusive the profile which the user has

    On the application we will have 3 main profiles: 
        - Admin
        - Anbieter
        - Suchender
    """

    profile_choices = models.IntegerChoices('Profile', 'ADMIN ANBIETER SUCHENDER')


    # Personal Information
    first_name = models.CharField(max_length=64, verbose_name='Vorname')
    last_name = models.CharField(max_length=128, verbose_name='Name', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Geburtsdatum', null=True)


    # Account Information
    email = models.EmailField(verbose_name='Email', unique=True)
    password = models.CharField(max_length=256, verbose_name='Password')
    profile = models.IntegerField(choices=profile_choices.choices, verbose_name='Profil', null=True)
    agreed_on_terms = models.BooleanField(default=False, verbose_name='Datenschutzgenehmigung?')
    is_active = models.BooleanField(default=False, verbose_name='Ist User aktiv?')
    is_superuser = models.BooleanField(default=False, verbose_name='Ist SuperUser?')
    is_staff=models.BooleanField(default=False, verbose_name='Ist Staff?')


    # Activity Information
    last_login = models.DateTimeField(null=True, verbose_name="Letztes Login")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Letztes Updated')

    # Responsibility Information
    groups = models.ManyToManyField(
        blank=True,
        help_text="Grupo ao qual o usuário pertence. O usuário recebe todas as permissões dos grupos ao qual ele pertence.",
        related_name="user_groups",
        related_query_name="user",
        to="auth.Group",
        verbose_name="Grupos de usuário",
    )

    user_permissions = models.ManyToManyField(
        blank=True,
        help_text="Permissões específicas do usuário.",
        related_name="user_permissions",
        related_query_name="user",
        to="auth.Permission",
        verbose_name="Permissões do usuário",
    )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name']


    objects = UserManager()
    class Meta:
        verbose_name = 'Benutzer'
        verbose_name_plural = 'Benutzern'

    def get_full_name(self):
        return f"{self.last_name}, {self.first_name}"

    def __str__(self):
        return f"{self.first_name} - {self.first_name.capitalize()}"
