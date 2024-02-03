
months = {
    1:"Winter",
    2:"Winter",
    3:"Spring",
    4:"Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn or Fall",
    10: "Autumn or Fall",
    11: "Autumn or Fall",
    12: "Winter"
    }
result = int(input("Number of months you want:"))
if result in months:
    print("Your season is",months[result])
else:
    print("Error")
