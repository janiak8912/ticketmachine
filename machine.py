from cart import Cart
from payment import Payment_method
from ticket import Ticket
import json

class TicketMachine:
    def __init__(self, prices_file):
        with open(prices_file, "r", encoding="UTF-8") as file:
            self.menu = json.load(file)
        self.cart = Cart()

    def run(self):
        print("Witamy w automacie biletowym.")
        while True:
            self.cart = Cart()
            self._add_tickets()

            print("\nPodsumowanie przed płatnością:")
            self.cart.display()


            total = self.cart.total_price()
            payment_success = Payment_method(total, self.cart).process()

            if payment_success:
                input("Drukowanie biletów. Proszę czekać...")
                print("Dziękujemy za skorzystanie z automatu biletowego!")
                cont = input("Czy chcesz kontynuować? (t\n): ")
                if cont.lower() !="t":
                    print("Daswidania kamrat")
                   
            else:
                print("\nAnulowano płatność.\n")

    def _add_tickets(self):
        add_more = "t"
        while add_more.lower() == "t":
            name, price, category, group = self._choose_ticket(self.menu)
            self.cart.add_ticket(Ticket(name, price, category, group))
            add_more = input("Czy chcesz dodać kolejny bilet (t/n)? ")

    def _choose_ticket(self, menu, category=None, group=None):
        print("Jaką opcję biletu chcesz kupić?")
        options = list(menu.keys())
        for i, option in enumerate(options):
            print(f"{i} - {option}")
        try:
            choice = int(input("Wybór: "))
        except ValueError:
            print("Niepoprawna wartość.")
            return self._choose_ticket(menu, category, group)
        if choice < 0 or choice >= len(options):
            print("Niepoprawny numer.")
            return self._choose_ticket(menu, category, group)

        selected_key = options[choice]
        selected_value = menu[selected_key]

        if isinstance(selected_value, dict):
            if category is None:
                return self._choose_ticket(selected_value, category=selected_key, group=group)
            else:
                return self._choose_ticket(selected_value, category=category, group=selected_key)

        return selected_key, selected_value, category, group