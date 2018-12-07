shopping = []
cos = []
how_many = input("How many item would you like to store ?: ")
how_many =int(how_many)
cost_sum=0
for item_number in range(how_many):
  item = input("Item " + str(item_number+1) + ":") # +1 to be logic for user
  cost = input("Which cost ?: ")
  cost = float(cost)
  shopping.append(item)
  cos.append(cost)
  cost_sum=cost_sum+cost
print("")
print("The list is:")
for item_number in range(how_many):
  print(shopping[item_number])
print("")
print("There is currently "+str(how_many)+" items in the list")
print("")
print("You pay "+str(cost_sum)+" euros for this shopping session.")
nb_pay = input("How many personne will pay for it?")
nb_pay=int(nb_pay)
share = cost_sum/nb_pay
print("Each personne will pay "+str(share)+" euros")
