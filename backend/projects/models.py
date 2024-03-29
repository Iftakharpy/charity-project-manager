from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

from beneficiaries.models import Beneficiaries


class Projects(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    title = models.CharField(_("Title"), max_length=255, blank=False)
    description = models.TextField(_("Description"), )
    eligibility = models.TextField(_("Beneficiary eligibility"))
    banner_image = models.ImageField(blank=True, null=True)

    total_budget = models.DecimalField(max_digits=24, decimal_places=4)
    budget_per_beneficiary = models.DecimalField(max_digits=24, decimal_places=4)

    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.title} - {self.total_budget}"


class ProjectCoordinators(models.Model):
    class Meta:
        verbose_name = 'Project Coordinator'
        verbose_name_plural = 'Project Coordinators'
        constraints = [
            models.UniqueConstraint(fields=[
                                    'project', 'coordinator'], name="%(app_label)s_%(class)s__check_project_and_coordinator_is_unique_together")
        ]

    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    coordinator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    assign_date_time = models.DateTimeField(
        auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Coordinator: {self.coordinator} Project: {self.project}"


class ProjectBeneficiaries(models.Model):
    class Meta:
        verbose_name = 'Project Beneficiary'
        verbose_name_plural = 'Project Beneficiaries'
        constraints = [
            models.UniqueConstraint(fields=[
                                    'project', 'beneficiary'], name="%(app_label)s_%(class)s__check_project_and_beneficiary_is_unique_together")
        ]

    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiaries, on_delete=models.CASCADE)
    benefactor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    benefit_receive_date_time = models.DateTimeField(null=True, blank=True)
    beneficiary_join_date_time = models.DateTimeField(
        auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Beneficiary: {self.beneficiary} Project: {self.project}"
