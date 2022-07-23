from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Beneficiaries(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    profile_picture = models.ImageField(_("Profile Picture"), blank=True, null=True)
    description = models.TextField(blank=True)

    last_updated_at = models.DateTimeField(auto_now=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)


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
