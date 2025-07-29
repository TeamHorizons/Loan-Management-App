from django.contrib import admin
from kyc_management.models import KYC, Documents

# Register your models here.
admin.site.register(KYC)
admin.site.register(Documents)