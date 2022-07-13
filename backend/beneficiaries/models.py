from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

from projects.models import Projects
from users.models import CustomUserModel


class Beneficiaries(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    display_image = models.ImageField(height_field=settings.IMAGE_SIZES['person_profile'].height, width_field=settings.IMAGE_SIZES['person_profile'].width, blank=True)
    description = models.TextField(blank=True)

    last_updated_at = models.DateTimeField(auto_now=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)


class ProjectBeneficiaries(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiaries, on_delete=models.CASCADE)
    benefactor = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)

    benefit_receive_date_time = models.DateTimeField(null=True, blank=True)
    beneficiary_join_date_time = models.DateTimeField(auto_now_add=True, default=timezone.now)




class District(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')


class Thana(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')


class PostOffice(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')


class Ward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')


class Village(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')


class BeneficiaryAddress(models.Model):
    beneficiary = models.ForeignKey(Beneficiaries, on_delete=models.CASCADE)
    
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, null=True, blank=True)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE, null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True, blank=True)
    Village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
