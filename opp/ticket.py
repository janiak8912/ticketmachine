class Ticket:
    def __init__(self, category, type_, name, price):
        self.category = category
        self.type = type_
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.category} > {self.type} > {self.name} ({self.price} zł)"

    def get_price(self):
        return self.price

    def get_label(self):
        return f"{self.category} - {self.type} - {self.name}"