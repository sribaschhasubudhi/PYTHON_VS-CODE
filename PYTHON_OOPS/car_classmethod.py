class Car:
    # Standard constructor expects separate attributes
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    # Factory Method 1: Build a car from a hyphenated string
    @classmethod
    def from_string(cls, car_str):
        # Turns "Ford-Mustang-V8" into ["Ford", "Mustang", "V8"]
        brand, model, engine = car_str.split("-")
        return cls(brand, model, engine)  # Creates and returns a new Car object

    # Factory Method 2: Build a car from a Python Dictionary (e.g. from a Web API)
    @classmethod
    def from_dict(cls, car_dict):
        return cls(
            brand=car_dict["brand_name"],
            model=car_dict["model_name"],
            engine=car_dict["fuel_type"]
        )
car1 = Car("Honda", "Civic", "Petrol")
# To print individual attributes:
print(car1.brand)   # Output: Honda
print(car1.model)   # Output: Civic
print(car1.engine)  # Output: Petrol

# OR to print the object itself (if you have __str__ defined):
print(car1)
raw_data = "Ford-Mustang-V8"
car2 = Car.from_string(raw_data)

print(car2.brand)   # Output: Ford
print(car2.engine)  # Output: V8