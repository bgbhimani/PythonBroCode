#  indexing : Accessing elements of a sequence using [] (indexing operator 
# [Start : end : step]

number = "1234-5678-9012-3456"

print(number[0:4])     # 1234
print(number[:8])      # Starts with 0
print(number[5:])      # ends with last


print(number[-2])      # second last from
print(number[::2])     # 13-6891-46
print(number[::3])     # 146-136

last_num = number[-4::1]
print(last_num)        # 3456

# reverse the String 
number = number[::-1]
print(number)    #6543-2109-8765-4321
