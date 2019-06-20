from django.db import models

# Create models for menu categories
SIZES = (
    ('S', 'Small'),
    ('L', 'Large'),
)

PIZZA_TOPPINGS_TYPES = (
    ('Cheese', 'Cheese'),
    ('1 Topping', '1 topping'),
    ('2 Toppings', '2 Toppings'),
    ('3 Toppings', '3 Toppings'),
    ('Special', 'Special'),
)

class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
    
class RegularPizza(models.Model):
    topping_type = models.CharField(max_length=10, choices=PIZZA_TOPPINGS_TYPES)
    size = models.CharField(max_length=1, choices=SIZES)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.topping_type} ({self.size}) - ${self.price}"

class SicilianPizza(models.Model):
    topping_type = models.CharField(max_length=10, choices=PIZZA_TOPPINGS_TYPES)
    size = models.CharField(max_length=1, choices=SIZES)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.topping_type} ({self.size}) - ${self.price}"
    
class Sub(models.Model):
    sub_type = models.CharField(max_length=30)
    size = models.CharField(max_length=1, choices=SIZES)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.sub_type} ({self.size}) - ${self.price}"

class Pasta(models.Model):
    pasta_type = models.CharField(max_length=30)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.pasta_type} - ${self.price}"
    
class Salad(models.Model):
    salad_type = models.CharField(max_length=20)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.salad_type} - ${self.price}"
    
class DinnerPlatter(models.Model):
    platter_type = models.CharField(max_length=20)
    size = models.CharField(max_length=1, choices=SIZES)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.platter_type} ({self.size}) - ${self.price}"
