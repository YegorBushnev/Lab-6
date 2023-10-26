"""


"""
def encode(password):
    password_list = []
    encoded_list = []
    for i in password:
        password_list.append(int(i))
    for i in range(0, len(password_list)):
        if 0 <= password_list[i] <= 6:
            encoded_list.append(str(password_list[i] + 3))
        elif 7 <= password_list[i]:
            encode_var = (password_list[i] + 3) - 10
            encoded_list.append(str(encode_var))
    encode_string = ''.join(encoded_list)
    return encode_string

def main():
    Program = True
    while Program == True:
        print("""Menu 
    -------------
    1. Encode
    2. Decode
    3. Quit""")
        print()
        menu_choice = int(input("Please enter an option: "))

        if menu_choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        elif menu_choice == 2:
            pass

        elif menu_choice == 3:
            break

if __name__ == "__main__":
    main()



