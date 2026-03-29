import tkinter as tk
from tkinter import messagebox

# -------- FUNCTIONS --------
def calculate():
    try:
        basic = float(entry_basic.get())
        overtime = float(entry_overtime.get())
        other = float(entry_other.get())

        gross = basic + overtime + other
        tax = gross * 0.10
        pension = gross * 0.05
        net = gross - (tax + pension)

        var_gross.set(f"{gross:.2f}")
        var_tax.set(f"{tax:.2f}")
        var_pension.set(f"{pension:.2f}")
        var_net.set(f"{net:.2f}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

def save_data():
    try:
        name = entry_name.get()
        address = entry_address.get()
        post = entry_post.get()
        gender = entry_gender.get()

        basic = float(entry_basic.get())
        overtime = float(entry_overtime.get())
        other = float(entry_other.get())

        gross = basic + overtime + other
        tax = gross * 0.10
        pension = gross * 0.05
        net = gross - (tax + pension)

        with open("payroll_data.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Post Code: {post}\n")
            file.write(f"Gender: {gender}\n")
            file.write(f"Basic: {basic}\n")
            file.write(f"Overtime: {overtime}\n")
            file.write(f"Other: {other}\n")
            file.write(f"Gross: {gross}\n")
            file.write(f"Tax: {tax}\n")
            file.write(f"Pension: {pension}\n")
            file.write(f"Net: {net}\n")
            file.write("-"*30 + "\n")

        messagebox.showinfo("Saved", "Data saved successfully!")

    except:
        messagebox.showerror("Error", "Fill all fields correctly!")

def reset():
    for entry in entries:
        entry.delete(0, tk.END)

    var_gross.set("")
    var_tax.set("")
    var_pension.set("")
    var_net.set("")

def exit_app():
    root.destroy()

# -------- UI --------
root = tk.Tk()
root.title("Payroll Management System")
root.geometry("900x600")
root.configure(bg="lightgray")

# TITLE
tk.Label(root, text="Payroll Management System",
         font=("Arial", 20, "bold"),
         bg="lightgray").pack(pady=10)

# -------- FRAME 1 --------
frame1 = tk.LabelFrame(root, text="Employee Details", padx=10, pady=10)
frame1.pack(fill="x", padx=10, pady=5)

tk.Label(frame1, text="Employee Name").grid(row=0, column=0)
entry_name = tk.Entry(frame1, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame1, text="Address").grid(row=1, column=0)
entry_address = tk.Entry(frame1, width=30)
entry_address.grid(row=1, column=1)

tk.Label(frame1, text="Post Code").grid(row=0, column=2)
entry_post = tk.Entry(frame1)
entry_post.grid(row=0, column=3)

tk.Label(frame1, text="Gender").grid(row=1, column=2)
entry_gender = tk.Entry(frame1)
entry_gender.grid(row=1, column=3)

# -------- FRAME 2 --------
frame2 = tk.LabelFrame(root, text="Salary Details", padx=10, pady=10)
frame2.pack(fill="x", padx=10, pady=5)

tk.Label(frame2, text="Basic Salary").grid(row=0, column=0)
entry_basic = tk.Entry(frame2)
entry_basic.grid(row=0, column=1)

tk.Label(frame2, text="Over Time").grid(row=1, column=0)
entry_overtime = tk.Entry(frame2)
entry_overtime.grid(row=1, column=1)

tk.Label(frame2, text="Other Payment").grid(row=2, column=0)
entry_other = tk.Entry(frame2)
entry_other.grid(row=2, column=1)

# -------- FRAME 3 --------
frame3 = tk.LabelFrame(root, text="Salary Output", padx=10, pady=10)
frame3.pack(fill="x", padx=10, pady=5)

var_gross = tk.StringVar()
var_tax = tk.StringVar()
var_pension = tk.StringVar()
var_net = tk.StringVar()

tk.Label(frame3, text="Gross Pay").grid(row=0, column=0)
tk.Entry(frame3, textvariable=var_gross).grid(row=0, column=1)

tk.Label(frame3, text="Tax").grid(row=1, column=0)
tk.Entry(frame3, textvariable=var_tax).grid(row=1, column=1)

tk.Label(frame3, text="Pension").grid(row=2, column=0)
tk.Entry(frame3, textvariable=var_pension).grid(row=2, column=1)

tk.Label(frame3, text="Net Pay").grid(row=3, column=0)
tk.Entry(frame3, textvariable=var_net).grid(row=3, column=1)

# -------- BUTTONS --------
frame_btn = tk.Frame(root, bg="lightgray")
frame_btn.pack(pady=20)

tk.Button(frame_btn, text="Calculate", width=15, command=calculate).grid(row=0, column=0, padx=10)
tk.Button(frame_btn, text="Reset", width=15, command=reset).grid(row=0, column=1, padx=10)
tk.Button(frame_btn, text="Save", width=15, command=save_data).grid(row=0, column=2, padx=10)
tk.Button(frame_btn, text="Exit", width=15, command=exit_app).grid(row=0, column=3, padx=10)

# Store entries
entries = [entry_name, entry_address, entry_post, entry_gender,
           entry_basic, entry_overtime, entry_other]

root.mainloop()