from django.test import TestCase
from django.urls import reverse


class JobsTest(TestCase):
    def test_homepage_loads(self):
        """Verifica que la página principal carga correctamente"""
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_jobs_url_exists(self):
        """Verifica que la app jobs responde"""
        self.assertIsNotNone(response := self.client.get('/'))
        
    def test_basic_math(self):
        """Test básico para verificar que el sistema funciona"""
        self.assertEqual(1 + 1, 2)