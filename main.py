from tkinter import *
from tkinter import messagebox
from support import support

root = Tk()

# Set title
root.title("YearPix Organizer")
root.geometry('350x150')
root.eval('tk::PlaceWindow . center')

def onClick():
   flag = support.select_path()
   if flag:
      display_location["text"] = flag
      # select_location["state"] = "disabled"
      select_location["text"] = "Change Location"
      start["state"] = "active"
   else:
      pass
   
def check_process():
      flag = support.sortImages()
      if flag:
         messagebox.showinfo('Info', 'Process completed')
         display_location["text"] = ""
         select_location["text"] = "Add Location"
         start["state"] = "disabled"
      else:
         messagebox.showinfo('Info', 'Try Again!')
   

title = Label(root, text="Turning Chaos into Visual Harmony!")
title.pack(pady=5)

display_location = Label(root,text="",borderwidth=1,relief="solid",width=30)
display_location.pack(padx=5,pady=5)

select_location= Button(root, text="Add Location",command=onClick)
select_location.pack(ipadx=5, pady=5)

start= Button(root, text="start",state="disabled",command=check_process)
start.pack(ipadx=5, pady=7)


root.mainloop()