from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	# urls 에 설정된 view 함수에 대한 매핑이 예측한대로 되었는지 테스트
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	# request 요청 시 응답이 만들어지는 home_page 에서 원하는 결과대로 리턴하는 지 테스트
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		# response.content 타입은 byte 형식으로 파이선 문자열로 변경하기 위해 b 를 붙여준다.
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))


