from django.shortcuts import render

# Create your views here.

# render  
#request 에 대해  랜더링할 템플릿명을 지정하면, Django 는 앱 폴더 내에 templates 를 검색하고,
# 템플릿 콘텐츠를 기반으로 HttpResponse 를 만들어줌.
def home_page(request):
	return render(request, 'home.html')

