from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60*60*24*7)
def index(request):
	pictures = []
	for file in range(9):
		pictures.append(f'/images/{file}.jpg')
	return render(request,'base/index.html',{'pictures': pictures})
