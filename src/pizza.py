class Pizza:
    def __init__(self, customers, ingredients):
        self.customers = customers
        self.ingredients = ingredients
        self.solution = set()
        self.score = 0