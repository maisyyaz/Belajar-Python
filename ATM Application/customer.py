from atm_card import ATMCard


class Customer:
    def __init__(self, id, cust_pin=1234, cust_balance=10000):
        self.id = id
        self.cust_pin = cust_pin
        self.cust_balance = cust_balance

    def cekId(self):
        return self.id

    def cekPin(self):
        return self.cust_pin

    def cekSaldo(self):
        return self.cust_balance

    def debet(self, nominal):
        self.cust_balance -= nominal

    def deposit(self, nominal):
        self.cust_balance += nominal
