#Define each menu Coffe, Tea, Sandwich and cake
menu = ["Coffe", "Tea", "Sandwich", "Cake"]
#Define the stock for each item in the menu
stock = {
    "Coffe": 100,
    "Tea": 200,
    "Sandwich": 90,
    "Cake": 20
    }
#Define price for each item in the menu Coffe, Tea, sandwich and cake
price = {
    "Coffe": 2.50,
    "Tea": 2.00,
    "Sandwich": 5.00,
    "Cake": 3.50
}
#calculate total stock worth in the cafe
total_stock_worth = 0
for item in menu:
    item_value = (stock[item] * price[item])
    total_stock_worth = item_value
# print out the result
print("Total stock worth in the cafe: ${: .2f}".format(total_stock_worth))
