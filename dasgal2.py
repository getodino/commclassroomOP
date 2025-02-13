class GroceryStore:
    def __init__(self, name, apple_sold_kg, apple_une, orange_sold_kg, orange_une):
        self.name = name
        self.apple_sold_kg = apple_sold_kg
        self.apple_price = apple_une
        self.orange_sold_kg = orange_sold_kg
        self.orange_price = orange_une

    def calculate_revenue(self):
        apple_revenue = self.apple_sold_kg * self.apple_une
        orange_revenue = self.orange_sold_kg * self.orange_une
        return apple_revenue + orange_revenue


bambaruush = GroceryStore("Bambaruush", 534, 5000, 487, 10000)
jimshen = GroceryStore("Jimshen", 764, 4800, 423, 9300)
fruits = GroceryStore("Fruits", 136, 5000, 228, 10000)


bambaruush_revenue = bambaruush.calculate_revenue()
jimshen_revenue = jimshen.calculate_revenue()
fruits_revenue = fruits.calculate_revenue()


print(f"Bambaruush дэлгүүрийн орлого: {bambaruush_revenue}")
print(f"Jimshen дэлгүүрийн орлого: {jimshen_revenue}")
print(f"Fruits дэлгүүрийн орлого: {fruits_revenue}")


total_revenue = bambaruush_revenue + jimshen_revenue + fruits_revenue
print(f"Нийт дэлгүүрийн орлого: {total_revenue}")
