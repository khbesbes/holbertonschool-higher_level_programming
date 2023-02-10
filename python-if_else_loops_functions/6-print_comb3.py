#!/usr/bin/python3
for digt1 in range(9):
    for digt2 in range (digt1 + 1, 10):
        if digt1 == 8 and digt2 == 9:
            print(("{}{}").format(digt1, digt2))
        else:
            print("{}{}".format(digt1, digt2), end=", ")
            