print("Welcome to 'Viva La Vida' Restuarant, What would you like to order: ")
print(f"Our Menu: \n1. Oreo Shake : 50rs.\n2. Kitkat Shake : 60rs.\n3. Pizza : 90rs.\n4. Burger : 65rs.\n5.Patty : 25rs.\n6. Sandwich : 40rs.\n")

menu ={
    "oreo shake" : 50 ,
    "kitkat shake" : 60,
    "pizza" : 90 ,
    "burger" : 65 ,
    "patty" : 25 ,
    "sandwich" : 40,
}

bill =0

flag = True
i =1
while(flag):
    a = input(f"enter {i} item => ")
   
    item = a.lower()
    if(item not in menu):
        if(item == 'NO' or item == "no" or item == "No"):
            flag= False
        else:
            print("Sorry! That is not in our menu")
    else:
        bill+= menu[item]
        print("Order Added ! \n also wish to type 'no' when order completed!")
    i+=1
    
print(f"Here is your total bill to be paid : {bill} rs. ")
print("Thank You For Coming, See you Soon , again!")




