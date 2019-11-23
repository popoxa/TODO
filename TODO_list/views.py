from django.shortcuts import render

from .models import Case

def index(request):
    todo_list = Case.objects.order_by('id')
    context = {'todo_list' : todo_list}
    return render(request,'TODO/index.html', context)
# Create your views here.
