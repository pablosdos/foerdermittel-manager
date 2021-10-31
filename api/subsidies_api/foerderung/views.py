from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from foerderung.serializers import FoerderungSerializer
from rest_framework.response import Response
from foerderung.models import Foerderung


class FoerderungViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Foerderung.objects.all().order_by('created_at')
    serializer_class = FoerderungSerializer
#    permission_classes = [permissions.IsAuthenticated]



n_classes = [permissions.IsAuthenticated]