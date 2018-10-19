from django.shortcuts import render, redirect
from todoapp.models import TodoList, Category

# Create your views here.
def index(request):
    return render(request, "personal/home.html")

def contact(request):
    # basic.html for c in content. iterates through list passed in param
    return render(request, "personal/basic.html", {"content":["Email:", "@gmail.com"]})

def include_sample(request):
    return render(request, "personal/sample_content.html")

def todoapp(request):
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager

    if request.method == "POST": #checking if the request method is a POST

        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted

            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo

    return render(request, "index.html", {"todos": todos, "categories":categories})