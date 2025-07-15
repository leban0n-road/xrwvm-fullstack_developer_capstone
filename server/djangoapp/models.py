# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
from django.db import models

class CarMake(models.Model):
    """
    Represents a car manufacturer or brand.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Make Name",
        help_text="Enter the name of the car make (e.g., Toyota, Ford)"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Make Description",
        help_text="Optional: A short description of the car make."
    )

    country_of_origin = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Country of Origin",
        help_text="Optional: Country where the car make originates (e.g., Japan, Germany)."
    )

    founded_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Year Founded",
        help_text="Optional: Year the car make was founded."
    )

    active = models.BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text="Check if the manufacturer is currently active."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Updated"
    )

    class Meta:
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.country_of_origin})" if self.country_of_origin else self.name



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class CarModel(models.Model):
    """
    Represents a specific model of a car, associated with a CarMake.
    """
    # Many-to-One relationship: One CarMake can have many CarModels
    car_make = models.ForeignKey(
        'CarMake',
        on_delete=models.CASCADE,
        related_name='car_models',
        verbose_name="Car Make",
        help_text="The manufacturer this model belongs to."
    )

    name = models.CharField(
        max_length=100,
        verbose_name="Model Name",
        help_text="The name of the car model (e.g., Corolla, Pathfinder)."
    )

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
        ('OTHER', 'Other'),
    ]

    type = models.CharField(
        max_length=15,
        choices=CAR_TYPES,
        default='SEDAN',
        verbose_name="Body Type",
        help_text="Type of car model (e.g., SUV, Sedan, Wagon)."
    )

    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(date.today().year + 1)  # Allow next year's models
        ],
        verbose_name="Model Year",
        help_text="Year the model was manufactured."
    )

    dealer_id = models.PositiveIntegerField(
        verbose_name="Dealer ID",
        help_text="ID of the dealer from the external database (Cloudant)."
    )

    fuel_type = models.CharField(
        max_length=20,
        blank=True,
        choices=[('GAS', 'Gasoline'), ('DIESEL', 'Diesel'), ('HYBRID', 'Hybrid'), ('EV', 'Electric')],
        default='GAS',
        verbose_name="Fuel Type",
        help_text="Fuel type used by the car model."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Updated"
    )

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"
        ordering = ['car_make__name', 'name']

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

