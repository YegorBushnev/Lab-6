"""
Lab 5
Authors: Yegor Bushnev and Dustin Nguyen
Class: COP3502C
Section: 22282
Description: Decode function that will be used in my lab partner's project. The function takes in the encoded password
as a string and then converts each digit in the string to an integer. 3 is subtracted from each integer to return
the decoded password.
"""

def decode(password):
    password_list = []
    decoded_list = []
    for i in password:
        password_list.append(int(i))
    for i in range(0, len(password_list)):
        if 3 <= password_list[i]:
            decoded_list.append(str(password_list[i] - 3))
        elif 0 <= password_list[i] <= 2:
            decode_var = (password_list[i] - 3) + 10
            decoded_list.append(str(decode_var))
    decode_string = ''.join(decoded_list)
    return decode_string


