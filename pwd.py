import random
flag = True
while flag == True:
    print("****THE SOFTWARE024'S PASSWORD SECURITY SYSTEM****")
    print("Program version 1.20.0")
    print("")
    print("1 -> Add or generate password to save file.")
    print("2 -> Retrieve password from save file.")
    print("3 -> Format save file")
    print("4 -> Display entire save file")
    print("5 -> Quit.")
    print("NOTE : If this program throws an error about a missing or corrupt file, go into the code and change the hardcoded directory path")
    option = int(input("Select option : "))
    if option == 1:


        print('Welcome to your password generator!')

        chars = '¦¬`1!23£4$€5%6^7&8*9(0-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'

        number = input('Amount of passwords to generate: ')
        number = int(number)

        length = input('Password length: ')
        length = int(length)



        for pwd in range(number):
            passwords = ''
            for c in range(length):
                passwords += random.choice(chars)
            print(passwords)
    elif option == 2:
        passopen  = open("G:/Python/Demo/PASSWORD.TXT","r")
        set1 = input("Please enter the set name for the desired password. : ")
        for line in passopen:
            if line.split(" -> ")[0] == set1:
                print(line.split(" -> ")[1])
    elif option == 3:
        del1 = input("WARNING! This option will delete all characters stored in save file and can no longer be previewed. To proceed, you must type 'YES'. To go to the previous screen,press a key...")
        if del1 == "YES":
            passdelete = open("G:/PYTHON/DEMO/Password.txt","w")
            passdelete.write(del1 + "                                      ")
            passave.close()
        else:
            print("Operation has been aborted and you will be redirected to the main screen")
    elif option == 4:
        passall = open("G:/Python/Demo/PASSWORD.TXT","r")
        print(passall)
        passall.close()

    elif option == 5:
        print("You have quit this program and you are in Powershell. Use the 'CMD' command to goto Windows Command Processer")
        flag = False    

    


def randomchr():
    for _ in range(100001):
        print(random.choice(chars))
        
def storage():
    return 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv'

def passw():
    pass1 = input('Enter password: ')
    if pass1 == 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv':
        print('You found the secret password!')
        def secret1():
            print('Use the function storage() to get access to this again.')
        secret1()
    else:
        pass2 = input('Enter password: ')
        if pass2 == 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv':
            print('You found the secret PWD')
            def secret1():
                print('Use the function storage() to get access to this again.')
                
        else:
            return 'You lost!'


""
