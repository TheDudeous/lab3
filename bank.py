class Bank:
    def __init__(self):
        self.cash = 0

    def insert_cash(self, money):
        if money < 0:
            raise ValueError
        else:
            self.cash += money

    def remove_cash(self, money):
        if money > self.cash or money < 0:
            raise ValueError
        else:
            self.cash -= money
    