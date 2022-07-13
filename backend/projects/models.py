from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone


class Projects(models.Model):
    title = models.CharField(_("Title"), max_length=255, blank=False)
    description = models.TextField(_("Description"), )
    eligibility = models.TextField(_("Beneficiary eligibility"))
    banner_image = models.ImageField(height_field=settings.IMAGE_SIZES['banner'].height, width_field=settings.IMAGE_SIZES['banner'].width, blank=True)

    total_budget = models.DecimalField(max_digits=24, decimal_places=4)
    total_budget = models.DecimalField(max_digits=24, decimal_places=4)

    start_date = models.DateField()
    end_date = models.DateField()


class ProjectCoordinators(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    coordinator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    assign_date_time = models.DateTimeField(auto_now_add=True, default=timezone.now)
