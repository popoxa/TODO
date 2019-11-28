from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Case
from .forms import TodoForm

from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CaseSerializer
from rest_framework.generics import get_object_or_404

def index(request):
    form = TodoForm
    todo_list = Case.objects.order_by('id')
    context = {'todo_list': todo_list, 'form': form}
    return render(request,'TODO/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Case(text_case=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Case.objects.get(pk=todo_id)
    todo.complete_case = True
    todo.save()

    return redirect('index')

def deletecomplete(request):
    Case.objects.filter(complete_case__exact=True).delete()

    return redirect('index')

def deleteall(request):
    Case.objects.all().delete()

    return redirect('index')


class CaseView(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

