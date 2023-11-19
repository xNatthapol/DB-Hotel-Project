from django.contrib import admin
from .models import Customer, Payment, Account, Facility, Room, ReservedRoom, ReservedFacility, Stock, Ingredient, MealList, Recipe, Employee, Role

# Register all models with the admin site
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Account)
admin.site.register(Facility)
admin.site.register(Room)
admin.site.register(ReservedRoom)
admin.site.register(ReservedFacility)
admin.site.register(Stock)
admin.site.register(Ingredient)
admin.site.register(MealList)
admin.site.register(Recipe)
admin.site.register(Employee)
admin.site.register(Role)
