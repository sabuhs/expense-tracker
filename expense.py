class Expense:
    def __init__(self, name, category, amount, payer) -> None:
        self.name = name
        self.amount = amount
        self.category = category
        self.payer = payer

    def __repr__(self):
        return f"<Expense: {self.name}, £{self.amount:.2f}, {self.category}, {self.payer}>"
