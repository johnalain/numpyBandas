import tkinter as tk
from PIL import ImageTk
# initialize app
#https://youtu.be/5qOnzF7RsNA?list=PLlvFEn0NKwXKsfAM-mXulCXOtGvDKQs81
root = tk.Tk()
root.title('Recipe Picker')
#eval type at the center of screen and not at the extrem left
x = root.winfo_screenwidth()//2
y = int(root.winfo_screenheight()*0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

# root.eval("tk::PlaceWindow . center")
#create our first frame inside the window

frame1 = tk.Frame(root, width=500, height=600,bg='#3d6464')
#place the frame inside the window on the page
frame1.grid(row=0,column=0)

log_img = ImageTk.PhotoImage(file="/Users/michelkadi/Desktop/grocery-cart.png")
logo_widget = tk.Label(frame1,image=log_img)
logo_widget.image = log_img
logo_widget.pack()
#https://youtu.be/5qOnzF7RsNA?list=PLlvFEn0NKwXKsfAM-mXulCXOtGvDKQs81&t=570





frame2 = tk.Frame(root, width=500, height=600,bg='red')
#place the frame inside the window on the page
frame2.grid(row=0,column=1)



#run app
root.mainloop()