from django.db import models


class Profile(models.Model):
    name = models.CharField(verbose_name="Nombre completo", max_length=100)
    my_avatar = models.ImageField(verbose_name="Avatar", upload_to="avatars/")
    occupation = models.CharField(verbose_name="Ocupación", max_length=100)
    biography = models.TextField(verbose_name="Biografía")
    age = models.IntegerField(verbose_name="Edad")
    phone = models.CharField(verbose_name="Teléfono", max_length=20)
    email = models.EmailField(verbose_name="Correo electrónico", max_length=100)
    created = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de modificacion", auto_now=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = [
            "-created",
        ]

    def __str__(self):
        return self.name
