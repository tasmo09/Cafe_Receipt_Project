class Order:
    def __init__(self):
        self.items = []

    def add_items(self, drink):
        self.items.append(drink)

    def calculate_total(self):
        total = 0
        for drink in self.items:
            total += drink.calculate_price()
        return round(total, 2)

    def display_receipt(self):
        if not self.items:
            return "No items in the order."
        receipt =  ["\n========== TAS CAFE RECEIPT =========="]
        for drink in self.items:
            receipt.append(drink.describe() + "\n")

        receipt.append("========================================")
        receipt.append(f"Total: ${self.calculate_total():.2f}")
        receipt.append("========================================")
        return "\n".join(receipt)
