import datetime

from kriterienkatalog.models import Kriterienkatalog
from rest_framework import serializers


class KriterienkatalogSerializer(serializers.Serializer):
    class Meta:
        model = Kriterienkatalog
#        fields = "__all__"
        fields = ['foerderprogramm_bezeichnung', 'foerdergebiet', 'foerdergeber', 'foerderhoehe', 'foerderfaehige_kosten', 'nicht_foerderbare_ausgaben', 'laufzeit']

    foerderprogramm = serializers.CharField(max_length=500)
    foerdergebiet = serializers.CharField(max_length=500)
    foerdergeber = serializers.CharField(max_length=500)
    foerderhoehe = serializers.DecimalField(max_digits=8, decimal_places=2)
    foerderfaehige_kosten = serializers.DecimalField(max_digits=8, decimal_places=2)
    nicht_foerderbare_ausgaben = serializers.DecimalField(max_digits=8, decimal_places=2)
    laufzeit = serializers.DecimalField(max_digits=8, decimal_places=0)