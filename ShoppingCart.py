class ShoppingCart:
    def __init__(self):
        self.items = []

    def get_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

    def add_item(self, item, price):
        # Exception bei negativem Preis
        if price < 0:
            raise ValueError("Preis muss positiv sein!")
        self.items.append([item, price])

    def get_quantity(self, item):
        count = 0
        for i in self.items:
            if i[0] == item:
                count += 1
        return count

    def remove_item(self, item):
        for i in self.items:
            if i[0] == item:
                self.items.remove(i)
                break