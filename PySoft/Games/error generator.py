try:
    def b1():
        pass
    def b2():
        pass
    def u1():
        choices[1] = buttonsoricons[0]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u2():
        choices[1] = buttonsoricons[1]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u3():
        choices[1] = buttonsoricons[2]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u4():
        choices[1] = buttonsoricons[3]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u5():
        choices[1] = buttonsoricons[4]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u6():
        choices[1] = buttonsoricons[5]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u7():
        choices[1] = buttonsoricons[6]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u8():
        choices[1] = buttonsoricons[7]
        x = messagebox.showinfo("Info","Complete.")
        return
    def i3():
        try:
            choices[6] = icons[0]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[0])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i5():
        try:
            choices[6] = icons[1]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[1])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i7():
        try:
            choices[6] = icons[2]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[2])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i9():
        try:
            choices[6] = icons[3]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[3])
            x = messagebox.showinfo("Info","Complete.")
            return
    def gen(titl,mst) -> None:
            windows.withdraw()
            if buttonsoricons[0] == choices[1]:
                z = messagebox.showerror(titl,mst)
                windows.deiconify()
                return
            elif buttonsoricons[1] == choices[1]:
                z = messagebox.showwarning(titl,mst)
                windows.deiconify()
                return
            elif buttonsoricons[2] == choices[1]:
                z = messagebox.showinfo(titl,mst)
                windows.deiconify()
                return
            elif buttonsoricons[3] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error",'Required parameter missing. Please use the "About & How" to use button for more information.')
                    windows.deiconify()
                    return  
            elif buttonsoricons[4] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error",'Required parameter missing. Please use the "About & How" to use button for more information.')
                    windows.deiconify()
                    return  
            elif buttonsoricons[5] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error",'Required parameter missing. Please use the "About & How" to use button for more information.')
                    windows.deiconify()
                    return  
            elif buttonsoricons[6] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error",'Required parameter missing. Please use the "About & How" to use button for more information.')
                    windows.deiconify()
                    return  
            elif buttonsoricons[7] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error",'Required parameter missing. Please use the "About & How" to use button for more information.')
                    windows.deiconify()
                    return  
            else:
                z = messagebox.showerror("Error",'Required parameter missing. Please use the "About & How" to use button for more information.')
                windows.deiconify()
                return
    def about_how():
        x = messagebox.showinfo("About & How","This is a error generator that can generate as many *fake* error messages that you can personalise as you want.\n\nMake sure to choose either a MSGBOX or ICON button first before typing your title and error message. Generation might fail if this is not respected.")
        return
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
    sample = messagebox
    buttonsoricons = ["showerror","showwarning","showinfo","askokcancel","askquestion","askretrycancel","askyesno","askyesnocancel"]
    icons = ["messagebox.ERROR","messagebox.INFO","messagebox.WARNING","messagebox.QUESTION"]
    choices = ["messagebox.","","(","",",",""]
    windows = Tk()
    windows.geometry("1900x1080")
    x = messagebox.showinfo("Info","© 2023 Okmeque1 Corporation, Github: https://github.com/Okmeque1/software/blob/main/PythonSoft/GUI/error%20generator.py")
    windows.title("Error message generator")
    l1 = Label(windows,text="Title: ")
    TString = Entry(windows,width=40)
    l2 = Label(windows,text="Error message: ")
    MSGString = Entry(windows,width=40)
    ErrorOk = Button(windows,text="MSGBOX: Show Error",command=u1,width=40)
    WarningOk = Button(windows,text="MSGBOX: Show Warning",command=u2,width=40)
    InfoOk = Button(windows,text="MSGBOX: Show Info",command=u3,width=40)
    okcan = Button(windows,text="MSGBOX: Buttons OK and CANCEL",command=u4,width=40)
    ques = Button(windows,text="MSGBOX: Question",command=u5,width=40)
    racecar = Button(windows,text="MSGBOX: Buttons RETRY and CANCEL",command=u6,width=40)
    yesrefuse = Button(windows,text="MSGBOX: Buttons YES and NO",command=u7,width=40)
    yescancelno = Button(windows,text="MSGBOX: Buttons YES, NO and CANCEL",command=u8,width=40)
    blank1 = Button(windows,text="------------------------------------------------------",command=b1,width=40)
    useerroricon = Button(windows,text="Use: ERROR icon",command=i3,width=40)
    useinfoicon = Button(windows,text="Use: INFO icon",command=i5,width=40)
    usewarningicon = Button(windows,text="Use: WARNING icon",command=i7,width=40)
    usequestionicon = Button(windows,text="Use: QUESTION icon",command=i9,width=40)
    blank2 = Button(windows,text="------------------------------------------------------",command=b2,width=40)
    generate = Button(windows,text="Generate error message!",command=lambda: gen(TString.get(),MSGString.get()),width=40)
    log = Button(windows,text="About & How",command=about_how,width=40)
    l1.pack()
    TString.pack()
    l2.pack()
    MSGString.pack()
    ErrorOk.pack()
    WarningOk.pack()
    InfoOk.pack()
    okcan.pack()
    ques.pack()
    racecar.pack()
    yesrefuse.pack()
    yescancelno.pack()
    blank1.pack()
    useerroricon.pack()
    useinfoicon.pack()
    usewarningicon.pack()
    usequestionicon.pack()
    blank2.pack()
    generate.pack()
    log.pack()
    windows.mainloop()

except FileExistsError:
    exit()
except FileNotFoundError:
    exit()
except OSError:
    exit()
except ValueError:
    exit()
except KeyboardInterrupt:
    exit()
except EOFError:
    exit()
except BaseException:
    x = messagebox.showerror("Error","This program has encountered an error and needs to close.\nError code : 770A")
    exit()
except IOError:
    exit()
except:
    exit()
