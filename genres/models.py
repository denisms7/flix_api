from django.db import models
from django.utils.translation import gettext_lazy as _

class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Nome"), unique=True)

    class Meta:
        verbose_name = _("Genero")
        verbose_name_plural = _("Generos")

    def __str__(self):
        return self.name  
