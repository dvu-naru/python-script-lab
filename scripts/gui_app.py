import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=f"Count: {count}")

# Window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("250x150")

# Widgets
label = tk.Label(root, text="Count: 0", font=("Arial", 16))
label.pack(pady=10)

btn = tk.Button(root, text="Increase", command=increase)
btn.pack()

# Run
root.mainloop()
