year = int(input("Enter the year:"))
if year < 1900 or year >= 1000000:
    print("the year does not meet the conditions")
elif year % 4 == 0 and year % 400 == 0:
    print(year, "is leep year")
else:
    print(year, "is not leep year")