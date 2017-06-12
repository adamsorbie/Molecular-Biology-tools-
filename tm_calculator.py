from Bio.Seq import Seq  # imports seq from biopython


primerF = Seq(raw_input("Enter forward primer sequence: "))  # takes raw input for forward primer and stores as variable
primerR = Seq(raw_input("Enter reverse primer sequence: "))  # takes raw input for forward primer and stores as variable


no_A_F = primerF.count("A")  # counts A nucleotides in forward primer and stores in variable
no_T_F = primerF.count("T")  # "" T
no_G_F = primerF.count("G")  # "" G
no_C_F = primerF.count("C")  # "" C

no_A_R = primerR.count("A")  # counts A nucleotides in reverse primer and stores in variable
no_T_R = primerR.count("T")  # "" T
no_G_R = primerR.count("G")  # "" G
no_C_R = primerR.count("C")  # "" C
forward_length = len(primerF)  # stores length of forward primer in variable
reverse_length = len(primerR)  # stores length of reverse
print("Forward primer length: " + str(forward_length))  # prints length of forward
print("Reverse primer length: " + str(reverse_length))  # prints length of reverse

if len(primerF) < 14:
    tmF = (no_A_F + no_T_F) * 2 + (no_C_F + no_G_F) * 4
    float_tmF = float(tmF)
    print("Forward primer tm: " + str(float_tmF))
else:
    tmF = 64.9 + 41*(no_C_F + no_G_F - 16.4) / (no_A_F + no_T_F + no_G_F + no_C_F)
    print("Forward primer tm: " + str(tmF))

if len(primerR) < 14:
    tmR = (no_A_R + no_T_R) * 2 + (no_C_R + no_G_R) * 4
    print("Reverse primer tm: " + str(tmR))
else:
    tmR = 64.9 + 41*(no_C_R + no_G_R - 16.4) / (no_A_R + no_T_R + no_G_R + no_C_R)
    print("Reverse primer tm: " + str(tmR))

gc_F = (no_G_F + no_C_F)
gc_content_F = float(gc_F) / forward_length * 100
print("Forward GC content: " + str(gc_content_F) + "%")

gc__R = (no_G_R + no_C_R)
gc_content_R = float(gc__R) / reverse_length * 100
print("Reverse GC content: " + str(gc_content_R) + "%")

list_tm = [tmF, tmR]
high_tm = max(list_tm)
low_tm = min(list_tm)

if high_tm - low_tm >= 5:
    print("Temperature difference is greater than the recommended 5C")
elif tmF < tmR:
    ta_l = tmF - 5
    ta_u = tmF - 3
    print("Annealing temp range:" + str(ta_l) + "-" + str(ta_u) + "C")
elif tmR < tmF:
    ta_l = tmR - 5
    ta_u = tmR - 3
    print("Annealing temp range: " + str(ta_l) + "-" + str(ta_u) + "C")

exit() 
