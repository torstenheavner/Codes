from re import *

string = input("Paste line to convert:\n")

stringout = sub(r"RD", "R'", string)
stringout = sub(r"RU", "R", stringout)
stringout = sub(r"UL", "U'", stringout)
stringout = sub(r"UR", "U", stringout)
stringout = sub(r"FR", "F'", stringout)
stringout = sub(r"FU", "F", stringout)
stringout = sub(r"LD", "L'", stringout)
stringout = sub(r"LU", "L", stringout)
stringout = sub(r"BR", "D'", stringout)
stringout = sub(r"BL", "D", stringout)

print("==========================================")
print(stringout)
print("==========================================")
