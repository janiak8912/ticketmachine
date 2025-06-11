class Cart:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def total_price(self):
        return sum(ticket.price for ticket in self.tickets)

    def display(self):
        print("\nTwoje bilety:")
        for index, ticket in enumerate(self.tickets):
            print(f"{index+1}.\t{ticket}")
        print(f"Wartość koszyka:\t{sum(ticket.price for ticket in self.tickets)} zł\n")