from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home/home.html')

def all_product(request):
    return render(request, "home/product.html")
