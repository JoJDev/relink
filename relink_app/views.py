from django.shortcuts import render, redirect, get_object_or_404
from .models import Link


# Create your views here.
def index(request):
    return render(request, "relink_app/index.html")


def relink(request, slug_url: str = ""):
    link = get_object_or_404(Link, slug=slug_url)
    return redirect(link.url)
