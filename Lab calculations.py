import sys


def dil_vol_calc(a, b, c):
    v1 = (a * b) / c
    return v1


def no_of_moles(molarity, volume):
    moles = molarity * volume
    return moles


def mass_grams(mass, mw):
    mass = mass * mw
    return mass


options = ["Dilution (1)", "Mass (2)", "Moles (3)"]

print("Available calculations: ")

for x in options:
    print(x)


calc = str(raw_input("Enter number of desired calculation: "))

units = (raw_input("Enter units: "))

list_units = ["l", "ml", "ul", "nl"]

if units not in list_units:
    print("Error")
    sys.exit()

print("Make sure to use the same units in the calculation!")


if calc == "1":
    C1 = float(raw_input("Enter C1: "))
    V2 = float(raw_input("Enter V2: "))
    C2 = float(raw_input("Enter C2: "))
    ans = dil_vol_calc(V2, C2, C1)
    diluent = V2 - ans
    print("%.3f" % ans + str(units) + ", diluent =" + " " + "%.3f" % diluent + units)
    sys.exit()

elif calc == "2":
    m = float(raw_input("Enter concentration in molar: "))
    v = float(raw_input("Enter volume in L: "))
    ans = no_of_moles(m, v)
    print(ans)
    sys.exit()

elif calc == "3":
    no_moles = float(raw_input("Enter number of moles: "))
    molecular_weight = float(raw_input("Enter molecular weight: "))
    ans = mass_grams(no_moles, molecular_weight)
    print(ans)
    sys.exit()

else:
    print("Error")
    sys.exit()
