def party_invoice():
    
    price_dict = {
        "H": 50,
        "S": 40,
        "Y": 35,
        "p": 10,
        "b": 2,
        "s": .5,
        "C": 15,
        "c": .25,
    }
    
    base_price = 100
    
    # input each addon as a string with the quantity and type
    # seperate each addon with a comma
    addons = input("What are the party addons? ")
    print(addons)
    
    # use the "split" method to convert the addons to a list
    addons_list = addons.split(",")
    print(addons_list)
    
    for addon in addons_list:
        
        item = addon[-1]
        count = float(addon[:-1])
        print("item: ", item, "count: ", count)
        
        base_price = base_price + (price_dict.get(item) * count)
        print(base_price)
        
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()

