from django.db import models


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return f'{self.name} Стоимость: {self.price}'
