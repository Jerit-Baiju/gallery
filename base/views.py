from django.shortcuts import render

# Create your views here.

def index(request):
	pictures = []
	for file in range(9):
		pictures.append(f'/images/{file}.jpg')
	return render(request,'base/index.html',{'pictures': pictures})
