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
        tax = gross * 0.1
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
            file.write("-" * 30 + "\n")

        messagebox.showinfo("Saved", "Data saved successfully!")

    except:
        messagebox.showerror("Error", "Fill all fields correctly!")
