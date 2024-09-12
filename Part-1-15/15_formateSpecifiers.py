# formate specifier = {:flags} Four meter value based on what flag are inserted

#  :(number)f = Round to that many decimal places. (fixed point)
#  :(number)  = Allocate that many species
#  :03 = Allocate and zero pad that many spaces
#  :+ = use a plus sign to indicate positive value
#  := = place sign to leftmost position
#  :- = Left align the number
#  :< = left justify
#  :> = right justify
#  :^ = center justify
#  :  = insert a space before positive numbers
#  :, = comma separator
#  :b = convert to binary
#  :c = convert to character
#  :d = convert to decimal
#  :e = convert to exponential notation
#  :f = convert to fixed point notation
#  :g = convert to fixed point notation if the number contains a decimal point, otherwise use
#  :o = convert to octal
#  :x = convert to hexadecimal
#  :X = convert to uppercase hexadecimal
#  :n = convert to integer
#  :p = convert to percentage
#  :r = convert to float
#  :s = convert to string


p1 = 3.14159
p2 = -987.65
p3 = 12.34

print(f"price 1 is {p1}")
print(f"price 2 is {p2}")
print(f"price 3 is {p3}")

print(f"price 1 is {p1:.2f}") #3.14   #for 2 num after .
print(f"price 2 is {p2:.3f}") #-987.650
print(f"price 3 is {p3:.1f}") #12.3

print(f"price 1 is {p1:10}")
print(f"price 2 is {p2:10}")
print(f"price 3 is {p3:010}")

print(f"price 1 is {p1:<10}")   #left Justified mean number than space
print(f"price 2 is {p2:>10}")
print(f"price 3 is {p3:^10}")   # centre Justified

print(f"price 1 is {p1:+}")  # pluse will be with + sign
print(f"price 2 is {p2:+}")  # negative will be with - sign
print(f"price 3 is {p3: }")  # it will add space for +ve & - for -ve

p1 = 5000.8462
p2 = -86472.254
p3 = 97865.546

print(f"price 1 is {p1:,}") # add the , at thousand
print(f"price 2 is {p2:+,.2f}")
print(f"price 3 is {p3:,}")