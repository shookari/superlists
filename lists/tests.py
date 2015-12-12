from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item

class ItemModelTest(TestCase):
	def test_saving_and_retriveing_item(self):
		# object 생성 및 속성 부여 후 저장(save())
		first_item = Item()
		first_item.text = 'First Item'
		first_item.save()
		
		second_item = Item()
		second_item.text = 'Second Item'
		second_item.save()
		
		# Object 를 통해 쿼리 수행 가능. 
		# -all 을 통해 모든 레코드 추출 : 결과 QuerySet 이라는 리스트 형태의 객체 반환 
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, first_item.text)
		self.assertEqual(second_saved_item.text, second_item.text)
		

# Create your tests here.
class HomePageTest(TestCase):
	# urls 에 설정된 view 함수에 대한 매핑이 예상대로 리턴되는지 되었는지 테스트
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	# request 요청 시 응답이 만들어지는 home_page 에서 원하는 결과대로 리턴하는 지 테스트
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		
		# view 함수(home_page)에서 리턴된 결과와 html 결과가 같은 지 테스트
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

	# post 요청에 대한 응답 처리 확인로직
	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'

		TestStr = 'new work item A'
		request.POST['item_text'] = TestStr
		
		response = home_page(request)
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, TestStr)	
				
		self.assertIn(TestStr, response.content.decode()) 
		expected_html = render_to_string(
			'home.html',
			{'new_item_text': TestStr}
		)
		self.assertEqual(response.content.decode(), expected_html)