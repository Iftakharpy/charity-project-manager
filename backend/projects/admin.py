from django.contrib import admin

from .models import Projects, ProjectBeneficiaries, ProjectCoordinators


admin.site.register(ProjectCoordinators)
admin.site.register(ProjectBeneficiaries)
admin.site.register(Projects)
