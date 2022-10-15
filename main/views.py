from django.shortcuts import render, redirect
from .forms import Gans_form
from .models import GunsModel
# Create your views here.

def text(request):
        
    if request.method=="POST":
        form=Gans_form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            name=data.get("name")
            quality=data.get("quality")
            discription=data.get("discription")
            price=data.get("price")
            GunsModel.objects.create(name=name, quality=quality, discription=discription, price=price)
            print(data)
            return redirect("home")
    form=Gans_form()
    v=GunsModel.objects.all()
    return render(request, "index.html", {"form":form, "v":v})
def text_2(request):
    return render(request, "index.html")
def menu(request):
    return render(request, "menu.html")
def login(request):
    return render(request, "login.html")








