year = int(input("年を入力"))

if year % 100 == 0 and year % 400 != 0:
    print("False")
elif year % 4 == 0:
    print("True")
else:
    print("False")