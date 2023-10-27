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

def main():
    """This is the function for the main program."""
    Program = True
    #Create a while loop for the menu.
    while Program == True:
        print("""Menu 
    -------------
    1. Encode
    2. Decode
    3. Quit""")
        print()
        #Allow user to input a menu choice
        menu_choice = int(input("Please enter an option: "))

        #Ecodes the password that the user inputs using the encode function.
        if menu_choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        #Decodes the encoded password of the user using the decode function
        #Returns the original password
        elif menu_choice == 2:
            pass

        #Quits the program
        elif menu_choice == 3:
            break

if __name__ == "__main__":
    main()



