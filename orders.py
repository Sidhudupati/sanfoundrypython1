order_numbers=['Order1','Order2','Order3','Order4','Order5']
Order_cost=[300,500,1100,800,700]
order_name=['mouse','keyboard','monitor','router','charger']
items=list(zip(order_numbers,Order_cost))
items.sort(key=lambda x:x[1],reverse=True)
for i in items:
    order_numbers,Order_cost=i
    print("Order Number:",order_numbers)
    print("Order cost:",Order_cost)








