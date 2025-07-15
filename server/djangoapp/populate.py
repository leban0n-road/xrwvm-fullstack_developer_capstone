from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "Toyota", "description": "Reliable Japanese brand"},
        {"name": "Ford", "description": "American innovation"},
        {"name": "BMW", "description": "German performance"},
    ]

    car_make_instances = []
    for data in car_make_data:
        make = CarMake.objects.create(name=data['name'], description=data['description'])
        car_make_instances.append(make)

    car_model_data = [
        {"name": "Camry", "type": "SEDAN", "year": 2023, "dealer_id": 1, "car_make": car_make_instances[0]},
        {"name": "Corolla", "type": "SEDAN", "year": 2022, "dealer_id": 1, "car_make": car_make_instances[0]},
        {"name": "F-150", "type": "TRUCK", "year": 2023, "dealer_id": 2, "car_make": car_make_instances[1]},
        {"name": "Mustang", "type": "COUPE", "year": 2023, "dealer_id": 2, "car_make": car_make_instances[1]},
        {"name": "3 Series", "type": "SEDAN", "year": 2023, "dealer_id": 3, "car_make": car_make_instances[2]},
    ]

    for data in car_model_data:
        CarModel.objects.create(**data)
