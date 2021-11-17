from django.db import models


class ContactMessage(models.Model):
    
    first_name = models.CharField(max_length=64, verbose_name='Vorname')
    last_name = models.CharField(max_length=128, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Nachricht')
    
    is_read = models.BooleanField(default= False, verbose_name='Ist die Nachricht schon gelesen?')
    is_answered = models.BooleanField(default= False, verbose_name='Ist die Nachricht schon geantworter?')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Zeit der Empfängen')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Zeit der Update')
    

    def __str__(self):
        return f'{self.last_name} - {self.email} - {self.created_at}'
    
    class Meta:
        verbose_name='Kontakt Nachricht'
        verbose_name_plural='Kontakt Nachrichten'