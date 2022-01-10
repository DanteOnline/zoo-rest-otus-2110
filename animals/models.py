from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    # Семейсвто - медведь
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Kind(models.Model):
    # Вид - Бурый (медведь)
    name = models.CharField(max_length=64)
    family = models.ForeignKey(Family, on_delete=models.PROTECT, db_index=True)
    image = models.ImageField(upload_to='kind', blank=True, null=True)

    full_name = models.CharField(max_length=128, blank=True, null=True)

    unique_together = [['name', 'family']]

    def __str__(self):
        return self.name

    def animal_count(self):
        result = Animal.objects.filter(kind=self).count()
        return result


class AnimalCard(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Food(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=64)
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT)
    card = models.OneToOneField(AnimalCard, on_delete=models.CASCADE, blank=True, null=True)
    foods = models.ManyToManyField(Food)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
