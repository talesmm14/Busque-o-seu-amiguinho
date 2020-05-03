from django.shortcuts import render


# Create your views here.

def page_home_view(request):
    return render(request, "pages/index.html")
