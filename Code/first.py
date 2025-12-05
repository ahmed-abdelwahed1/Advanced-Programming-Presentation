class Car:
    def __init__(self, brand, model, max_speed):
        self.brand = brand      # STR
        self.model = model      # STR
        self.max_speed = max_speed  # INT
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Max Speed: {self.max_speed} KM/H")


car1 = Car("VOLVO", "XC90", 180)
car2 = Car("TESLA", "MODEL Y", 250)
car3 = Car("LEXUS", "RX", 210)
car4 = Car("FORD", "RAPTOR", 180)
car5 = Car("MAZDA", "", 190)# CAR 5
car6 = Car ("Audi", "A4", 240)# CAR 6
car7 = Car("SUBARU", "OUTBACK", 200) # CAR 7
car8 = Car("HYUNDAI", "ELANTRA", 185)  # CAR 8
car9 = Car("PORSCHE", "911", 320)  # CAR 9

print("CAR1 Details:")
car1.display_info()
print("\nCAR2 Details:")
car2.display_info()
print("\nCAR3 Details:")
car3.display_info()
print("\nCAR4 Details:")
car4.display_info()
print("\nCAR5 Details:")
car5.display_info()
print("\nCAR6 Details:")
car6.display_info()
print("\nCAR7 Details:")
car7.display_info()
print("\nCAR8 Details:")
car8.display_info()
print("\nCAR9 Details:")
car9.display_info()
