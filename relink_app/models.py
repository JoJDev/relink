from django.db import models

# Create your models here.


class Link(models.Model):
    name = models.CharField(
        max_length=50,
        default="title",
        verbose_name="Nombre del enlazador",
        help_text="Nombre para identificar al enlazador",
    )
    slug = models.SlugField(default="", verbose_name="Slug (a acceder)")
    url = models.URLField(max_length=200, verbose_name="URL (a redirigir)")
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    mod_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    expire_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        default=None,
        blank=True,
        verbose_name="Fecha de expiración",
        help_text="(Dejar en blanco para no tener fecha de expiración)"
    )
    text_link = models.CharField(
        max_length=200,
        default="",
        blank=True,
        verbose_name="Texto de mostrador",
        help_text="Texto que se mostrara como encabezado al acceder al enlace para ser redirigido",
    )
    public = models.BooleanField(default=True, verbose_name="Esta activado")
    auto_redirect = models.BooleanField(
        default=False, verbose_name="Redireccionar automaticamente"
    )
    seconds_wait = models.IntegerField(default=0, verbose_name="Segundos a esperar")
    url_broken = models.SmallIntegerField(
        default=0, verbose_name="Contador de avisos de enlace roto"
    )

    """
from relink_app.models import Link
l = Link.objects.all() 
    """

    def __str__(self):
        return (
            self.name + " ("
            + (self.slug if len(self.slug) < 10 else self.slug[:10])
            + ")"
        )
