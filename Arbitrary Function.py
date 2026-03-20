# *args & **kwargs

def shipping_label(*args, **kwargs):
    for agr in args:
        print(agr, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "PO_BOX" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('PO_BOX')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('zip')}")




shipping_label("Dr.", "Spongebob", "Squarepants",
               street = "45 Fake St.",
               apt = "#100",
               PO_BOX = "PO BOX #1001",
               city = "Detroit",
               zip = "12345")