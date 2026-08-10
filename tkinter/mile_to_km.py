from tkinter import *

def mile_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_lable.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_lable = Label(text="Miles")
miles_lable.grid(column=2, row=0)

is_equal_lable = Label(text=f"is equal to")
is_equal_lable.grid(column= 0, row= 1)

kilometer_result_lable = Label(text="0")
kilometer_result_lable.grid(column=1, row=1 )

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

cal_button = Button(text="Calculate", command=mile_km)
cal_button.grid(column=1, row=2)

window.mainloop()