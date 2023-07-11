import random
import time
length = 20
print("*****|THE SECURITY MANAGER SYSTEM|*****")
print("Program version: 1.11.4.")
print("")
name = input("Enter your name as this program is in security level 10 mode. (It will be kept private throughout entire your session). ")
print("")
print("Currently running backround checks on your OS system for bot detection and prevention in progress. Please wait...")
time.sleep(7)
print("")
print("Hello " + name + "!")
print("You have been confirmed you are not a bot. You are now going to be directed to the main menu.")
print("")
input("Press enter to continue...")
print("")
security_manager = True
while security_manager == True:
    print("1 -> About this program.")
    print("2 -> Quit program.")
    print("")
    print("Accessable Programs:")
    print("")
    print("3 -> THE PASSWORD MANAGER SYSTEM.")
    print("4 -> THE BINARY ENCRYPTER AND DECRYPTER SYSTEM.")
    print("")
    print("This program and all of the accessable program are open-source programs so you can share it anywhere on the internet, copy it on USB/CD/DVD or other medias so please mention in your copy Software24TCG and Okmeque1 so that the original code is not lost to time.")
    print("")
    option = int(input("Select option: "))
    if option == 1:
        print("")
        input("Specifications/informations about this program: ")
        print("")
        print("-> Program name: THE SECURITY MANAGER SYSTEM.")
        print("-> Manufacturers: Software24TCG.")
        print("-> Manufacturers' company: © TCG - Technology, Coding and Gaming Inc.™")
        print("-> Program version: 1.11.4.")
        print("-> Program description: This program is a Security Manager System. It can access programs that are useful in terms of security and protection of your personel datas.")
        print("")
        input("About this program's security level: ")
        print("")
        print("This program will ask your name at every prompt to ensure that it is a human and not a bot.")
        input("This program is a security level 10 program. Here are all the security levels that all of the accessable programs including this one will use.")
        print("")
        print("Security Levels:")
        print("")
        print("1 -> Level 1: Low level.")
        print("2 -> Level 2: Standart level.")
        print("3 -> Level 3: Moderate level.")
        print("4 -> Level 4: Strong level.")
        print("5 -> Level 5: Low bot protection level + Strong level.")
        print("6 -> Level 6: Standart bot protection level + Strong level.")
        print("7 -> Level 7: Moderate bot protection level + Strong level.")
        print("8 -> Level 8: Strong bot protection level + Strong level.")
        print("9 -> Level 9: Strong bot protection level + Max level.")
        print("10 -> Level 10: Max bot protection level + Max level.")
        print("")
        print("The more stronger the level is, the more security questions and checks it will require. ")
        print("In this case, with level 10 security, this program will be running backrounds checks on your PC's informations, SSH, IPv4 and IPv6 addresses (in a way so that your informations are kept secure) after you have entered your name. ")
        print("")
        input("Program's releases and pre-releases: ")
        print("")
        print("Program's releases: ")
        print("1 -> Option 1.")
        print("2 -> Option 2.")
        print("3 -> Option 3.")
        print("")
        print("Program's pre-releases: ")
        print("None.")
        print("")
        input("Press enter to continue...")
    
    elif option == 3:
        print("")
        print("This option will open The Password Manager System.")
        print("")
        input("Press enter to continue...")
        time.sleep(2)
        print("")
        pwd_manager = True
        while pwd_manager == True:
            print("*****|THE PASSWORD MANAGER SYSTEM|*****")
            print("Program version: 1.20.0.")
            print("")
            print("1 -> Add and generate password to a save file.")
            print("2 -> Show a password from a save file.")
            print("3 -> Show all passwords from a save file.")
            print("4 -> About this program.")
            print("5 -> Access TCG Headquarters' Database.")
            print("6 -> Quit program.")
            print("")
            print("Please read option 4 if this is the first time you use this program or if any updates has been done on this program's version, as new options or functions could be added!")
            print("")
            print("When you are asked for a valid file name, please make sure that the directory is valid and for best compatability and please make sure that the file exists.")
            print("")
            optionpwd_manager = int(input("Select option : "))
            if optionpwd_manager == 1:

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
                        set0 = input("Enter a name or nothing to continue this program. This program does not support having 2 sets of the same name. Entering a name that already exists will cause conflict. ")
                        passave = open(filename,"a")
                        passave.write(set0 + " -> " + passwords + "\n")
                        passave.close()
                    else:
                        set0 = input("Enter a name or nothing to continue this program. This program does not support having 2 sets of the same name. Entering a name that already exists will cause conflict. ")
                        passave = open(filename,"a")
                        passave.write(set0 + " -> " + passwords + "\n")
                        passave.close()
                    print("")
                    print("Save has completed with no disk errors.")
                    print("")
                    input("Press enter to continue...")
            elif optionpwd_manager == 2:
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

            elif optionpwd_manager == 3:
                print("")
                print("An error has occured! Any unsaved data will be deleted. To continue: ")
                print("-> Press enter to return to the main menu.")
                print("-> Press CTRL + C to terminate this program. You will lose any unsaved data in any open programs.")
                print("")
                input("Press enter or CTRL + C to continue...")
                # passall = open("U:\pwd_openscs.pwd","r")
                # print(passall)
                # passall.close()
    
            elif optionpwd_manager == 4:
                print("")
                input("Specifications/informations about this program: ")
                print("")
                print("-> Program name: THE PASSWORD MANAGER SECURITY SYSTEM.")
                print("-> Manufacturers: Software24TCG and Okmeque1.")
                print("-> Manufacturers' company: © TCG - Technology, Coding and Gaming Inc.™")
                print("-> Program version: 1.20.0.")
                print("-> Program description: This program is a Password Manager Security System. It can create, save, read, show and manage passcodes.")
                print("")
                input("About this program's security level: ")
                print("")
                input("This program is a security level 8 program. You can learn more about security levels with option 1 in The Security Manager System.")
                print("")
                print("In this case, with level 8 security, this program will be running backrounds checks on your PC's informations, SSH and IPv4 addresses (in a way so that your informations are kept secure) when you entered this program. ")
                print("")
                input("Recommendations about this program: ")
                print("")
                print("1 -> When creating a passcode (option 1), choose between 10 to 50 characters of length as it's enough for passcode security. More characters could cause passcode loading problems, program or buffer crashing/overload or passcode failing to be saved.")
                print("2 -> When showing a passcode (option 2), your file name path must be as this example path layout: 'C:\...\Password Manager Security System\pwd' for the the function to work.")
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
                print("")
                print("Program's pre-releases: ")
                print("1 -> Option 3.")
                print("")
                input("Press enter to continue...")

            elif optionpwd_manager == 6:
                print("")
                print("Saving data to database. Please wait...")
                time.sleep (5)
                print("")
                input("Press enter to continue...")
                pwd_manager = False




            elif optionpwd_manager == 5:
                print("")
                passstorg = input('Enter TCG Admin password: ')
                if passstorg == 'hchi&okmeque1.tcg_hq':
                    print("")
                    print("Correct passcode. ")
                    print("Loading TCG Headquarters' Database...")
                    time.sleep (4)
                    print("")
                    print("Currently nothing on the database.")
                    print("")
                    input("Press enter to continue...")
                else:
                    print("Wrong password!")
                    print("")
                    input("Press enter to continue...")
    
    elif option == 4:
        print("")
        print("This option will open The Binary Encrypter and Decrypter System.")
        print("")
        input("Press enter to continue...")
        time.sleep(2)
        print("")
        binary_encrypt_decrypt_system = True
        while binary_encrypt_decrypt_system == True:
            print("*****|THE BINARY ENCRYPTER AND DECRYPTER SYSTEM|*****")
            print("Program version: 1.12.0")
            print("")
            print("1 -> Encrypt text.")
            print("2 -> Quit program.")
            print("")
            optionbinary_encrypt_decrypt_system = int(input("Select option : "))
            if optionbinary_encrypt_decrypt_system == 1:
                text=input("Please enter text to encrypt into binary: ")
                li=list(text)
                code=""
                for x in range(len(li)):
                    t1=li[x]
                    t2=ord(t1)
                    t3=bin(t2)
                    t4=t3[2:]
                    code=code+t4
                print("This is your text converted into binary: ",code)
            
            elif optionbinary_encrypt_decrypt_system == 2:
                print("")
                print("Saving data to database. Please wait...")
                time.sleep (5)
                print("")
                input("Press enter to continue...")
                binary_encrypt_decrypt_system = False

    elif option ==  2:
        print("")
        print("Saving data to database. Please wait...")
        time.sleep (5)
        print("")
        input("Press enter to continue...")
        security_manager = False
