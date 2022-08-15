from tkinter import *

window = Tk()
window.title(string="Mile to Km Converter")
window.config(padx=20, pady=20)


def calculate_mile_to_km():
    miles = float(entry_mile.get())
    km = miles * 1.609344
    label_km_result.config(text=f"{km:.3f}")


# Entry Mile value
entry_mile = Entry(width=10)
entry_mile.insert(END, string="0")
entry_mile.focus()
entry_mile.grid(column=1, row=0)

# Label Miles measure
label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

# Label is equal to
label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(column=0, row=1)

# Label km result
label_km_result = Label(text="0")
label_km_result.grid(column=1, row=1)
label_km_result.config(padx=10, pady=10)

# Label Km measure
label_km = Label(text="Km")
label_km.grid(column=2, row=1)

# Button calculate
button_calculate = Button(text="Calculate", command=calculate_mile_to_km)
button_calculate.grid(column=1, row=2)

window.mainloop()

