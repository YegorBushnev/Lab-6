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

def decode(password):
    decode_string = ''
    for i in password:
        if i == '0' or i == '1' or i == '2':
            special_case = {
                '0':'7', '1':'8', '2':'9'
            }
            decode_string += special_case[i]
        else:
            decode_string += str(int(i) - 3)


    return decode_string

def main():
    Program = True
    encoded_password = ''
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

            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            pass

        elif menu_choice == 3:
            break

if __name__ == "__main__":
    main()



