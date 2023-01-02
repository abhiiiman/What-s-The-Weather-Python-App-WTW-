from tkinter import *

def quit_window():  
   global opened
   window.destroy()
   opened = False
   main.deiconify()

def return_main(): 
    global opened 
    window.withdraw()
    opened = True
    print(opened)
    main.deiconify()

def launch():
    global opened, window
    print(opened)
    # main.withdraw()  # withdraw main instead of destroying it
    if opened == True:
        window.deiconify()
    else:
        window = Toplevel(main) 
        breturn = Button(window, text="Return", command=return_main).pack()
        bquit = Button(window, text="Quit", command=quit_window).pack()   

main = Tk()  
bopen = Button(main, text="Open", command=launch).pack() 
opened = False 
main.mainloop()