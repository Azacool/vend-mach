class VendingMachine:
    def __init__(self):
        self.beverages = {}

    def addBeverage(self, name, price):
        
        if not isinstance(price, (int, float)) or price <= 0:
            print("Mavjud bolmagan narx, iltimos positive raqam kiriting")
            return

        name = name.lower()

        if name in self.beverages:
            print(f"{name.capitalize()} vending machine da bor.")
        else:
            self.beverages[name] = price
            print(f"{name.capitalize()} vending machine ga qoshildi.")

    def getPrice(self, name):
        
        name = name.lower()

        return self.beverages.get(name, -1.0)

vending_machine = VendingMachine()

vending_machine.addBeverage("coca cola", 3200)
vending_machine.addBeverage("suv", 1000)
vending_machine.addBeverage("pepsi", 2500)

beverage_name = "coca cola"
price = vending_machine.getPrice(beverage_name)
if price != -1.0:
    print(f"Ichimlikning nomi {beverage_name} va {price} sum.")
else:
    print(f"{beverage_name} bu ichimlik vending machine da yoq.")

beverage_name = "sprite" 
price = vending_machine.getPrice(beverage_name)
if price != -1.0:
    print(f"Ichimlikning nomi {beverage_name} va {price} sum.")
else:
    print(f"{beverage_name} bu ichimlik vending machine da yoq.")
