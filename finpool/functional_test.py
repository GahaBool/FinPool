from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('FinPool', header_text)

        # Ввод элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a deposite'
        )

        # При новых покупках идет добавление "1000р"
        inputbox.send_keys('Депозит в "1000 р"!')
        
        # После нажатия на Enter, страница обновляется, и теперь страница
        # Содержит "1: 1000 р" в качестве элемента списка
        inputbox.send_keys
        time.sleep(1)

        table = self.browser.find_element_by_id('id_deposite_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 1000 р' for row in rows)
        )

        self.fail('Закончить тест!')

    def tearDown(self) -> None:
        # Отключение
        self.browser.quit()

if __name__ == "__main__":
    unittest.main(warnings='ignore')


