from django.shortcuts import render, redirect

def landing_page(request):
    return render(request,
                  "<h1>Site is under maintenance</h1>")
