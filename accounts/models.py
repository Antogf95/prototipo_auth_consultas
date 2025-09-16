from django.contrib.auth.models import User

class MedicoAuditor(User):
    class Meta:
        proxy = True
        verbose_name = "Médico Auditor"
        verbose_name_plural = "Médicos Auditores"