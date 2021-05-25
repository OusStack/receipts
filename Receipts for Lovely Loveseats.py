# Adding the Catalog
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

# variable that calculate sales tax
sales_tax = .088

# a variable running tally of customer expenses
customer_one_total = 254.00

# adding the price to the total price
customer_one_total += luxurious_lamp_price

# a variable that keeps a list of the descriptions of things they’re purchasing
customer_one_itemization = "lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# adding new item to the list
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items: " + customer_one_itemization + "\n")
print("Customer One Total: ", customer_one_total)
