class PriceProduct:
    def __init__(self, price_list):
        self.price_list = price_list

    def __add__(self, other):
        return PriceProduct([x + y for x, y in zip(self.price_list, other.price_list)])

    def __sub__(self, other):
        return PriceProduct([x - y for x, y in zip(self.price_list, other.price_list)])

    def __mul__(self, other):
        return PriceProduct([x * other for x in self.price_list])

    def __truediv__(self, other):
        return PriceProduct([x / other for x in self.price_list])

    def __lt__(self, other):
        return sum(x < y for x, y in zip(self.price_list, other.price_list)) > (len(self.price_list) / 2)

    def average_price(self):
        return sum(self.price_list) / len(self.price_list)

    def __str__(self):
        return f"Prices: {self.price_list}"


# قیمت کالاهای دو فروشگاه
product_price_list1 = [5000, 10000, 15000, 6000, 25000, 12000, 14000, 10000, 7000, 20000]
product_price_list2 = [4000, 12000, 16000, 5000, 22000, 10000, 16000, 11000, 5000, 18000]

# ایجاد نمونه‌های کلاس
store1 = PriceProduct(product_price_list1)
store2 = PriceProduct(product_price_list2)

# محاسبه میانگین قیمت‌ها
average_prices = (store1 + store2) / 2
print("Average Prices:", average_prices)

# محاسبه میانگین قیمت‌ها با تخفیف 20 درصد
discounted_prices = average_prices * 0.8
print("Discounted Average Prices:", discounted_prices)

# مقایسه قیمت‌های دو فروشگاه
cheaper_store = "Store 1" if store1 < store2 else "Store 2"
print(f"Cheaper Store: {cheaper_store}")

