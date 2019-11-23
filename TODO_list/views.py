from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Case
from .forms import TodoForm

def index(request):
    form = TodoForm
    todo_list = Case.objects.order_by('id')
    context = {'todo_list' : todo_list, 'form' : form}
    return render(request,'TODO/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    print(request.POST['text'])
    return redirect('index')
# Create your views here.
