#Continous Looping until break is executed
i=0
while True:
    try:
        number = int(input("Hey! go ahead and enter a number"))
        print(3/number)
        break
    except ValueError:
        print("Yeah, thats not a number. Try Again !")
    except ZeroDivisionError:
        print("Division by 0 is not supported")
    #Execute no matter what
    finally:
        i += 1
        print("executed ",i," times")


