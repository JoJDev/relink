import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Link


# Create your views here.
def index(request):
    return render(request, "relink_app/index.html")


def relink(request, slug_url: str = ""):
    link: Link = get_object_or_404(Link, slug=slug_url)
    if link.public:
        if (
            link.expire_date is not None
            and link.expire_date.timestamp() < datetime.datetime.now().timestamp()
        ):
            return redirect("/")

        if link.auto_redirect and link.seconds_wait <= 0:
            # auto_re = true y seconds = 0 es para redirigirse automaticamente y
            # sin esperar al url
            return redirect(link.url)

        context: dict = {
            "seconds": link.seconds_wait,
            "auto_redirect": link.auto_redirect,
            "url": link.url,
        }

        return render(request, "relink_app/relink.html", context=context)

    return redirect("/")
