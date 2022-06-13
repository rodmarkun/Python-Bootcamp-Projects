import tkinter

window = tkinter.Tk()
window.title("Miles to Km converter")

# Miles Entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)

# Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

# Button
def miles_to_km() -> None:
    result_label.config(text=str(float(miles_input.get()) * 1.60934))


calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()