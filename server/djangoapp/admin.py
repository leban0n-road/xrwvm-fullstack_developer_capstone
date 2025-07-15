# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to show CarModel within CarMake admin page
class CarModelInline(admin.TabularInline):  # You can use StackedInline if you prefer
    model = CarModel
    extra = 1  # Number of extra empty CarModel forms to display

# Admin customization for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_of_origin', 'founded_year', 'active')  # Customize as needed
    inlines = [CarModelInline]

# Admin customization for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id', 'fuel_type')
    list_filter = ('type', 'fuel_type', 'year', 'car_make')
    search_fields = ('name',)

# Register both models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
