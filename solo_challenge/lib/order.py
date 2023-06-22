class Order:
    # User facing properties:
    #   none

    def __init__(self, delivery_time, comms, time, menu, receipt):
        self.delivery_time = delivery_time
        self.comms = comms
        self.time = time
        self.menu = menu
        self.receipt = receipt
        self.order_items = []

    def add_order_item(self, name, quantity):
        # Parameters:
        #   name: string value
        #   quantity: int
        # Side-effects:
        #   adds dish object to order_items list property
        for i in range(quantity):
            if self.menu.find_dish(name) != None:
                self.order_items.append(self.menu.find_dish(name))
            else:
                return False
        

    def remove_order_item(self, name, quantity):
        # Parameters:
        #   name: string value
        #   quantity: int
        # Side-effects:
        #   removes dish object from order_items list propert
        new_list = []
        item_found = 0
        for item in self.order_items:
            if item.name == name and item_found < quantity:
                item_found += 1
            else:
                new_list.append(item)
        
        self.order_items = new_list

        if item_found == 0:   
            return False


    def generate_receipt(self):
        # Returns : string value showing an itemized bill with total
        receipt_list = []
        for item in self.order_items:
            receipt_list.append({item.name: item.price})
        return self.receipt.create(receipt_list)

    def send_confirmation_text(self, phone_number):
        # Parameters:
        #   phone_number: string value
        #   time: int value 
        # Side effects:
        #   Calls comms.send_text_message which sends out text message
        #  
        estimated_delivery_time = self.time.localtime(self.time.time() + self.delivery_time * 60)
        self.comms.send_text_message(phone_number, f"Thank you! Your order was placed and will be delivered before {self.time.strftime('%H:%M' ,estimated_delivery_time)}")

