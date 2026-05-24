from django.db import models


class Project(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    url = models.URLField(
        verbose_name="Link de informacion adicional", null=True, blank=True
    )
    created = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de modificacion", auto_now=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = [
            "-created",
        ]

        def __str__(self):
            return self.title
