import json
from ticket import Ticket
from cart import Cart
from payment import PaymentProcessor

class TicketSelector:
    def __init__(self, price_file):
        with open(price_file, "r", encoding="utf-8") as f:
            self.prices = json.load(f)

    def display_menu(self, menu=None, path=None):
        if menu is None:
            menu = self.prices
            path = []

        options = list(menu.keys())
        print("\nWybierz opcję:")
        for i, option in enumerate(options):
            print(f"{i} - {option}")

        try:
            choice = int(input("Wybór: "))
            if choice < 0 or choice >= len(options):
                raise ValueError
        except ValueError:
            print("Nieprawidłowy wybór.")
            return self.display_menu(menu, path)

        selected_key = options[choice]
        selected_value = menu[selected_key]
        path.append(selected_key)

        if isinstance(selected_value, dict):
            return self.display_menu(selected_value, path)
        else:
            return Ticket(path[0], path[1], path[2], selected_value)

def main():
    selector = TicketSelector("prices.json")
    cart = Cart()

    while True:
        ticket = selector.display_menu()
        cart.add_ticket(ticket)
        cont = input("Dodać kolejny bilet? (t/n): ").lower()
        if cont != 't':
            break

    if cart.is_empty():
        print("Koszyk jest pusty.")
        return

    cart.display_cart()

    confirm = input("\nCzy chcesz przejść do płatności? (t/n): ").lower()
    if confirm == 't':
        processor = PaymentProcessor(cart.total())
        processor.process_payment()

        input("\nDrukowanie biletów...")
        cart.display_cart()
        print("Dziękujemy za zakup!")
    else:
        print("Zakup anulowany.")

if __name__ == "__main__":
    main()