from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig

class TestTodoconfig(TestCase):
    def test_app(self):
        self.assertEqual('todo', TodoConfig.name)
        self.assertEqual('todo', apps.get_app_config('todo'))