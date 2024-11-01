from urllib import response
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from main.views import main

class HomePageTest(TestCase):
    # Тестирование домашней страницы

    def test_uses_home_template(self):
        # Испльзуется домашний шаблон
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/index.html')

    def test_can_save_a_POST_request(self):
        # Можно сохранить post-запрос
        response = self.client.post('/', data={'item_text': 'A new item'})
        self.assertIn('A new item', response.content.decode())
        self.assertTemplateUsed(response, 'main/index.html')

    def test_home_page_return_correct_html(self):
        # Тест на возврат правильно html страницы
        #request = HttpRequest()
        #response = main(request)
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>FinPool</title>', html)
        self.assertTrue(html.endswith('</html>'))

        # Проверяем какой шаблон используется у нас шаблон.
        self.assertTemplateUsed(response, 'main/index.html')