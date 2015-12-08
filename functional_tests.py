from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# 셀레늄을 이용한 사용자 반응 테스트 
class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
		
	# 리스트에 해당 row 가 존재하는지 확인하는 함수 
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])			
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		# 웹 사이트 확인 요청 
		self.browser.get('http://localhost:8000')
		
		# browser 로 수신한  title 에 To-Do 를 포함하는지 확인 
		self.assertIn('To-Do', self.browser.title)

		# browser 에서 h1 태그가 있는 text 를 찾고, To-Do 가 포함됬는지 확인 	
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# browser 에서 id_new_item element 를 찾고, element 의 attribute 가 placeholder 인 곳에 값을 체크 
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertIn(inputbox.get_attribute('placeholder'), 'input work item')

		# browser 에 id_new_item element 에 'Buy bird' 를 입력 
		# testbox 에 사용자가 입력. (Buy bird)		
		inputbox.send_keys('Buy bird')
		 
		# Entry 키를 치면, 페이지가 갱신되고, 전체 목록에 'Buy Bird' 가 추가된다. 
		inputbox.send_keys(Keys.ENTER)
	
		# 추가된 항목이 제대로 들어갔는지 확인한다. 
		self.check_for_row_in_list_table('1:Buy bird')
		
		# 두 번째 입력 테스트
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('make homeworld using bird')
		inputbox.send_keys(Keys.ENTER)
		
		# 두 번째 목록 확인 
		self.check_for_row_in_list_table('2:make homeworld using bird')
		
					
		self.fail('Finish the Test')
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')