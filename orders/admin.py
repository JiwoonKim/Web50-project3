from django.contrib import admin
from .models import DinnerPlatter, Order, Pasta, PizzaTopping, Salad, SubTopping

# Register your models here.
admin.site.register(DinnerPlatter)
admin.site.register(Order)
admin.site.register(Pasta)
admin.site.register(PizzaTopping)
admin.site.register(Salad)
admin.site.register(SubTopping)