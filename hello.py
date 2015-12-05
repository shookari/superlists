# 셀레늄을 이용한 사용자 반응 테스트 
class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
			
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.fail ('finish the test')
		# 웹 사이트 확인 요청 
		self.browser.get('http://localhost:8000')
		
		# browser 로 수신한  title 에 To-Do 를 포함하는지 확인 
		self.assertIn('To-Do', self.browser.title)

		# browser 에서 h1 태그가 있는 text 를 찾고, To-Do 가 포함됬는지 확인 	
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# browser 에서 id_new_item element 를 찾고, element 의 attribute 가 placeholder 인 곳에 값을 체크 
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertIn(inputbox.get_attribute('placeholder'), 'Working Item Input')

		# browser 에 id_new_item element 에 'Buy bird' 를 입력 
		# testbox 에 사용자가 입력. (Buy bird)		
		inputbox.send_keys('Buy bird')
		
		# Entry 키를 치면, 페이지가 갱신되고, 전체 목록에 'Buy Bird' 가 추가된다. 
		inputbox.send_keys(Keys.ENTER)
	
		# 추가된 항목이 제대로 들어갔는지 확인한다. 
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		
		self.assertTrue(any(row.text == '1: Buy bird' for row in rows),)
		self.fail('Finish the Test')
		
	if __name__ == '__main__':
		unittest.main(warnings='ignore')