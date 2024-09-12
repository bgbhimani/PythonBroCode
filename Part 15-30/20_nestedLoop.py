# Nested Loop: a loop within another loop (inne : outer)
#   Outer Loop:
#       Inner Loop:

rows = int(input("Enter The rows: "))
cols = int(input("Enter the Columns: "))
symb = input("Enter thr Symbol: ")

for y in range(rows):
    for x in range (cols):
        print(symb, end="")
    print("")
    