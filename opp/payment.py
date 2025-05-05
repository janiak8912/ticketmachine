import re

class PaymentProcessor:
    def __init__(self, total):
        self.total = total

    def process_payment(self):
        print(f"\nKwota do zapłaty: {self.total} zł")
        method = input("Wybierz metodę płatności: \nb - BLIK \nk - karta \ng - gotówka\n").lower()

        if method == 'b':
            self.blik_payment()
        elif method == 'k':
            self.card_payment()
        elif method == 'g':
            self.cash_payment()
        else:
            retry = input("Niepoprawny wybór. Spróbować ponownie? (t/n): ").lower()
            if retry == 't':
                self.process_payment()
            else:
                exit()

    def blik_payment(self):
        code = input("Podaj kod BLIK: ")
        if re.fullmatch(r'\d{6}', code):
            print("Transakcja powiodła się.")
        else:
            retry = input("Zły kod. Spróbować jeszcze raz? (t/n): ").lower()
            if retry == 't':
                self.blik_payment()
            else:
                exit()

    def card_payment(self):
        print("Proszę zbliżyć kartę...")
        input("Potwierdź transakcję Enterem.")
        print("Transakcja powiodła się.")

    def cash_payment(self):
        paid = 0
        while paid < self.total:
            try:
                paid += float(input(f"Wrzuć gotówkę (brakuje {self.total - paid:.2f} zł): "))
            except ValueError:
                continue
            if paid < self.total:
                retry = input("Za mało. Dopłacić? (t/n): ").lower()
                if retry != 't':
                    exit()
        change = round(paid - self.total, 2)
        print("Transakcja gotówkowa powiodła się.")
        if change > 0:
            print(f"Wydaję resztę: {change:.2f} zł")