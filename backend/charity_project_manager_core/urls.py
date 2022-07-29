"""charity_project_manager_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from users.views import UserRetrieveUpdateViewSet
from projects.views import (ProjectsViewSet,
    ProjectCoordinatorsViewSet, ProjectBeneficiariesViewSet)
from beneficiaries.views import (BeneficiariesViewSet,
    DistrictViewSet, ThanaViewSet, PostCodeViewSet, WardViewSet, VillageViewSet,
    BeneficiaryAddressViewSet)

router = routers.DefaultRouter()
router.register('users', UserRetrieveUpdateViewSet)
router.register('projects', ProjectsViewSet)
router.register('project_coordinators', ProjectCoordinatorsViewSet)
router.register('projects_beneficiaries', ProjectBeneficiariesViewSet)
router.register('beneficiaries', BeneficiariesViewSet)
router.register('district', DistrictViewSet)
router.register('thana', ThanaViewSet)
router.register('post_code', PostCodeViewSet)
router.register('ward', WardViewSet)
router.register('village', VillageViewSet)
router.register('beneficiary_address', BeneficiaryAddressViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls')), # This line should stay at the end of the list
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
