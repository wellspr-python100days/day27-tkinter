import tkinter

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

def click_button():
    print("click!")
    label["text"] = input.get()

input = tkinter.Entry()
input.grid(column=0, row=0)

button_1 = tkinter.Button(text="Click", command=click_button)
button_1.grid(column=1, row=1)

button_2 = tkinter.Button(text="Click me too", command=click_button)
button_2.grid(column=2, row=0)

label = tkinter.Label(text="Hello world!", font=("Arial", 20, "bold"))
label.grid(column=3, row=3, columnspan=4, )


window.mainloop()