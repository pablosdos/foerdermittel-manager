from django.db import models
from kriterienkatalog.models import Kriterienkatalog
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

CATEGORY_CHOICES = (
    ('Arbeit','Arbeit'),
    ('Aus- & Weiterbildung', 'Aus- & Weiterbildung'),
    ('Corona-Hilfe','Corona-Hilfe'),
    ('Digitalisierung','Digitalisierung'),
    ('Energieeffizienz & Erneuerbare Energien','Energieeffizienz & Erneuerbare Energien'),
    ('Existenzgründung & -festigung', 'Existenzgründung & -festigung'),
    ('Forschung & Innovation (themenoffen)', 'Forschung & Innovation (themenoffen)'),
    ('Forschung & Innovation (themenspezifisch)', 'Forschung & Innovation (themenspezifisch)'),
    ('Gesundheit & Soziales', 'Gesundheit & Soziales'),
    ('Infrastruktur', 'Infrastruktur'),
    ('Kultur, Medien & Sport', 'Kultur, Medien & Sport'),
    ('Landwirtschaftlich & Ländliche Entwicklung', 'Landwirtschaftlich & Ländliche Entwicklung'),
    ('Regionalförderung', 'Regionalförderung'),
    ('Smart Cities & Regionen', 'Smart Cities & Regionen'),
    ('Städtebau & Stadterneuerung', 'Städtebau & Stadterneuerung'),
    ('Umwelt- & Naturschutz', 'Umwelt- & Naturschutz'),
    ('Unternehmensfinanzierung', 'Unternehmensfinanzierung'),
    ('Wohnungsbau & Modernisierung', 'Wohnungsbau & Modernisierung'),
)

SUBCATEGORY_CHOICES = (
    ('Schulen','Schulen'),
    ('Sporteinrichtung', 'Sporteinrichtung'),
    ('Wasserwirtschaft','Wasserwirtschaft'),
    ('Abwasserwirtschaft','Abwasserwirtschaft'),
    ('Breitbandnetzte','Breitbandnetzte'),
    ('Verkehrsinfrastruktur', 'Verkehrsinfrastruktur'),
    ('Abfallwirtschaft', 'Abfallwirtschaft'),
    ('Stadtentwicklung', 'Stadtentwicklung'),
    ('Dorfentwicklung', 'Dorfentwicklung'),
    ('Tourismus', 'Tourismus'),
    ('Krankenhaus', 'Krankenhaus'),
    ('Behinderteneinrichtungen', 'Behinderteneinrichtungen'),
    ('Flüchtlingsunterkünfte', 'Flüchtlingsunterkünfte'),
    ('Baulanderschließung', 'Baulanderschließung'),
    ('Planungsleistung', 'Planungsleistung'),
    ('Grundstücke', 'Grundstücke'),
)

class Foerderung(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    foerdergebiet = models.CharField(max_length=80, choices=STATES_CHOICES, default=None)
    thema = models.CharField(max_length=80, choices=CATEGORY_CHOICES, default=None)
    unterkategorie = models.CharField(max_length=80, choices=SUBCATEGORY_CHOICES, default=None)
    foerderprogramm = models.CharField(max_length=500)
    foerdergeber = models.CharField(max_length=500)
    foerderart = models.CharField(max_length=500)
    foerderhoehe = models.DecimalField(max_digits=8, decimal_places=2)
    nicht_foerderbare_ausgaben = models.DecimalField(max_digits=8, decimal_places=0)
    kriterienkatalog = models.OneToOneField(Kriterienkatalog, null=True, on_delete=models.CASCADE)
    vorhabenbeginn = models.DateField()
    rechtsgrundlage = models.CharField(max_length=500)
    laufzeit = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Förderungen'

    def __str__(self):
        return self.foerderprogramm