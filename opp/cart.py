class Cart:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def display_cart(self):
        print("\n--- Twój koszyk ---")
        for ticket in self.tickets:
            print(ticket)

    def total(self):
        return sum(ticket.get_price() for ticket in self.tickets)

    def is_empty(self):
        return not self.tickets