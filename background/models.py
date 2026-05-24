from django.db import models


class Background(models.Model):
    home_image = models.ImageField(
        verbose_name="Imagen de portada", upload_to="background/"
    )
    biography_image = models.ImageField(
        verbose_name="Imagen de biografía", upload_to="background/"
    )
    portfolio_image = models.ImageField(
        verbose_name="Imagen de portafolio", upload_to="background/"
    )

    created = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de modificacion", auto_now=True)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        ordering = [
            "-created",
        ]

    def __str__(self):
        return "Imagenes de la página"
