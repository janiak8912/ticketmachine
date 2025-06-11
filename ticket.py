class Ticket:
    def __init__(self, name, price, category, group):
        self.name = name
        self.price = price
        self.category = category
        self.group = group

    def __str__(self):
        return f"Bilet {self.category}\t{self.group}\t{self.name}\t{self.price} zł"
