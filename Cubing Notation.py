from re import *

string = input("Paste line to convert:\n")

stringout = string
stringout = sub(r"R'", "RD", string)
stringout = sub(r"R(?!D)", "RU", stringout)
stringout = sub(r"U'", "UL", stringout)
stringout = sub(r" U(?!L)", " UR", stringout)
stringout = sub(r"F'", "FL", stringout)
stringout = sub(r"F(?!L)", "FR", stringout)
stringout = sub(r"L'", "LD", stringout)
stringout = sub(r" L(?!D)", "LU", stringout)
stringout = sub(r"D'", "BR", stringout)
stringout = sub(r" D", " BL", stringout)

print("==========================================")
print(stringout)
print("==========================================")
