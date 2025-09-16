from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MedicoAuditor  # Asegurate de importar correctamente

@admin.register(MedicoAuditor)
class MedicoAuditorAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(groups__name='Auditor')