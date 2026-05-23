from django.db.models.signals import post_save
from django.dispatch import receiver

from controles.models import Auditor
from users.models import Usuario


@receiver(post_save, sender=Usuario)
def garantir_perfil_de_auditor(sender, instance, created, **kwargs):
    auditor_existente = Auditor.objects.filter(id_user=instance).first()

    if auditor_existente:
        return

    nome_auditor = instance.get_full_name() or instance.username

    Auditor.objects.create(
        id_user=instance,
        nome_auditor=nome_auditor,
        documento_auditor='N/A',
    )
