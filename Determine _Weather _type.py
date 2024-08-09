temp = int (input("Enter your temperature  in celcious: "))
humid = int (input("Enter  humidity in percentage: "))

if   temp >=30 and humid >= 90:
        print("hot and humid ")
elif temp>=30 and humid < 90:
        print("hot")
elif temp < 30 and humid >=90:
        print("cold and humid")
else:
        print("cold")