import datetime

from foerderung.models import Foerderung
from rest_framework import serializers


class FoerderungSerializer(serializers.Serializer):
    class Meta:
        model = Foerderung
#        fields = "__all__"
        fields = ['foerdergebiet', 'thema', 'unterkategorie', 'foerderprogramm', 'foerdergeber', 'foerderart', 'foerderhoehe', 'nicht_foerderbare_ausgaben', 'foerderprogramm_bezeichnung', 'vorhabenbeginn', 'rechtsgrundlage', 'laufzeit']

    foerdergebiet = serializers.CharField(max_length=500)
    thema = serializers.CharField(max_length=500)
    unterkategorie = serializers.CharField(max_length=500)
    foerderprogramm = serializers.CharField(max_length=500)
    foerdergeber = serializers.CharField(max_length=500)
    foerderart = serializers.CharField(max_length=500)
    foerderhoehe = serializers.DecimalField(max_digits=8, decimal_places=2)
    nicht_foerderbare_ausgaben = serializers.DecimalField(max_digits=8, decimal_places=2)
    foerderprogramm = serializers.CharField(max_length=500)
    vorhabenbeginn = serializers.DateField(initial=datetime.date.today)
    rechtsgrundlage = serializers.CharField(max_length=500)
    laufzeit = serializers.CharField(max_length=500)
    foerderhoehe = serializers.CharField(max_length=500)
