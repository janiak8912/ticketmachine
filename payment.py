import re
import datetime
import os

class Payment_method:
    def __init__(self, amount, cart):
        self.amount = amount
        self.cart = cart

    def process(self):
        print(f"Kwota do zapłaty - {self.amount} zł")
        method = input("Wybierz metodę płatności: \nb - BLIK\nk - karta\ng - gotówka\n")

        if method.lower() == "b":
            return self._blik()
        elif method.lower() == "k":
            return self._card()
        elif method.lower() == "g":
            return self._cash()
        else:
            retry = input("Niepoprawna opcja. Spróbować ponownie (t/n)? ")
            return self.process() if retry.lower() == "t" else False


    def _blik(self):
        code = input("Podaj kod BLIK: ")
        if re.fullmatch(r"\d{6}", code):
            print("Transakcja się powiodła.")
            self.log_transaction("BLIK")
            return True
        else:
            retry= input("Niepoprawny kod. Spróbować ponownie (t/n)? ")
            return self._blik() if retry.lower() == "t" else False

    def _card(self):
        print("Proszę zbliżyć kartę...")
        input("Potwierdź transakcję: ")
        print("Transakcja się powiodła.")
        self.log_transaction("Karta")
        return True

    def _cash(self):
        paid = 0
        while paid < self.amount:
            try:
                paid += float(input("Wprowadź gotówkę: "))
            except ValueError:
                print("Niepoprawna kwota.")
                continue

            if paid < self.amount:
                retry = input("Za mało gotówki. Dopłacić? (t/n) ")
                if retry.lower() != "t":
                    print("Transakcja anulowana.")
                    return False

        if paid > self.amount:
            print(f"Reszta: {round(paid - self.amount, 2)} zł")
        print("Transakcja się powiodła.")
        self.log_transaction("Gotówka")
        return True
    


    def log_transaction(self, method_name):
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        with open(os.path.join(log_dir, "transactions.log"), "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} | Metoda: {method_name} | Kwota: {self.amount} zł\n")
            for ticket in self.cart.tickets:
                f.write(f"  - {ticket}\n")

            f.write("\n")
