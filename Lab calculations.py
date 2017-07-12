def dil_vol__calc(a,b,c):
    x = (a * b) / c
    return x
d
calc = str(raw_input("Enter calculation type: "))

if calc == "dilution":
    C1 = float(raw_input("Enter C1: "))
    V2 = float(raw_input("Enter V2: "))
    C2 = float(raw_input("Enter C2: "))
    ans = dil_vol__calc(V2, C2, C1)
    print(ans, "ul", V2 - ans, "ul")

