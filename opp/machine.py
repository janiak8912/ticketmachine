import re
import json
import cart
import ticket

class Ticket_machine:
    def __init__(self):
        self.cart = cart.Cart()
        with open("prices.json", "r", encoding="UTF-8") as jf:
            self.prices = json.load(jf)
    def choose_ticket(self) -> ticket.Ticket:
        menu = self.prices
        new_ticket = ticket.Ticket()
        print("Jaki rodzaj biletu chcesz kupić? ")
        options = list(menu.keys())
        for index, option in enumerate(options):
            print(f"{index} - {option}")
        try:
            choice = int(input("Wybór: "))
        except ValueError:
            print("Wprowadzono niepoprawny typ wartości.")
            return self.choose_ticket(menu)
        if choice > len(options)-1 or choice < 0:
            print("Wprowadzono błędny numer opcji.")
            return self.choose_ticket(menu)
        menu = menu[options[choice]]
        if isinstance(menu, dict):
            return self.choose_ticket(menu)
        else: 
            return (options[choice], menu)

# tu rozpoczyna się rzeczywoste działanie programu 
add_another = 't'
while add_another.lower()=='t':
    cart.append(display_menu(prices))
    add_another = input("Czy chcesz dodać kolejny bilet (t/n)? ")
register_payment(cart)
input("Drukowanie biletów. Proszę czekać...")
display_cart(cart)
print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie")

