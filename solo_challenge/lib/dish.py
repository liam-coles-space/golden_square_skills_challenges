
class Dish:
    # User facing properties:
    #   name : string value
    #   price: int value

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def format(self):
        # returns:
        #   string value
        print(self.price)
        return f"{self.name} : £{self.price:.2f}"