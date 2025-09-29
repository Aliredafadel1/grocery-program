groceries={"apple":2,"banana":1,"milk":3,"bread":2}
cart={}
while True:
    item=input("what do you want to buy ?").lower
    if item=="done":
        break
    parts = item.split()
    product = parts[0]
    quantity =int(part[1]) if len(parts) >1 else 1
if product in groceries :
    cart[product] = cart.get(product,0)+ quantity
else:
    print("sorry,we dont have that item.")