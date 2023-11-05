import tkinter as tk

def calculate_mortgage():
    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100.0
    years = int(years_entry.get())
    
    monthly_interest_rate = interest_rate / 12
    months = years * 12
    
    mortgage_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** months) / (((1 + monthly_interest_rate) ** months) - 1)
    result_label.config(text=f"Monthly Mortgage Payment: ${mortgage_payment:.2f}")

# Create the main window
root = tk.Tk()
root.title("Wolfrank's Mortgage Calculator")
root.geometry("400x200")
root.configure(bg="black")

# Create labels
principal_label = tk.Label(root, text="Principal Amount ($):", bg="black", fg="white")
interest_rate_label = tk.Label(root, text="APR (%):", bg="black", fg="white")
years_label = tk.Label(root, text="Duration:", bg="black", fg="white")
result_label = tk.Label(root, text="", bg="black", fg="white")

# Create entry widgets
principal_entry = tk.Entry(root)
interest_rate_entry = tk.Entry(root)
years_entry = tk.Entry(root)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_mortgage, bg="white", fg="black")

# Grid layout
principal_label.grid(row=0, column=0, padx=10, pady=10)
principal_entry.grid(row=0, column=1, padx=10, pady=10)
interest_rate_label.grid(row=1, column=0, padx=10, pady=10)
interest_rate_entry.grid(row=1, column=1, padx=10, pady=10)
years_label.grid(row=2, column=0, padx=10, pady=10)
years_entry.grid(row=2, column=1, padx=10, pady=10)
calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
