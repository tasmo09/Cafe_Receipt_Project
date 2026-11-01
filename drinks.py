
class Drink:
    

    def __init__(self, name, base_price, size="Small", milk="Whole", temperature="Hot"):
        
        self.name = name
        self.base_price = base_price
        self.size = size
        self.milk = milk
        self.temperature = temperature

    def calculate_price(self):
        
        price = self.base_price

        if self.size == "Medium":
            price += 0.25
        elif self.size == "Large":
            price += 0.50

        return round(price, 2)

    def describe(self):

        size_letter = {
            "Small": "S",
            "Medium": "M",
            "Large": "L"
        }

        return (
            f"{self.name} | {size_letter[self.size]} | "
            f"{self.milk} milk | {self.temperature} | "
            f"${self.calculate_price():.2f}"
        )


class Coffee(Drink):
    category = "Coffee"


class Matcha(Drink):
    category = "Matcha"


MENU = {
    "Iced Vanilla Latte": 5.50,
    "Caramel Macchiato": 5.50,
    "Matcha Latte": 5.25,
    "Strawberry Matcha Latte": 5.50,
}


def create_drink(name, size, milk, temperature):
    
    if name not in MENU:
        raise ValueError(f"{name} is not on the menu.")

    price = MENU[name]

    if "Matcha" in name:
        return Matcha(name, price, size, milk, temperature)

    return Coffee(name, price, size, milk, temperature)


