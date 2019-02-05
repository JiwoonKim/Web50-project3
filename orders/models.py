from django.db import models

# Create choices used in models
PIZZAS = (
    ('regular', 'Regular'),
    ('sicilian', 'Sicilian'),
)
SIZES = (
    ('S', 'Small'),
    ('L', 'Large'),
)

# Create models for menu categories
class DinnerPlatter(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=1, choices=SIZES)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.size})"

class Pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class PizzaTopping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Salad(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class SubTopping(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"