import random

print("--Password Generator--")
username= (input("Enter your username:"))
username=username.lower()

passgen=input("""Tell for pass:
              1. Make your own Password
              2. Generate Password
                 choose one:""")
passgen=passgen.lower()

# password= int(input("Enter the lenght of Password you want:"))

upper_alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
lower_alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
symbol=["@","!","#","_","/","(",")","%"]
# password=()

if(passgen=='1' or passgen=="make your own password"):
    password=(input("Enter the password:"))
    if len(password)>16:
        print("Password is too long make it of 16 characters only...")
    elif len(password)<6:
        print("Your written password is too short make it atleast of 6 characters")
    else:
        print("Your password:", password)

elif passgen=="2" or passgen=="generate password":
    length=int(input("Enter the lenght of password you want:"))
    if length<6 or length>16:
        print("Lenght should be between 6 and 16")
    else:
        characters= upper_alphabet + lower_alphabet + symbol
        password=""

        for i in range(length):
            password += random.choice(characters)
        print(f"Generated password is: {password}")

else: 
    print("Something is wrong")
