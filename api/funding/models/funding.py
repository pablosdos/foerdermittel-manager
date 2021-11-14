from enum import unique
import uuid
from django.db import models
from django.db.models.enums import TextChoices


class FundingArea(models.Model):

    name = models.CharField(max_length=64, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name


class FundingSponsor(models.Model):
    name = models.CharField(max_length=128, verbose_name='Fördergeber')
    telephone = models.CharField(max_length=64, verbose_name='Telefon')
    email = models.EmailField(verbose_name='Email')
    website = models.URLField(verbose_name='Website')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Fördergeber'
        verbose_name_plural = 'Fördergebern'


class FundingPlace(models.TextChoices):
    HE = 'Hessen', 'Hessen'
    BW = 'Baden Würtemberg', 'Baden Würtemberg'
    BA = 'Bayern', 'Bayern'
    RP = 'Rheinland-Pfalz', 'Rheinland-Pfalz'
    BR = 'Brandenburg', 'Brandenburg'
    BE = 'Berlin', 'Berlin'
    BM = 'Bremen', 'Bremen'
    NS = 'Niedersachsen', 'Niedersachsen'
    SA = 'Sachsen-Anhalt', 'Sachsen-Anhalt'
    HA = 'Hamburg', 'Hamburg'
    MV = 'Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'
    NW = 'Nordrhein-Westfalen', 'Nordrhein-Westfalen'
    SC = 'Sachsen', 'Sachsen'
    SH = 'Schleswig-Holstein', 'Schleswig-Holstein'
    AN = 'Sonstige', 'Sonstige'
    TH = 'Thüringen', 'Thüringen'
    WW = 'Bundesweit', 'Bundesweit'


class FundingType(models.TextChoices):
    SUBSIDY = 'Zuschuss', 'Zuschuss'
    CREDIT = 'Kredit', 'Kredit'
    BETEILIGUNG = 'Beteiligung', 'Beteiligung'
    BURGSCHAFT = 'Bürgschaft', 'Bürgschaft'
    DARLEHEN = 'Darlehen', 'Darlehen'
    GARANTIE = 'Garantie', 'Garantie'
    SONSTIGE = 'sonstige', 'sonstige'


class FundingProgramm(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, auto_created=True, verbose_name='id')

    name = models.CharField(max_length=512, blank=True,
                            null=True, verbose_name='Name')

    description = models.TextField(
        blank=True, null=True,  verbose_name='Beschreibung')
    type = models.CharField(verbose_name='Förderungsart',
                            max_length=56, null=True, choices=FundingType.choices)

    area = models.ManyToManyField(
        to=FundingArea, verbose_name='Förderungsbereich')

    region = models.CharField(choices=FundingPlace.choices,
                              max_length=64, default='RP', verbose_name='Födergebiet')

    min_citzens = models.IntegerField(
        default=0, verbose_name='Mindest Einwöhnerszahl')

    url = models.URLField(unique=True, verbose_name='URL')

    sponsor = models.ForeignKey(
        to=FundingSponsor, null=True,  on_delete=models.SET_NULL, verbose_name='Fördergeber')

    last_updated = models.DateTimeField(
        auto_now=True, verbose_name='Letzt bearbeitet')

    who_last_updated = models.ForeignKey(
        to='users.CustomUser', null=True, on_delete=models.SET_NULL, verbose_name='Letzt bearbeitet bei')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Förderungsprogramm'
        verbose_name_plural = 'Förderungsprogramme'
