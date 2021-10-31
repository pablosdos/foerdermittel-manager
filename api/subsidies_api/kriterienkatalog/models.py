from django.db import models
from rest_framework.settings import api_settings

STATES_CHOICES = (
    ('Baden-Würtemberg','Baden-Würtemberg'),
    ('Bayern', 'Bayern'),
    ('Berlin','Berlin'),
    ('Brandenburg','Brandenburg'),
    ('Bremen','Bremen'),
    ('Niedersachsen', 'Niedersachsen'),
    ('Sachsen-Anhalt', 'Sachsen-Anhalt'),
    ('Hamburg', 'Hamburg'),
    ('Hessen', 'Hessen'),
    ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'),
    ('Nordrhein-Westfalen', 'Nordrhein-Westfalen'),
    ('Rheinland-Pfalz', 'Rheinland-Pfalz'),
    ('Saarland', 'Saarland'),
    ('Sachsen', 'Sachsen'),
    ('Schleswig-Holstein', 'Schleswig-Holstein'),
    ('Thüringen', 'Thüringen'),
)

class Kriterienkatalog(models.Model):
    foerderprogramm = models.CharField(max_length=500)
    foerdergebiet = models.CharField(max_length=80, choices=STATES_CHOICES, default=None)
    foerdergeber = models.CharField(max_length=500)
    foerderhoehe = models.DecimalField(max_digits=8, decimal_places=2)
    foerderfaehige_kosten = models.DecimalField(max_digits=8, decimal_places=0)
    nicht_foerderbare_ausgaben = models.CharField(max_length=500)
    laufzeit = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Kriterienkataloge'

    def __str__(self):
        return 'Kriterienkatalog: ' + self.foerderprogramm