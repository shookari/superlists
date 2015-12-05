from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

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
