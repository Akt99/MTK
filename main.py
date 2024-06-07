from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())

    km = miles * 1.609

    kilometer_result_label.config(text=f"{km} ")


window = Tk()

window.title("Miles to Kilometer Convertor")

window.config(padx=20, pady=20)

window.configure(background='#0096DC')

window.minsize(100, 100)

window.maxsize(1000, 1000)

window.geometry('400x600')

miles_input = Entry()

miles_input.grid(column=3, row=0)

miles_label = Label(text="Miles")

miles_label.grid(column=5, row=0)

is_equal_label = Label(text="is equal to")

is_equal_label.grid(column=2, row=6)

is_equal_label.configure(background='#0096DC')

kilometer_result_label = Label(text="0 ")

kilometer_result_label.grid(column=3, row=6)

kilometer_label = Label(text="km")

kilometer_label.grid(column=4, row=6)

calculate_button = Button(text="CALCULATE", command=miles_to_km)

calculate_button.grid(column=3, row=7)

window.mainloop()