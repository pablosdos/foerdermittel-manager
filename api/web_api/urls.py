from django.contrib import admin
from django.urls import path, include

from .views import FundingProgrammViewSets, import_funding_projects, process_contact_messsage


urlpatterns = [
    path('programs/', FundingProgrammViewSets.as_view({'get': 'list'})),
    path('file-upload/', import_funding_projects),
    path('contact/', process_contact_messsage)
]
