from django.db import models

# Create models for menu categories
class Order(models.Model):
    pass

    def __str__(self):
        return f"{self.platters.all()}, {self.pastas.all()}, {self.salads.all()}"

# Create choices used in models
SIZES = (
    ('S', 'Small'),
    ('L', 'Large'),
)

# Create models for menu categories
class DinnerPlatter(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="platters")
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=1, choices=SIZES)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.size})"

class Pasta(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="pastas")
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    name = models.CharField(max_length=10)
    size = models.CharField(max_length=1, choices=SIZES)
    topping = models.IntegerField()

class PizzaTopping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Salad(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="salads")
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class SubTopping(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"
