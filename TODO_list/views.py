from django.shortcuts import render

def index(request):
    context = {}
    return render(request,'TODO/index.html', context)
# Create your views here.
