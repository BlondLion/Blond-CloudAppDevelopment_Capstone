from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    maker_name = models.CharField(null=False, max_length=30, default="Car Name")
    description = models.CharField(null=False, max_length=200, default="Car Description")

    def __str__(self):
        return  "Name: " + self.maker_name



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = "sedan"
    SUV = "suv"
    WAGON = "wagon"
    MODEL_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "Suv"),
        (WAGON, "Wagon")
    ]
    carMake = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    model_name = models.CharField(null=False, max_length=30, default="Model Name")
    model_type = models.CharField(null=False, max_length=30, choices=MODEL_CHOICES, default=SEDAN)
    year = models.DateField()

    def __str__(self):
        return  "Model Name: " + self.model_name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, state, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state 
        self.state = state
        # Dealer state short
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
