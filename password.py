
def encoder(password):
    new_password = ''
    for i in password:
        num = int(i)
        if num >= 7:
            new_num = num - 7
        else:
            new_num = num + 3
        new_password += str(new_num)
    return new_password

def main()
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")

        response = int(input("Please enter an option: "))
        if response == 1:
            password_to_encode = input("Please enter your password to encode: ")
            new_password = encoder(password_to_encode)
            print("Your password has been encoded and stored!")
        elif response == 2:
            print(f"The encoded password is {new_password}, the original password is {password_to_encode}.")
        elif response == 3:
            quit()

if __name__ == '__main__':
    main()
