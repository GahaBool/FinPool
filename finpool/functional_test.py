from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import unittest

class NewVisitorTest(unittest.TestCase):
    # Тест нового посетителя

    def setUp(self):
        # Установка 
        self.browser = webdriver.Chrome()

    
    def test_open_main_window(self):
        # Добавление платижа который можно потом увидеть в истории
        self.browser.get('http://localhost:8000')
        # Проверка наличие заголовка 
        self.assertIn('FinPool', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('FinPool App', header_text)

        # Ввод элемент списка
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a deposite'
        )

        # При новых покупках идет добавление "1000р"
        inputbox.send_keys('1000 р')
        
        # После нажатия на Enter, страница обновляется, и теперь страница
        # Содержит "1: 1000 р" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_item_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: 1000 р' for row in rows),
            "Новый элемент в списках таблицы"
        )

        self.fail('Закончить тест!')

    def tearDown(self) -> None:
        # Отключение
        self.browser.quit()

if __name__ == "__main__":
    unittest.main(warnings='ignore')


