import tkinter as tk
from tkinter import ttk, messagebox

# Window
root = tk.Tk()
root.title("Weight Converter")
root.geometry("420x450")
root.resizable(False, False)

# Units (value in kg)
units = {
    "Kilogram (kg)": 1,
    "Gram (g)": 0.001,
    "Milligram (mg)": 0.000001,
    "Pound (lb)": 0.453592,
    "Ounce (oz)": 0.0283495,
    "Stone (st)": 6.35029,
    "Ton (metric)": 1000
}

# Convert function
def convert():
    try:
        value = float(entry_value.get())
        from_unit = from_unit_combo.get()
        selected_units = to_unit_listbox.curselection()

        if not selected_units:
            messagebox.showwarning("Warning", "Please select at least one unit")
            return

        kg = value * units[from_unit]

        result_text.delete("1.0", tk.END)

        for index in selected_units:
            unit_name = to_unit_listbox.get(index)
            result = kg / units[unit_name]
            result_text.insert(
                tk.END,
                f"{value} {from_unit} = {result:.4f} {unit_name}\n"
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# UI
tk.Label(root, text="Weight Converter",
         font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Enter Value").pack()
entry_value = tk.Entry(root, width=20)
entry_value.pack(pady=5)

tk.Label(root, text="From Unit").pack()
from_unit_combo = ttk.Combobox(
    root,
    values=list(units.keys()),
    state="readonly"
)
from_unit_combo.pack()
from_unit_combo.set("Kilogram (kg)")

tk.Label(root, text="Select To Units (Ctrl + Click)").pack(pady=5)

to_unit_listbox = tk.Listbox(
    root,
    selectmode=tk.MULTIPLE,
    height=6
)
for unit in units.keys():
    to_unit_listbox.insert(tk.END, unit)
to_unit_listbox.pack()

tk.Button(root, text="Convert",
          command=convert,
          width=15).pack(pady=10)

result_text = tk.Text(root, height=6, width=45)
result_text.pack(pady=5)

root.mainloop()
