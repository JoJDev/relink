from django.db import models

# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=50, default="title")
    slug = models.SlugField(default="")
    url = models.URLField(max_length=200, default="")
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    mod_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    expire_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, default=None, blank=True
    )
    public = models.BooleanField(default=True)
    auto_redirect = models.BooleanField(default=False)
    seconds_wait = models.IntegerField(default=0)
    url_broken = models.SmallIntegerField(default=0)

    """
from relink_app.models import Link
l = Link.objects.all() 
    """

    def __str__(self):
        return (
            self.name + " (" + (self.slug
            if len(self.slug) < 10
            else self.slug[:10]) + ")"
        )

        
