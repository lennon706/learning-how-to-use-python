weight = int(input("enter weight: "))
if weight >30:
    print("you cant by anymore than 30 kgs")
elif weight == 30:
    print(" the price is $30")
elif weight >= 15:
    print("the price is 25")
elif weight >= 10:
    print("the price is $20: ")
elif weight >= 5:
    print("the price is $15: ")
else:
    print("the price is $10: ")
