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
      if product in cart:
         cart[item] += quantity
      else:
         cart[item] = quantity
    else:
      print("sorry,we dont have that item.")
    total= 0
    for item ,qty in cart.items():
       price=groceries[item]
       if item =="milk" and qty > 2:
          price -= 1
       total += price *qty
    print(" your cart",cart)
    print(f"Total =${total}")
    if total >10:
       print("you spent a lot")
    else:
       print("you spent a little!")