from django.contrib import admin

from .models import Beneficiaries, BeneficiaryAddress, District, Thana, PostCode, Ward, Village


admin.site.register(Beneficiaries)
admin.site.register(BeneficiaryAddress)
admin.site.register(District)
admin.site.register(Thana)
admin.site.register(PostCode)
admin.site.register(Ward)
admin.site.register(Village)
