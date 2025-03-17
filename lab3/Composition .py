class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def __repr__(self):
        return f"Engine({self.fuel_type}, {self.horsepower} HP)"


class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    def __repr__(self):
        return f"Car({self.brand}, {self.model}, {self.engine})"


engine = Engine("Petrol", 150)

car = Car("Toyota", "Camry", engine)

print(car)
# Output: Car(Toyota, Camry, Engine(Petrol, 150 HP))
