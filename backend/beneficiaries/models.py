from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Beneficiaries(models.Model):
    class Meta:
        verbose_name = 'Beneficiary'
        verbose_name_plural = 'Beneficiaries'

    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    profile_picture = models.ImageField(
        _("Profile Picture"), blank=True, null=True)
    description = models.TextField(blank=True)

    last_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name} Phone Number: {self.phone_number}"


class District(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    def __str__(self) -> str:
        return f"{self.name}"


class Thana(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    def __str__(self) -> str:
        return f"{self.name}"


class PostCode(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    def __str__(self) -> str:
        return f"{self.name}"


class Ward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    def __str__(self) -> str:
        return f"{self.name}"


class Village(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    def __str__(self) -> str:
        return f"{self.name}"


class BeneficiaryAddress(models.Model):
    class Meta:
        verbose_name = 'Beneficiary Address'
        verbose_name_plural = 'Beneficiary Addresses'

    beneficiary = models.ForeignKey(Beneficiaries, on_delete=models.CASCADE)

    district = models.ForeignKey(
        District, on_delete=models.CASCADE, null=True, blank=True)
    thana = models.ForeignKey(
        Thana, on_delete=models.CASCADE, null=True, blank=True)
    post_office = models.ForeignKey(
        PostCode, on_delete=models.CASCADE, null=True, blank=True)
    ward = models.ForeignKey(
        Ward, on_delete=models.CASCADE, null=True, blank=True)
    village = models.ForeignKey(
        Village, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.beneficiary} - District: {self.district} Thana: {self.thana}"
