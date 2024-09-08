# username < 12 no space no digit

username = input("Enter Your Username: ")
if len(username) < 12 and username.find(" ") and username.isalpha():
    print(f"You're In. {username}")
elif len(username)>12:
    print("Length must < 12")
elif username.find(" ") > 0:
    print("No space allowed")
elif not username.isalpha():
    print("No digit allowed")
else: 
    print("You're OUT.")