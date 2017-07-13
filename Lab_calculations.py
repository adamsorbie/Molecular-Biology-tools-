import sys
def dil_vol_calc(a,b,c):
    x = (a * b) / c
    return x

calc = str(raw_input("Enter calculation type: "))
units = (raw_input("Enter units: "))
list_units = ["l", "ml", "ul", "nl"]
if units not in list_units:
    print("Error")
    sys.exit()

print("Make sure to use the same units in the calculation!")

if "dilution" or "dilution " or "dilutions" or "Dilution" in calc:
    C1 = float(raw_input("Enter C1: "))
    V2 = float(raw_input("Enter V2: "))
    C2 = float(raw_input("Enter C2: "))
    ans = dil_vol_calc(V2, C2, C1)
    print(str(ans) + str(units) + ", diluent =" + " " + str(V2 - ans) + str(units))

else:
    print("Error")
    sys.exit()
