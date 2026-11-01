import json
from pathlib import Path

ORDER_FILE = Path("data/orders.json")
RECEIPT_FILE = Path("receipts")

def save_order(order):
    ORDER_FILE.parent.mkdir(parents=True, exist_ok=True)

    try:
        if ORDER_FILE.exists():
            with ORDER_FILE.open("r") as f:
                orders = json.load(f)
        else:
            orders = []
    except (json.JSONDecodeError, OSError):
        orders = []

    order_data = []

    for drink in order.items:
        order_data.append({
            "name": drink.name,
            "size": drink.size,
            "milk": drink.milk,
            "temperature": drink.temperature,
            "price": drink.calculate_price()
        })

    orders.append({
        "items": order_data,
        "total": order.calculate_total()
        })

    with ORDER_FILE.open("w") as f:
        json.dump(orders, f, indent=4)

def save_receipt(order):
    RECEIPT_FILE.mkdir(exist_ok=True)

    receipt_number = len(list(RECEIPT_FILE.glob("receipt_*.json"))) + 1
    receipt_path = RECEIPT_FILE / f"receipt_{receipt_number}.json"

    with receipt_path.open("w") as f:
        f.write(order.display_receipt())

    return receipt_path

def load_order_history():
    try:
        with ORDER_FILE.open("r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Order history could not be found")
        return []

    except OSError:
        print("Order history could not be accessed")
        return []
    