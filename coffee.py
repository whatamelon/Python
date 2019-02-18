#coffee.py
coffee=10
while True:
    money = int(input("put your money:"))
    if money ==300:
        print("this is your coffee")
        coffee==coffee-1
    elif money>300:
        print("change %d and its coffee"%(money-300))
        coffee=coffee-1
    else:
        print("take your money back")
        print("now coffee %d"%coffee)
    if not coffee:
        print("nothing")
        break
    