from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    return (request, "todo/todo_list.html")