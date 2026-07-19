coupons = [
    {"code": "SAVE10", "type": "percent", "value": 10, "min": 0},
    {"code": "FLAT150", "type": "flat", "value": 150, "min": 800},
    {"code": "SAVE20", "type": "percent", "value": 20, "min": 3000},
    {"code": "FLAT500", "type": "flat", "value": 500, "min": 5000}
]

while True:

    total = float(input("Enter Cart Total: "))

    best_coupon = ""
    best_discount = 0

    for coupon in coupons:

        if total >= coupon["min"]:

            if coupon["type"] == "percent":
                discount = total * coupon["value"] / 100
            else:
                discount = coupon["value"]

            if discount > best_discount:
                best_discount = discount
                best_coupon = coupon["code"]

    print("Best Coupon:", best_coupon)
    print("Discount: ₹", best_discount)
    print("Amount to Pay: ₹", total - best_discount)

    again = input("Again? (y/n): ")

    if again.lower() == "n":
        break