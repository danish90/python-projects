#Level 1 - Multiply Dictionary Items

# grocery_list = {
#     "apples": 5,
#     "bananas": 2,
#     "milk": 1,
#     "bread": 1
# }
#
# print(f"Current grocery list and quantities: ", grocery_list)
#
# multiplier = int(input("How would you like to modify the quantity of the grocery basket: "))
#
# new_grocery_list = {key: value * multiplier for key, value in grocery_list.items()}
#
# print(f"Your updated grocery list and quantities are: ", new_grocery_list)

#Level 2 - Supermarket Billing System

class SupermarketBilling:

    def __init__(self):
        #initialise an empty list to store all purchased items
        self.items = [] #list of dictionaries with item details, to be added later

    def add_item(self, name: str, price: float, quantity: int):
        item = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        self.items.append(item)
        print(f"Added {quantity} x {name} at ${price:.2f} each (Total: ${item['total']:.2f})")

    def calculate_total(self) -> float:
        return sum(item['total'] for item in self.items)

    def apply_discounts(self) -> float:
        total = self.calculate_total()
        discount = 0
        if total >= 100:
            discount_rate = 10 / 100
            discount = total * discount_rate
            print(f"{discount_rate:.2%} discount:   ${discount:.2f}")
        return discount

    def print_receipt(self):
        print("\n------------SUPERMARKET BILL------------")
        print(f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total'}")
        print("-" * 40)
        for item in self.items:
            print(f"{item['name']:<15}{item['quantity']:<5}${item['price']:<10.2f}${item['total']:.2f}")

        print("-" * 40)
        subtotal = self.calculate_total()
        discount = self.apply_discounts()
        sales_tax_rate = 7.8 / 100
        sales_tax = (subtotal - discount) * sales_tax_rate
        total = subtotal - discount + sales_tax
        print(f"\nSubtotal:          ${subtotal:.2f}")
        print(f"Discount:         -${discount:.2f}")
        print(f"Sales tax ({sales_tax_rate:.2%}): ${sales_tax:.2f}")
        print(f"Total:             ${total:.2f}")
        print("-" * 40)
        print("\nThank you for shopping with us!")

bill = SupermarketBilling()

while True:
    name = str(input("Enter item name (or 'done' to finish): "))
    if name.lower() == "done":
        break
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))
    bill.add_item(name, price, quantity)

bill.print_receipt()