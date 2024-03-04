from django.db import models  # noqa F401


class Pokemon(models.Model):
    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='pokemons_image', null=True)

    def __str__(self):
        return self.name