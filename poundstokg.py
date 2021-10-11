# Python 3 Pounds to Kg weight Converter
# Write a Python GUI program
# using tkinter module
# to input pounds in Entry
# text box widget and convert
# to Kilograms on button click. 

from  tkinter import *

def main():
    window= Tk()
    window.title("Pounds to Kilograms Converter")
    window.geometry("450x230")
    label_easycodebook1 = Label(text="Python 3 Pounds to Kilograms Converter",
                           bg='lightgreen',font=('verdana',10))

    label_easycodebook1.place(x=25,y=5) 
    
    # create a label with text Enter Pounds
    label1 = Label(window, text="Enter Pounds:")
    
    # create a label with text Kilograms
    label2 = Label(window, text="Kilograms:")

    # place label1 in window at position x,y 
    label1.place(x=50,y=30)

    # create an Entry widget (text box) 
    #kilo = tk.StringVar()
    textbox1 = Entry(window, width=12)

    # place textbox1 in window at position x,y 
    textbox1.place(x=200,y=35)
    

    # place label2 in window at position x,y 
    label2.place(x=50,y=100)
    
    # create a label3 with empty text:
    label3 = Label(window, text=" ")

    # place label3 in window at position x,y 
    label3.place(x=180,y=100)

         
    def btn1_click():
        pounds = round(float(textbox1.get()) / 2.20462,2)
        label3.configure(text = str(pounds)+ '  Pounds')
        

    # create a button with text Button 1
    btn1 = Button(window, text="Click Me To Convert Lbs to Kg", command=btn1_click)
    # place this button in window at position x,y 
    btn1.place(x=90,y=150)

    label_easycodebook = Label(text="www.EasyCodeBook.com for Python GUI Tutorials",
                           bg='lightgreen',font=('verdana',10))

    label_easycodebook.place(x=5,y=200) 
    window.mainloop()
    

main()
