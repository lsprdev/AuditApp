from django.test import TestCase

from controles.models import Auditor
from users.models import Usuario


class UsuarioAuditorTests(TestCase):
    def test_create_superuser_cria_perfil_de_auditor(self):
        user = Usuario.objects.create_superuser(
            username='superteste',
            email='superteste@example.com',
            password='SenhaForte123!',
        )

        self.assertTrue(Auditor.objects.filter(id_user=user).exists())
