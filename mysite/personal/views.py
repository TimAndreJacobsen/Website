from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "personal/home.html")

def contact(request):
    #basic.html for c in content. iterates through list passed in param
    return render(request, "personal/basic.html", {"content":["Email:", "@gmail.com"]})

def include_sample(request):
    return render(request, "personal/sample_content.html")