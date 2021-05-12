from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from To_Do_App.models import Todo
from django.http import HttpResponseRedirect


def home(request):
    todo_items = Todo.objects.filter(is_completed=False)
    completed_items = Todo.objects.filter(is_completed=True)
    params = {
        'todo_items': todo_items,
        'completed_items': completed_items
        }
    return render(request, "to_do_app/index.html", params)


@csrf_exempt
def add_todo(request):
    print(f"The POST is {request.POST}")
    content = request.POST["content"]
    created_object = Todo.objects.create(text=content)
    print(f"Coontent:>>> {content}")
    print(created_object.id)
    print(created_object)
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, todo_id):
    print(f"Todo Id is {todo_id}")
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


@csrf_exempt
def complete_todo(request, todo_id):
    print(f"To do is {todo_id}")
    completed_item = Todo.objects.get(id=todo_id)
    completed_item.is_completed=True
    completed_item.save()
    return HttpResponseRedirect("/")


@csrf_exempt
def uncomplete_todo(request, todo_id):
    print(f"To do is {todo_id}")
    incompleted_item = Todo.objects.get(id=todo_id)
    incompleted_item.is_completed=False
    incompleted_item.save()
    return HttpResponseRedirect("/")
