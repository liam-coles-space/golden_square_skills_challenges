
class Receipt:
    # User facing properties:
    #   None

    def __init__(self):
        pass

    def create(self, entries):
        # Parameters:
        #   entries: dictionary of items(key) and prices(value)
        # Returns:
        #   list of itemised recipt with total
        receipt = []
        if entries != []:
            total = 0
            for entry in entries:
                key, value = entry.popitem()
                receipt.append(f"{key} £{value:.2f}")
                total += value

            receipt.append(f"Total : £{total:.2f}")    
        
        return receipt
        
        
   