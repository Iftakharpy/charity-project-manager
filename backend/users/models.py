from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUserModel(AbstractUser):
    """
    Customizes django.contrib.auth.AbstractUser by removing username field.
    Instead of using username field for user identification email is used
    for identification and new field phone_number is added.
    """

    # run `pipenv run python manage.py makemigrations --dry-run --verbosity 3`
    # to see all fields
    username = None
    email = models.EmailField(
        _("Email"), unique=True, blank=False, null=False, db_index=True
    )
    phone_number = models.CharField(_("Phone Number"), max_length=32)
    profile_picture = models.ImageField(_("Profile Picture"), blank=True, null=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.email}"
