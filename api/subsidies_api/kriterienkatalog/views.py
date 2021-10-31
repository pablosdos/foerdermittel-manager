from rest_framework import viewsets
from rest_framework import permissions
from kriterienkatalog.serializers import KriterienkatalogSerializer
from rest_framework.response import Response
from kriterienkatalog.models import Kriterienkatalog


class KriterienkatalogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Kriterienkatalog.objects.all().order_by('foerderprogramm')
    serializer_class = KriterienkatalogSerializer
#    permission_classes = [permissions.IsAuthenticated]



n_classes = [permissions.IsAuthenticated]