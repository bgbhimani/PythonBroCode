# python file detection

import os
# Relative = folder/test.txt
# Absolute = C:/Users/BroCode/Desktop/test.txt

file_path = ("stuff.pdf")

if os.path.exists(file_path):
    print(f"the location {file_path} exist")

    if os.path.isfile(file_path):
        print(f"that is file")
    elif os.path.isdir(file_path):
        print("that is the Directory")

else:
    print("That location Doesn't exist")

