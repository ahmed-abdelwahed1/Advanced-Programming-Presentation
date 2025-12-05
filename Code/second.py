class Car:

    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

def main():
    cars_array = [
        Car("VOLVO", "XC90", 180),  # CAR 1
        Car("TESLA", "MODEL Y", 250), # CAR 2
        Car("LEXUS", "RX", 210),  # CAR 3
        Car("FORD", "RAPTOR", 180),  # CAR 4
        Car("MAZDA", "", 190),  # CAR 5
        Car("AUDI", "A4", 240),  # CAR 6
        Car("SUBARU", "OUTBACK", 200),  # CAR 7
        Car("HYUNDAI", "ELANTRA", 185),  # CAR 8
        Car("PORSCHE", "911", 320)  # CAR 9
        
    ]

    print("--- Car Data from Array (Optimal OOP Display) ---")
    
    for car in cars_array:
        print(f"Brand: {car.brand}, Model: {car.model}, Speed: {car.max_speed} KM/H")

if __name__ == "__main__":
    main()