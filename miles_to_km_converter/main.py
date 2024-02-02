import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def convert():
    miles = float(input.get())
    km = 1.609344 * miles
    label_3["text"] = f"{km:0.2f}"

input = tkinter.Entry()
input.grid(column=0, row=0, columnspan=2)
input.insert(tkinter.END, string="0")
input.focus()

label_1 = tkinter.Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = tkinter.Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = tkinter.Label(text=0)
label_3.grid(column=1, row=1)

label_4 = tkinter.Label(text="Km")
label_4.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=0, row=2, columnspan=3)

tkinter.mainloop()