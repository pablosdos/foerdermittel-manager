"""subsidies_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from foerderung import views as foerderung_views
from kriterienkatalog import views as kriterienkatalog_views

router = routers.DefaultRouter()
router.register(r'foerderungen', foerderung_views.FoerderungViewSet)
router.register(r'kriterienkataloge', kriterienkatalog_views.KriterienkatalogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

admin.site.site_header = "Smarter Fördermittelmanager"
admin.site.site_title = "Smarter Fördermittelmanager"
admin.site.index_title = "Willkommen im Admin-Bereich des smarten Fördermittelmanagers."