import os
import tkinter as tk
from tkinter import messagebox as msgbox
import random as rnd
import time
def sysconfig():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("SYSTEM CONFIGURATION TOOL - (C) MICRO$OFT 1981-1983")
    print("[1] DISPLAY CURRENT CONFIGURATION")
    print("[2] CHANGE SYSTEM SETTINGS")
    print("[3] QUIT TO BOOT")
    sconfig = input("Please select the options marked in []. : ")
    config = "****CURRENT SYSTEM CONFIGURATION****\n[1]DATE/TIME = 03/27/84 18:35\n[2]FLOPPY A = TYPE 1 - 5.25/360K\nFLOPPY B = NONE - NONE\n[3]FIXED DISK 0 = NONE - NONE\n[4]CDROM = NONE - NONE\n[5]BOOT = A,C,B,CDROM"
    if sconfig == "1":
        print(config)
        input("Press ENTER |-> to continue.")
        sysconfig()
    elif sconfig == "2":
            print(config)
            cconfig = input("Please enter the setting number to change : ")
            if cconfig == "1":
                input("Enter new date : 00/11/2222 : ")
                input("Enter new time : 12:34 : ")
                sysconfig()
            elif cconfig == "2":
                print("TYPE 1 = 5.25/360K\nTYPE 2 = 5.25/1.2M\nTYPE 3 = 3.5/720K\nTYPE 4 = 3.5/1.44MHD")
                input("Enter type number : ")
                sysconfig()
            elif cconfig == "3":
                print("Refer to your documentation for hard disk types.Use type CS for a custom hard drive parameters.")
                hdconfig = input("Choose type : ")
                if hdconfig == "CS":
                    input("Hard disk size(Bytes) : ")
                    input("Head count : ")
                    input("Cylinders : ")
                    input("Sectors : ")
                    input("Driver File(A:\DRIVER\DRIVER.DRV) : ")
                    sysconfig()
            elif cconfig == "4":
                print("[1]SCSI CDROM\n[2]IDE CDROM\n[3]CUSTOM")
                dsconfig = input("Enter type : ")
                if dsconfig == "1":
                    print("SCSI CDROM DRIVER LOADED.")
                    sysconfig()
                elif dsconfig == "2":
                    print("IDE CDROM DRIVER LOADED.CDROM DRIVE ON SECONDARY MASTER.")
                    sysconfig()
                elif dsconfig == "3":
                        input("Driver files(A:\DRIVER\DRIVER.DRV) : ")
                        print("Driver failed to load.Possible reasons are bad/corrupt drivers or wrong drivers.Check your diskette and drive.")
                        sysconfig()
            elif cconfig == "5":
                input("Enter BOOT order - Possible values are A,B,C,CDROM : ")
                sysconfig()
    elif sconfig == "3":
        print("Rebooting NOW...")
        time.sleep(3)
        boot()
    else:
        sysconfig()
def boot():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    os.system("title DOS - Windows Virtual Machine")
    print("THE WINDOWS VIRTUAL BIOS VERSION 3.20")
    print("DRIVER WAS NOT INSTALLED.CD-ROM DRIVE NOT FOUND")
    print("No fixed disks detected.")
    print("327680B OK")
    print("Loading C...Not loaded.")
    print("No fixed disks detected.")
    print("ERROR\n0271 : Check date and time settings")
    dbios = input("Press ENTER |-> to enter SYSCONFIG")
    if dbios == "":
        sysconfig()
    elif dbios == 'ATCFWCHG~1':
        print("Now in debug mode.Some errors will NOT appear.")
        command()
    print("Loading A:...",end='\r')
    time.sleep(10)
    error = [1,2,3,4,5,6,7,8,9]
    badfloppy = rnd.choice(error)
    if badfloppy == 1:
        print("Loading A:...Error!")
        print("Diskette drive error.Reinsert system diskette in A: and")
        os.system("pause")
        boot()
    elif badfloppy == 2:
        print("Loading A:...Error!")
        print("Non system disk or disk error")
        print("Replace the disk and")
        os.system("pause")
        boot()
    elif badfloppy == 3:
        print("Loading A:...Error!")
        print("Invalid system disk")
        print("Replace the disk and")
        os.system("pause")
        boot()
    elif badfloppy == 4:
        print("Loading A:...Error!")
        print("Reboot and Select proper Boot device")
        print("or Insert Boot media in selected boot device and")
        os.system("pause")
        boot()
    elif badfloppy == 5:
        print("Loading A:...Success.")
        print("MS-DOS 3.30")
        print("Copyright (c) Microsoft / IBM 1981-1985")
        print("The following file is missing or corrupt : BOOT.MBR")
        print("The following file is missing or corrupt : BOOT.BSS")
        print("There is an error in your CONFIG.SYS on line 37.")
        print("While initializing device IOS:")
        print(" A subsystem driver failed to load. \n \n")
        print("Either a file in the .\iosubsys")
        print("subdirectory is corrupt, or the system is low on memory.")
        print("DOS Failed to load.")
        os.system("pause")
        boot()
    elif badfloppy == 6 or badfloppy == 7 or badfloppy == 8 or badfloppy == 9:
        print("Loading A:...Success.")
        print("MS-DOS 3.30")
        print("Copyright (c) Microsoft / IBM 1981-1985")
        print("Initializing sound device...")
        time.sleep(10)
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        print("****CD-ROM DRIVER****\nThis driver is copyrighted (c) by International Business Machines International 1983-1991")
        time.sleep(3)
        print("Driver/drive NOT installed properly.CD-ROM Drive NOT found.")
        time.sleep(0.5)
        print("Device driver not found : TPCD001\nNo Valid CDROM device drivers selected\n")
        time.sleep(0.3)
        print("Bad command or file name")
        time.sleep(0.31)
        print("Invalid drive specification")
        time.sleep(0.11)
        print("Label not found.\nInvalid drive in search path")
        time.sleep(0.31)
        print("Bad command or file name")
        command()
def command():
    A = input('A:>')
    if A == 'dir':
        print('Volume label is BootDisk')
        print('Directory of A:')
        print("=============================")
        print('FILENAME         SIZE  DATE  ')
        print('xcopy.exe        1328 3-27-22')
        print('command.com      4213 3-27-22')
        print('edit.com         7414 3-27-22')
        print('format.com       5001 3-27-22')
        print('autoexec.bat     2006 3-27-22')
        print('config.sys       1064 3-27-22')
        print('edit.ini          440 3-27-22')
        print('boot.mbr          512 3-27-22')
        print('boot.bss          745 3-27-22')
        print('fdisk.exe        4660 3-27-22')
        print("sdsys.exe        6540 3-07-91")
        print("windir.exe        657 5-10-07")
        print("wbytes.exe       6550 9-01-23")
        print("chkdsk.exe       6543 3-27-22")
        print("")
        command()
    elif A == 'fdisk.exe':
        print('No fixed disks presents')
        print("")
        command()
    elif A == 'format.com':
        for h in range(11):
            print('Formatting track' + ": " + str(h))
        print("Formatting complete! ")
        print("")
    elif A == 'autoexec.bat':
        print("")
        command()
    elif A == 'command.com':
        print("")
        command()
    elif A == 'edit.com':
        print('EDIT VERSION 1.00')
        print('1 → Add value for a file.')
        print('2 → Replace value for a file.')
        print('3 → Erase file.')
        print('4 → List file.')
        B = input('Choose an option (any invalid option will quit the program and return to MS-DOS). ')
        C = int(B)
        file = ''
        if C == 1:
            write = True
            while write == True:
                d = input('Write anything you want. Type eX1t to quit the program and return to MS-DOS. ')
                file += d
                if d == 'eX1t':
                    write = False
                    file += d
                    command()
                elif d == 'c0Mn4mD':
                    write = False
                    command()
        if C == 2:
            write = True
            while write == True:
                print('Please note that this option will wipe any existing file. ')
                d = input('Write anything you want. Type eX1t to quit the program and return to MS-DOS. Type c0Mn4mD to quit without saving. ')
                file = d
                if d == 'eX1t':
                    write = False
                    file = d
                    command()
                elif d == 'c0Mn4mD':
                    write = False
                    command
        if C == 3:
            
            e = input('This option is IRREVERSIBLE. Type eR45€ to erase the file.')
            f = input('This option is IRREVERSIBLE. LAST WARNING! Type Er8s£ to erase the file.')
            if e == 'eR45€' and f == 'Er8s£':
                file = ''
                command()
        if C == 4:
            if file == '':
                print('List empty. Quitting now...')
                print("")
            else:
                print(file)
                print("")
                command()
        else:
            command()
    elif A == 'xcopy.exe':
        print('No other drives or disks have been detected. This includes Hard Disks/Drives, or other floppy disks')
        print("")
        command()
    elif A == 'copy':
        print('Sorry, this disk is write-protected (read-only) and cannot be copied.')
        print("")
        command()
    elif A == 'ver':
        print('MS-DOS 4.10.0')
        print("")
        command()
    elif A == 'version':
        print('MS-DOS 4.10.0')
        print("")
        command()
    elif A == 'Software24TCG':
        print('Software24TCG and Okmeque1 MS-DOS 4.10.0 running on 8TB A: Drive.')
        print('Software24TCG is the co-creator of MS-DOS.')
        print("")
        command()
    elif A == 'Okmeque1':
        print('Okmeque1 and Software24TCG MS-DOS 4.10.0 running on 8TB A: Drive.')
        print('Okmeque1 is the creator of MS-DOS.')
        print("")
        command()
    elif A == 'specs':
        print('8.74 GHz/s IBM at: 64GB RAM, 16 cores 18 threads.')
        print("")
        command()
    elif A == 'help':
        print('fdisk.exe : Fixed disk utility.')
        print('edit.com : Edits text files.')
        print('stop : Stops the whole computer.')
        print('ver : Shows the current version.')
        print('format.com : Formats any disks or drives.')
        print('dir : Lists directory.')
        print('config : enter SYSTEM BIOS ')
        print('config /s : show advanced PC configuration without leaving DOS')
        print('config /syste : Show the current CONFIG.SYS file')
        print('specs : Shows the specifications of the computer.')
        print('specifications : show advanced PC specifications')
        print('')
        print('Note : This version of DOS is a bootdisk and only contains')
        print('minimal commands. To have more commands,eject this disk    ')
        print('and insert an installer disk. Then hold CTRL + ALT and then')
        print('press DELETE/DEL/SUPPR. You need a Hard Disk/Drive.')
        print('Keep this disk as if the installation fails, you may see')
        print('what caused it.')
        print("")
        command()
    elif A == 'sdsys.exe':
                print("Sound system now enabled.To test,please do SDSYS.EXE /TEST")
                command()
    elif A == 'sdsys.exe /test':
                print("Sound driver test.")
                print('\a')
                command()
    elif A == 'sdsys.exe /info':
            print("SDSYS Sound System Company")
            print("A compatible card is detected.")
            print("Driver version 2.174")
            print("This card supports EAX,MIDI and SynthWave formats")
            print("Card on slot 4")
            print("Driver enabled at location 00AAFF22CC")
            command()
    elif A == 'A:':
            command()
    elif A == 'specifications':
            print("Querying required information...")
            time.sleep(5)
            print("System : VMPC V386-5XS 10mHz - Micro$oft Virtual Machine")
            print("Processor : intel i80386 16mHz")
            print("Memory Installed : 640kByte - 630kByte Usable")
            print("Hard Disk 0 : Not detected - Not installed")
            print("Floppy Disk 0 : Detected - Type 1 - TEAC FD-55GHR")
            time.sleep(3)
            print("Floppy Disk 1 : Detected - Type 4 - Not Usable : No Driver - TEAC FD-05HG")
            print("Querying PSU info...")
            time.sleep(2)
            print("PSU Capable : 250WT - OCP - OVP - SCP - FSC")
            print("Circuit Board : EffiPower,HighPerformaceVideoSlot,InteDriveCtr,AntiCorrupt")
            print("BIOS ver : 2.22.2")
            command()
    elif A == 'config /s':
            em = tk.Tk()
            em.withdraw()
            en = msgbox.showerror("DOS - Windows Virtual Machine","The following virtual machine has returned an unrecoverable error\n\nError details : \nSYSTEM_ACCESS_VIOLATION(0x0000005) has occured in WVM.EXE.Buffer of address 0F5A.\nThe virtual CPU has tried to access a part of memory that was not allocated.\nPossible reasons are bad drivers or the current machine is not capable of running this VM\n\nAny unsaved data was lost\nThe program will now exit.")
            exit()

    elif A == 'config /syste':
            fg = True
            print("General permission protection error reading drive A:")
            while fg == True:
                dk = input("[A]bort,[R]etry,[I]gnore,[F]ail?")
                if dk == "A":
                    fg = False
                    command()
                elif dk == "R" or dk == "I":
                    print("General permission protection error reading drive A:")
                elif dk == "F":
                    print("Fail on INT 24")
                    fg = False
                    command()
            command()
    elif A == 'winexec.exe':
            b = input("Enter any executable file name.The FULL file path must be included : ")
            os.system(b)
            command()
    elif A == '':
        command()
    elif A == 'stop':
        exit()
    elif A == 'exit':
        exit()
    elif A == 'B:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'C:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'D:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'E:':
        print('Invalid drive name specification.')
        command()
    elif A == 'F:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'G:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'H:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'I:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'J:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'K:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'L:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'M:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'N:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'O:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'P:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'Q:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'R:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'S:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'T:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'U:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'V:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'W:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'X:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'Y:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'Z:':
        print('Invalid drive name specification.')
        print("")
        command()
    elif A == 'windir.exe':
            print("****THE WINDOWS VIRTUAL MACHINE DIRECTORY****")
            print("Special driver has been loaded which allows full disk access for this session.")
            print("ATTENTION!THE DRIVER FILES ARE PROTECTED BY COPYRIGHT AND ANY COPYING WILL BE PUNISHED BY THE PROGRAM SELF DESTROYING AND PUNISHABLE BY LAW!")
            ld = input("DIR : ")
            dl = os.listdir(ld)
            print("Directory of " + ld)
            for x in range(len(dl)):
                if "." not in dl[x]:
                    print(dl[x] + "[DIR]")
                else:
                    print(dl[x])
            if ld == "A:" or ld == "a:":
                ld = "AB:"
            print("Driver now disabled." + ld + " no longer accessible from COMMAND.")
            command()
    elif A == 'wbytes.exe':
            db = input("Enter file to show BYTES : ")
            bn = input("Byte count(VALUE MUST BE SPECIFIED) : ")
            bn = int(bn)
            with open(db,"rb") as bd:
                cd = bd.read(bn)
            print(cd)
            command()
    elif A == 'chkdsk.exe':
            j = input("[Q]uick or [T]hourough check?(Any invalid option to abort) : ")
            if j == 'Q':
                for x in range(101):
                    print("Checking..." + str(x) + " percent done",end='\r')
                    time.sleep(0.1)
                print('\n')
                print("Use CHKDSK premium for more info.\n 360KByte in whole disk\nFile record\n338572 Bytes in USE\n21428 Free\n0Bad file records found.")
                command()
            elif j == 'T':
                for x in range(101):
                    print("Checking..." + str(x) + " percent done",end='\r')
                    time.sleep(2)
                print("Use CHKDSK premium for more info.\n 360KByte in whole disk\nFile record\n338572 Bytes in USE\n21428 Free\n0Bad file records found.")
                command()
    else:
        print('Invalid/not recognised command or file name.')
        print("")
        command()
boot()
