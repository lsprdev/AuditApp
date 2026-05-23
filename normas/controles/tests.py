import importlib.util
from pathlib import Path

from django.test import TestCase

from controles.models import Norma


class InserirBaseTests(TestCase):
    def test_inserir_normas_com_id_zero(self):
        script_path = Path(__file__).resolve().parents[0] / 'inserir_base' / 'inserir_base.py'
        spec = importlib.util.spec_from_file_location('inserir_base_seed', script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        module.inserir_normas()

        self.assertEqual(Norma.objects.count(), 2)
        self.assertTrue(Norma.objects.filter(nome='ISO 27001').exists())
        self.assertTrue(Norma.objects.filter(nome='ISO 27701').exists())
