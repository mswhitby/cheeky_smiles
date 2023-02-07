def party_invoice():
    
    base_price = 100
    
    # input each addon as a string with the quantity and type
    # seperate each addon with a comma
    addons = input("What are the party addons? ")

    # use the "split" method to convert the addons to a list
    addons_list = addons.split(",")
    print("addons_list ", addons_list)
    
    for addon in addons_list:
        
        item = addon[-1]
        count = addon[:-1]
        print("item: ", item, "count: ", count)
        
        if item == "H":
            base_price = base_price + (50 * count)
            
        if item == "S":
            base_price = base_price + (40 * count)
            
        if item == "Y":
            base_price = base_price + (35 * count)
            
        if item == "p":
            base_price = base_price + (10 * count)
            
        if item == "M":
            base_price = base_price + (3.75 * count) 
    
    
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()
