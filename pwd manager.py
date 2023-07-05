import random
import time
length = 20
name = input("Enter your name (It will be kept private throughout entire your session): ")
print("")
print("Hello" + " " + name + "!")
print("")
time.sleep(3)
flag = True
while flag == True:
    print("*****|THE PASSWORD MANAGER SECURITY SYSTEM|*****")
    print("Program version: 1.20.0.")
    print("")
    print("1 -> Add and generate password to a save file.")
    print("2 -> Show a password from a save file.")
    print("3 -> Show all passwords from a save file.")
    print("4 -> Show more informations about this program.")
    print("5 -> Access TCG Headquarters' Database.")
    print("6 -> Top secret!")
    print("7 -> Quit program.")
    print("")
    print("Please read the whole option 4 if this is the first time you use this program or if any updates has been done on this program's version!")
    print("")
    print("When you are asked for a valid file name, please make sure that the directory is valid and for best compatability and please make sure that the file exists.")
    print("")
    print("This is an open-source program so you can share it anywhere on the internet, USB/CD/DVD or other media. Please mention in your copy Software024 and Okmeque1 so that the original code is not lost in/to time.")
    print("")
    option = int(input("Select option : "))
    if option == 1:

        print("")
        print('Welcome to your password generator! (learn more with option 4).')

        chars = '¦¬`1!23£4$€5%6^7&8*9(0-_=+q"~{[]}=+QwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~^¨µù%#\|zéèàZxXcCvVbBnNmMm,<.>/?)'

        number = 1
        length = input('Password length: ')
        length = int(length)



        for pwd in range(number):
            passwords = ''
            for c in range(length):
                passwords += random.choice(chars)
            print("")
            print(passwords)
            print("")
            print('Passwords generated! Now saving...')
            filename = input("Please enter a valid file name: ")
            if filename == "":
                filename = "U:\pwd_openscs.pwd"
                set0 = input("Enter a name or nothing to continue this program. This program does NOT support having 2 sets of the same name. Entering a name that already exists will cause conflict. ")
                passave = open(filename,"a")
                passave.write(set0 + " -> " + passwords + "\n")
                passave.close()
            else:
                set0 = input("Enter a name or nothing to continue this program. This program does NOT support having 2 sets of the same name. Entering a name that already exists will cause conflict. ")
                passave = open(filename,"a")
                passave.write(set0 + " -> " + passwords + "\n")
                passave.close()
            print("")
            print("Save has completed with no disk errors.")
            print("")
            input("Press enter to continue...")
    elif option == 2:
        print("")
        fileopen = input("Please enter a valid file name path. The format must be full with the drive name included (learn more with option 4)! If this is not respected, this program will/could terminate: ")
        if fileopen == "":
            fileopen = "U:\pwd_openscs.pwd"
            passopen  = open("U:\pwd_openscs.pwd","r")
            set1 = input("Please enter the set name for the desired password: ")
            for line in passopen:
                if line.split(" -> ")[0] == set1:
                    print("")
                    print(line.split(" -> ")[1])
                    print("")
                    input("Press enter to continue...")
                   
        else:
            passopen  = open(fileopen,"r")
            set1 = input("Please enter the set name for the desired password: ")
            for line in passopen:
                if line.split(" -> ")[0] == set1:
                    print("")
                    print(line.split(" -> ")[1])
                    print("")
                    input("Press enter to continue...")

    elif option == 3:
        print("")
        print("An error has occured! Any unsaved data will be deleted. To continue: ")
        print("-> Press enter to return to the main menu.")
        print("-> Press CTRL + C to terminate this program. You will lose any unsaved data in any open programs.")
        print("")
        input("Press enter or CTRL + C to continue...")
        # passall = open("U:\pwd_openscs.pwd","r")
        # print(passall)
        # passall.close()
    
    elif option == 4:
        print("")
        input("Specifications/informations about this program: ")
        print("")
        print("-> Program name: THE PASSWORD MANAGER SECURITY SYSTEM.")
        print("-> Manufacturers: Software24TCG and Okmeque1.")
        print("-> Manufacturers' company: © TCG - Technology, Coding and Gaming Inc.™")
        print("-> Program version: 1.20.0.")
        print("-> Program description: This program is a Password Manager Security System. It can create, save, read, show and manage passcodes.")
        print("")
        input("Recommendations about this program: ")
        print("")
        print("1 -> When creating a passcode (option 1), choose between 10 to 50 characters of length as it's enough for passcode security. More characters could cause passcode loading problems, program or buffer crashing/overload or passcode failing to be saved.")
        print("2 -> When showing a passcode (option 2), your file name path must be as this example path layout: 'C:\Password Manager Security System\pwd' for the the function to work.")
        print("")
        input("Problems of this program: ")
        print("")
        print("1 -> The showing all passcodes from a save file option (option 3) is not fully released yet and is still under developpement. Any attempts of using it now can lead into a program error and could delete any unsaved data.")
        print("")
        input("Program's releases and pre-releases: ")
        print("")
        print("Program's releases: ")
        print("1 -> Option 1.")
        print("2 -> Option 2.")
        print("3 -> Option 4.")
        print("4 -> Option 5.")
        print("5 -> Option 5.")
        print("6 -> Option 6.")
        print("7 -> Option 7.")
        print("")
        print("Program's pre-releases: ")
        print("1 -> Option 3.")
        print("")
        input("Press enter to continue...")

    elif option == 7:
        print("")
        print("Saving data to database. Please wait...")
        time.sleep (8)
        print("")
        input("Press enter to continue...")
        flag = False




    elif option == 5:
        print("")
        passstorg = input('Enter TCG Admin password: ')
        if passstorg == 'hchi&okmeque1.tcg_hq':
            print("")
            print("Correct passcode. ")
            print("Loading TCG Headquarters' Database...")
            time.sleep (5)
            print("")
            print("This password will be used to unlock option 6: ")
            print("s:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv")
            print("")
            input("Press enter to continue...")
        else:
            print("Wrong password!")
            print("")
            input("Press enter to continue...")        
        

    elif option == 6:
        print("")
        pass1 = input('Enter password: ')
        if pass1 == 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv':
            print("")
            print('Correct password!')
            print("You won! ")
            print("")
            input("Press enter to continue...")
        else:
            print("Wrong password!")
            print("You lost! ")
            print("")
            input("Press enter to continue...")

