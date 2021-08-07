from products import allProducts
from tax_rate import taxes


# Item wise tax calculation...

def taxCalculator (product):
    taxOnProduct = 0
    totalPrice = 0
    if product["salesTaxExempted"] and product["isImported"]:
        taxOnProduct = round(product["price"] * taxes["importDuty"], 2)
        totalPrice = round(product["price"] + taxOnProduct, 2)
    elif product["salesTaxExempted"] and not product["isImported"]:
        taxOnProduct = round(product["price"] * 0.0, 2)
        totalPrice = round(product["price"] + taxOnProduct, 2)
    elif not product["salesTaxExempted"] and not product["isImported"]:
        taxOnProduct = round(product["price"] * taxes["salesTax"], 2)
        totalPrice = round(product["price"] + taxOnProduct, 2)
    else:
        taxOnProduct = round(product["price"] * (taxes["salesTax"] + taxes["importDuty"]), 2)
        totalPrice = round(product["price"] + taxOnProduct, 2)
    
    return taxOnProduct, totalPrice

# Function for creating receipt
def create_receipt(IDs):    
    items = []
    totalTax = 0
    grandTotal = 0
    for product_id in IDs.id:
        for product in allProducts["items"]:
            if product_id == product["itemCode"]:
                # calling tax calculation function on each item in the request          
                salesTax, totalPrice = taxCalculator(product) 
                # creating object object for product after tax calculation
                itm = {                    
                    "itemName": product["itemName"],
                    "price": product["price"],
                    "quantity": product["quantity"],
                    "taxOnProduct": salesTax,
                    "totalPrice": totalPrice
                }
                # appending product object into array of items after tax calculation
                items.append(itm)
                # adding item wise tax to total tax on invoice
                totalTax+=salesTax
                # adding item wise price including tax for total amount of invoice
                grandTotal+=totalPrice
                # print(product)

    result = {"items": items, "salesTaxTotal": float(totalTax), "grandTotal": float(grandTotal)}

    return result