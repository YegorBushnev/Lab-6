"""
Lab 5
Authors: Yegor Bushnev and Dustin Nguyen
Class: COP3502C
Section: 22282
Description: Password encoder and decoder program that allows a user to go between encoding and
decoding a password.
"""

def encode(password):
    """This function takes in a 8-digit password in string format containing only integers. The
    function first converts every digit in the string into an integer and then increments each digit
    by 3. The final string is the encoded password."""
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
    """This function takes in the user's encoded password in string format containing only integers. Then
    a for loop goes through each character, changes it with the corresponding value in the library or subtracts 3,
    and adds it to a new string."""

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
    """This is the function for the main program."""
    Program = True
    encoded_password = ''
    #Create a while loop for the menu.
    while Program == True:
        print("""Menu 
-------------
1. Encode
2. Decode
3. Quit""")
        print()
        print()
        #Allow user to input a menu choice
        menu_choice = int(input("Please enter an option: "))

        #Ecodes the password that the user inputs using the encode function.
        if menu_choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
            print()

        #Decodes the encoded password of the user using the decode function
        #Returns the original password
        elif menu_choice == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()
            print()

        #Quits the program
        elif menu_choice == 3:
            break

if __name__ == "__main__":
    main()



