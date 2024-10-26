from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from main.views import main

class HomePageTest(TestCase):
    # Тестирование домашней страницы

    def test_home_page(self):
        # Тест корневого url 
        found = resolve('/')
        self.assertEqual(found.func, main)

    def test_home_page_return_correct_html(self):
        # Тест на возврат правильно html страницы
        request = HttpRequest()
        response = main(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>FinPool</title>', html)
        self.assertTrue(html.endswith('</html>'))