import sys


def dil_vol_calc(a, b, c):
    x = (a * b) / c
    return x


def moles(m, v):
    n = m * v
    return n


def mass_grams(n, mw):
    mass = n * mw
    return mass


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
    diluent = V2 - ans
    print("%.3f" % ans + str(units) + ", diluent =" + " " + "%.3f" % diluent + units)
    sys.exit()

if "molarity" or "Molarity" or "molar" or "Molar" in calc:
    m = float(raw_input("Enter concentration in molar: "))
    v = float(raw_input("Enter volume in L: "))
    ans = moles(m, v)
    print(ans)
    sys.exit()

if "mass" or "Mass" in calc:
    n = float(raw_input("Enter number of moles: "))
    mw = float(raw_input("Enter molecular weight: "))
    ans = mass_grams(n, mw)
    print(ans)
    sys.exit()

else:
    print("Error")
    sys.exit()
