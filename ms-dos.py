from os import system

print('MS-DOS Version 4.10.0')
print('Hard Disk/Drive or and 2nd floppy not detected')
def command():
    A = input('A:>')
    if A == 'dir':
        print('Volume label is BootDisk')
        print('Directory of A:')
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
        command()
    elif A == 'fdisk.exe':
        print('No fixed disks presents')
        command()
    elif A == 'format.com':
        for h in range(11):
            print('Formatting track' + str(h))
    elif A == 'autoexec.bat':
        command()
    elif A == 'command.com':
        command()
    elif A == 'edit.com':
        print('EDIT VERSION 1.00')
        print('1 → Add value for  File')
        print('2 → Replace value for file')
        print('3 → Erase file')
        print('4 → List file')
        B = input('Choose an option(any invalid option to quit to DOS).')
        C = int(B)
        file = ''
        if C == 1:
            while write == True:
                d = input('Write anything you want.Type eX1t to quit to DOS')
                file += d
                if d == 'eX1t':
                    write = False
                    file += d
                    command()
                elif d == 'c0Mn4mD':
                    write = False
                    command()
        if C == 2:
            while write == True:
                print('Please note that this option will wipe any existing file.')
                d = input('Write anything you want.Type eX1t to quit to DOS.Type c0Mn4mD to exit without save')
                file = d
                if d == 'eX1t':
                    write = False
                    file = d
                    command()
                elif d == 'c0Mn4mD':
                    write = False
                    command
        if C == 3:
            e = input('This option is IRREVERSIBLE.Type eR45€ to erase the file.')
            f = input('This option is IRREVERSIBLE.Type Er8s£ to erase the file.')
            if e == 'eR45€' and f == 'Er8s£':
                file = ''
                command()
        if C == 4:
            if file = '':
                print('File empty.Quitting NOW...')
            else:
                print(file)
                command()
        else:
            command()
    elif A == 'xcopy.exe':
        print('No other drives or disks have been detected. This includes Hard Disks/Drives, or other floppy disks')
        command()
    elif A == 'copy':
        print('Sorry, this disk is write-protected (Read-only) and cannot be copied.')
        command()
    elif A == 'ver':
        print('MS-DOS 4.10.0')
        command()
    elif A == 'version':
        print('MS-DOS 4.10.0')
        command()
    elif A == 'Software024':
        print('Software024 and Okmeque1 MS-DOS 4.10.0 running on 8TB A: Drive.')
        print('Software024 is the co-creator of MS-DOS')
        command()
    elif A == 'Okmeque1':
        print('Okmeque1 and Software024 MS-DOS 4.10.0 running on 8TB A: Drive.')
        print('Okmeque1 is the creator of MS-DOS')
        command()
    elif A == 'specs':
        print('8.74 GHz/s IBM at: 64GB RAM.')
        command()
    elif A == 'specifications':
        print('8.74 GHz/s IBM at: 64GB RAM.')
        command()
    elif A == 'help':
        print('fdisk.exe : Fixed disk utility')
        print('edit.com : Edits text files')
        print('stop : Stops the whole computer')
        print('ver : Shows the current version')
        print('format.com : Formats any disks or drives')
        print('dir : Lists directory')
        print('specs : Shows the specifications of the computer')
        print('')
        print('Note : This version of DOS is a bootdisk and only contains')
        print('minimal commands.To have more commands,eject this disk    ')
        print('and insert an installer disk. Then hold CTRL + ALT and then')
        print('press DELETE/DEL/SUPPR. You need a Hard Disk/Drive. Keep this disk as if the')
        print('installation fails, you may see what caused it.            ')
        command()

    elif A == '':
        command()
    elif A == 'stop':
        return 'Stopped this machine' 
    elif A == 'exit':
        return 'Stopped this machine' 
    elif A == 'B:':
        print('Invalid drive name specification')
        command()
    elif A == 'C:':
        print('Invalid drive name specification')
        command()
    elif A == 'D:':
        print('Invalid drive name specification')
        command()
    elif A == 'E:':
        print('Invalid drive name specification')
        command()
    elif A == 'F:':
        print('Invalid drive name specification')
        command()
    elif A == 'G:':
        print('Invalid drive name specification')
        command()
    elif A == 'H:':
        print('Invalid drive name specification')
        command()
    elif A == 'I:':
        print('Invalid drive name specification')
        command()
    elif A == 'J:':
        print('Invalid drive name specification')
        command()
    elif A == 'K:':
        print('Invalid drive name specification')
        command()
    elif A == 'L:':
        print('Invalid drive name specification')
        command()
    elif A == 'M:':
        print('Invalid drive name specification')
        command()
    elif A == 'N:':
        print('Invalid drive name specification')
        command()
    elif A == 'O:':
        print('Invalid drive name specification')
        command()
    elif A == 'P:':
        print('Invalid drive name specification')
        command()
    elif A == 'Q:':
        print('Invalid drive name specification')
        command()
    elif A == 'R:':
        print('Invalid drive name specification')
        command()
    elif A == 'S:':
        print('Invalid drive name specification')
        command()
    elif A == 'T:':
        print('Invalid drive name specification')
        command()
    elif A == 'U:':
        print('Invalid drive name specification')
        command()
    elif A == 'V:':
        print('Invalid drive name specification')
        command()
    elif A == 'W:':
        print('Invalid drive name specification')
        command()
    elif A == 'X:':
        print('Invalid drive name specification')
        command()
    elif A == 'Y:':
        print('Invalid drive name specification')
        command()
    elif A == 'Z:':
        print('Invalid drive name specification')
        command()
    else:
        print('Invalid/Not recognised command or file name;')
        command()
    
command()
