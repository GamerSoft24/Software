from tkinter import *
import random

length = 0  # Define the global variable length here
savefile = ""  # Define the global variable savefile here

def clear_screen():
    for widget in windows.winfo_children():
        widget.destroy()
    l2 = Label(windows, text="Welcome to your password generator! (learn more with button 4).").pack()
    l3 = Label(windows, text="Password length:").pack()
    global length
    entry = Entry(windows, width=40)
    entry.focus_set()
    entry.pack()
    confirm = Button(windows, text="Continue...", command=lambda: generate_inprogress(entry.get()), width=20)
    confirm.pack(pady=20)

def generate_inprogress(length_value):
    global passwords
    for widget in windows.winfo_children():
        widget.destroy()
    chars = '¦¬`1!23£4$€5%6^7&8*9(0-_=+qQwWeErRtTyYuUiIoOpPaAs°]}^`|[{#~SdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
    num = 1
    if length_value.isdigit():
        length_value = int(length_value)
        for a in range(num):
            passwords = ""
            for b in range(length_value):
                passwords += random.choice(chars)
                print(f"{b+1} of {length_value} completed!")
        password_label = Label(windows, text="Password generated. Now saving: " + passwords)
        password_label.pack()
        global savefile
        l5 = Label(windows, text="Now saving to save file...").pack()
        l6 = Label(windows, text="Please enter a valid file name:").pack()
        savefile = Entry(windows, width=40)
        savefile.focus_set()
        savefile.pack()
        confirm = Button(windows, text="Continue...", command=lambda: save(savefile.get(), passwords), width=20)
        confirm.pack(pady=20)        
    else:
        print("Bad value for buffer heap 0x20358 (131072K). Returning to main menu...")
        
def save(savefile_value, password_value):
    for widget in windows.winfo_children():
        widget.destroy()
    if savefile_value == "":
        savefile_value = "G:\python\demo\demo.pc"
    l7 = Label(windows, text="Please enter a valid set name. This program does not support having 2 sets with the same name as you may encounter issues when reading back from the file. → ")
    l7.pack()
    setname = Entry(windows, width=40)
    setname.focus_set()
    setname.pack()
    
    def save_password():
        set_value = setname.get()
        passave = open(savefile_value, "a")
        passave.write(set_value + " -> " + password_value + "\n")
        passave.close()
        l8 = Label(windows, text="Password saved successfully!").pack()
        backstart = Button(windows, text="Continue...", command=lambda: [windows.destroy(), start()], width=20)
        backstart.pack()
    
    confirm = Button(windows, text="Save Password", command=save_password, width=20)
    confirm.pack(pady=20)
def showset1():
    for widget in windows.winfo_children():
        widget.destroy()
    l9 = Label(windows, text="Please enter a valid file name:").pack()
    fileshow = Entry(windows, width=40)
    fileshow.focus_set()
    fileshow.pack() 
    nextshow = Button(windows, text="Continue...", command=lambda: showset2(fileshow.get()), width=20).pack()

def showset2(file):
    for widget in windows.winfo_children():
        widget.destroy()
    if file == "":
        file = "G:\python\demo\demo.pc"

    l10 = Label(windows, text="Please enter a valid set name:").pack()
    setshow = Entry(windows, width=40)
    setshow.focus_set()
    setshow.pack()

    def show_password():
        set1 = setshow.get()
        found_password = False

        with open(file, "r") as f:
            for line in f:
                if line.split(" -> ")[0] == set1:
                    password = line.split(" -> ")[1].rstrip()
                    l11 = Label(windows, text="The password for the set name entered is: " + password).pack()
                    print(password)
                    found_password = True
                    break

        if not found_password:
            l11 = Label(windows, text="No password found for the set name entered.").pack()

        backstart = Button(windows, text="Continue", command=lambda: [windows.destroy(), start()], width=20)
        backstart.pack()

    confirm = Button(windows, text="Show Password", command=show_password, width=20)
    confirm.pack(pady=20)
def delete():
    for widget in windows.winfo_children():
        widget.destroy()

    l12 = Label(windows, text="This is an IRREVERSIBLE decision and you may corrupt files if used incorrectly. Please enter your password defined on line 108 → ")
    l12.pack()

    password1 = "GUIPWD-Okmeque1_edition"
    uac = Entry(windows, width=40)
    uac.focus_set()
    uac.pack()

    def setchk():
        uac_in = uac.get()
        if uac_in == password1:
            l13 = Label(windows, text="Please enter a valid file name (none to default of G:\python\demo\demo.pc). The format must be a:\directory\pwdfile.extention. :")
            l13.pack()

            filesel = Entry(windows, width=40)
            filesel.focus_set()
            filesel.pack()

            def filechk():
                setdel = filesel.get()
                if setdel == "":
                    setdel = "G:\python\demo\demo.pc"
                l14 = Label(windows, text="Please enter a valid set name for the desired password to be deleted. →")
                l14.pack()

                pwddel = Entry(windows, width=40)
                pwddel.focus_set()
                pwddel.pack()

                def laststage():
                    with open(setdel, "r") as read0:
                        read = read0.readlines()

                    pwdtodel = pwddel.get()  # Get the value of pwdtodel here

                    with open(setdel, "w") as passdelete:
                        for line in read:
                            if line.split(" -> ")[0] != pwdtodel:
                                passdelete.write(line)

                    print("Set name deleted.")
                    E = Button(windows, text="Continue...", command=start())
                    windows.destroy()

                next2 = Button(windows, text="Continue...", command=laststage)
                next2.pack()

            next1 = Button(windows, text="Continue...", command=filechk, width=20)
            next1.pack()

    delcnf = Button(windows, text="Continue with action...", command=setchk)
    delcnf.pack()
def show():
    for widget in windows.winfo_children():
        widget.destroy()   
    s1 = Label(windows,text="This program is open source and made by Okmeque1.If you desire to copy this program,please keep a mention of Okmeque1 in the code as so the original code is not lost to time.")
    s2 = Label(windows,text="This program can create a secure password of your length,8 to 19 characters is recommended for a secure password(DO NOT MAKE YOUR PASSWORD TOO LONG AS IT CAN OVERLOAD THE BUFFER ON THE COMPUTER AND CRASH IT.),can retrieve the password(this function is only useful if the file extention is foreign) and can erase the password file in case of hacking")
    s3 = Label(windows,text="For maximum compatability,run this program in Python 3+ and Windows 7 or higher(Please note that you can run it lower than those versions but the program might throw errors in lower version of windows(XP,Vista,etc) and some python functions might not exist in lower versions of python)")
    s4 = Label(windows,text="The program will run on macOS and Linux but the filepath format will vary as neither of those use drive letters (eg A:\directory\file.ext).The structure for those OS's will either be : ")
    s5 = Label(windows,text="1 : macOS : The file structure may be /path/path1/pwdfile.extention (Please note that this program might not work as macOS does NOT support harddisk writing to a bit level and might throw an error about write fail.)")
    s6 = Label(windows,text="2 : Linux : The file structure is unclear as there are so many Linux distros out there but the structure may be /dev/sda/mountpoint1/folder/pwdfile.extention.")
    s7 = Label(windows,text="Please note that in both cases,DO NOT USE FOREIGN FILE EXTENTIONS(.dell,pc or any non-standard file format that can't be read by a text editor.) as the disk check utility might assume that the file is corrupt and delete it.")
    s8 = Label(windows,text="Please do NOT modify this program as the file may become unoriginal and might cause program breakage.This program took HOURS to complete and be at its current state.")
def show():
    for widget in windows.winfo_children():
        widget.destroy()

    s1 = "This program is open source and made by Okmeque1. If you desire to copy this program, please keep a mention of Okmeque1 in the code so the original code is not lost to time.\n"
    s2 = "This program can create a secure password of your desired length, 8 to 19 characters is recommended for a secure password (DO NOT MAKE YOUR PASSWORD TOO LONG AS IT CAN OVERLOAD THE BUFFER ON THE COMPUTER AND CRASH IT). It can also retrieve the password (this function is only useful if the file extension is familiar) and can erase the password file in case of hacking.\n"
    s3 = "For maximum compatibility, run this program in Python 3+ and Windows 7 or higher. Please note that you can run it in lower versions, but the program might throw errors in lower versions of Windows (XP, Vista, etc) and some Python functions might not exist in lower versions of Python.\n"
    s4 = "The program will run on macOS and Linux, but the filepath format will vary as neither of those use drive letters. The structure for those OS's will either be:\n"
    s5 = "1: macOS: The file structure may be /path/path1/pwdfile.extension. Please note that this program might not work as macOS does NOT support hard disk writing to a bit level and might throw an error about write fail.\n"
    s6 = "2: Linux: The file structure is unclear as there are so many Linux distros out there, but the structure may be /dev/sda/mountpoint1/folder/pwdfile.extension.\n"
    s7 = "Please note that in both cases, DO NOT USE FOREIGN FILE EXTENSIONS (.dell, .pc, or any non-standard file format that can't be read by a text editor) as the disk check utility might assume that the file is corrupt and delete it.\n"

    text = Text(windows, height=10, width=800)
    text.pack(side=LEFT, fill=Y)

    scrollbar = Scrollbar(windows)
    scrollbar.pack(side=RIGHT, fill=Y)

    text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text.yview)

    text.insert(END, s1)
    text.insert(END, s2)
    text.insert(END, s3)
    text.insert(END, s4)
    text.insert(END, s5)
    text.insert(END, s6)
    text.insert(END, s7)

    b9 = Button(windows, text="Back to the main menu...", command=del1)
    b9.pack()
def del1():
    windows.destroy()
    start()

def quit():
    windows.destroy()
    print("Program ended.")
def start():
    global windows
    windows = Tk()
    windows.title("THE PASSWORD MANAGER SECURITY SYSTEM - GUI Edition")
    windows.geometry("1024x768")

    button_width = 10

    l1 = Label(windows, text="*****|THE PASSWORD MANAGER SECURITY SYSTEM|*****").pack()
    l2 = Label(windows, text="Program version: 1.15.2.").pack()

    b1 = Button(windows, text="1 -> Add and generate password to save file.", command=clear_screen, activeforeground="green", activebackground="green", pady=10)
    b2 = Button(windows, text="2 -> Show a passwords from save file.", command=showset1, activeforeground="blue", activebackground="blue", pady=10)
    b3 = Button(windows, text="3 -> Show all passwords from a save file.", command=delete,activeforeground="blue", activebackground="blue", pady=10)
    b4 = Button(windows, text="4 -> Show more informations about this program.", command=show, activeforeground="yellow", activebackground="yellow", pady=10)
    b5 = Button(windows,text="5 -> Quit program.", activeforeground="red", activebackground="red", pady=10, command=quit)
    b1.pack(side=TOP, fill=BOTH, expand=False)
    b2.pack(side=TOP, fill=BOTH, expand=False)
    b3.pack(side=TOP, fill=BOTH, expand=False)
    b4.pack(side=TOP, fill=BOTH, expand=False)
    b4.pack(side=TOP, fill=BOTH, expand=False)
    b5.pack(side=TOP,fill=BOTH,expand=False)
    windows.mainloop()
start()
