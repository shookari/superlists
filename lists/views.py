from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# TODO : view 함수에서 response 객체를 리턴하도록 수정해야함
def home_page(request):
	return HttpResponse("<html><title>To-Do lists</title></html>")

