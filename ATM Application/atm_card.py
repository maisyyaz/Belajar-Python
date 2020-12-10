class ATMCard:
    def __init__(self, defaultPin, defaultBalace):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalace

    def cekPinAwal(self):
        return self.defaultPin

    def cekSaldoAwal(self):
        return self.defaultBalance
