
# 01 - Basic Window Creation using Tkinter

"""
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter Window")

# Set window size (width x height)
root.geometry("400x300")

# Set background color
root.configure(bg="#f0f4f8")

# Add a Label widget
label = tk.Label(
    root,
    text="Welcome to Tkinter GUI!",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
)
label.pack(pady=60)

# Add a sub-label
sub_label = tk.Label(
    root,
    text="This is your first Python GUI window.",
    font=("Arial", 11),
    bg="#f0f4f8",
    fg="#7f8c8d"
)
sub_label.pack()

# Add a Quit button
quit_btn = tk.Button(
    root,
    text="Close Window",
    command=root.destroy,
    font=("Arial", 11),
    bg="#e74c3c",
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
    cursor="hand2"
)
quit_btn.pack(pady=40)

# Start the event loop
root.mainloop()
"""

# 02 - Labels and Buttons Demo
"""


import tkinter as tk

def change_text():
    label.config(text="Button was Clicked!", fg="#27ae60")

def reset_text():
    label.config(text="Hello, Tkinter!", fg="#2c3e50")

def change_color():
    current = root.cget("bg")
    root.configure(bg="#dfe6e9" if current == "#f0f4f8" else "#f0f4f8")
    label.configure(bg=root.cget("bg"))
    btn_frame.configure(bg=root.cget("bg"))

root = tk.Tk()
root.title("Labels and Buttons")
root.geometry("420x300")
root.configure(bg="#f0f4f8")

# Label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 20, "bold"),
                 bg="#f0f4f8", fg="#2c3e50", pady=30)
label.pack()

# Button frame
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Click Me",    command=change_text,  font=("Arial", 11),
          bg="#3498db", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").grid(row=0, column=0, padx=8)

tk.Button(btn_frame, text="Reset",       command=reset_text,   font=("Arial", 11),
          bg="#95a5a6", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)

tk.Button(btn_frame, text="Toggle BG",   command=change_color, font=("Arial", 11),
          bg="#9b59b6", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").grid(row=0, column=2, padx=8)

tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 11),
          bg="#e74c3c", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").pack(pady=20)

root.mainloop()
"""

# 03 - Entry Widget - Taking User Input
"""


import tkinter as tk
from tkinter import messagebox

def greet():
    name = name_entry.get().strip()
    age  = age_entry.get().strip()
    if not name or not age:
        messagebox.showwarning("Missing Input", "Please enter both name and age.")
        return
    if not age.isdigit():
        messagebox.showerror("Invalid Input", "Age must be a number.")
        return
    result_label.config(text=f"Hello, {name}! You are {age} years old.", fg="#27ae60")

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Entry Widget Demo")
root.geometry("420x320")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="User Input Form", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=15)

frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(pady=5)

# Name field
tk.Label(frame, text="Name :", font=("Arial", 12), bg="#f8f9fa", width=8, anchor="e").grid(row=0, column=0, pady=8, padx=5)
name_entry = tk.Entry(frame, font=("Arial", 12), width=22, relief="solid", bd=1)
name_entry.grid(row=0, column=1, pady=8)

# Age field
tk.Label(frame, text="Age  :", font=("Arial", 12), bg="#f8f9fa", width=8, anchor="e").grid(row=1, column=0, pady=8, padx=5)
age_entry = tk.Entry(frame, font=("Arial", 12), width=22, relief="solid", bd=1)
age_entry.grid(row=1, column=1, pady=8)

# Buttons
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Greet",  command=greet,        font=("Arial", 11), bg="#3498db", fg="white",
          padx=14, pady=6, relief="flat", cursor="hand2").grid(row=0, column=0, padx=8)
tk.Button(btn_frame, text="Clear",  command=clear_fields, font=("Arial", 11), bg="#95a5a6", fg="white",
          padx=14, pady=6, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)

result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#f8f9fa", fg="#2c3e50")
result_label.pack(pady=10)

root.mainloop()
"""

# 04 - Simple Calculator
"""


import tkinter as tk
from tkinter import messagebox

def button_click(value):
    current = display_var.get()
    if value == "C":
        display_var.set("")
    elif value == "⌫":
        display_var.set(current[:-1])
    elif value == "=":
        try:
            result = eval(current)
            # Format: remove trailing zeros for floats
            if isinstance(result, float) and result == int(result):
                result = int(result)
            display_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            display_var.set("")
        except Exception:
            messagebox.showerror("Error", "Invalid expression!")
            display_var.set("")
    else:
        display_var.set(current + str(value))

root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#2c3e50")
root.resizable(False, False)

display_var = tk.StringVar()

# Display
display = tk.Entry(root, textvariable=display_var, font=("Arial", 22, "bold"),
                   justify="right", bd=0, bg="#34495e", fg="white",
                   insertbackground="white", relief="flat")
display.pack(fill="x", padx=15, pady=(20, 10), ipady=14)

# Button layout
buttons = [
    ["C",  "⌫",  "%",  "/"],
    ["7",  "8",  "9",  "*"],
    ["4",  "5",  "6",  "-"],
    ["1",  "2",  "3",  "+"],
    ["00", "0",  ".",  "="],
]

btn_colors = {
    "=": "#27ae60", "C": "#e74c3c", "": "#e67e22",
    "/": "#8e44ad", "*": "#8e44ad", "-": "#8e44ad", "+": "#8e44ad", "%": "#8e44ad",
}

btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(padx=15, pady=5, fill="both", expand=True)

for row_vals in buttons:
    row_frame = tk.Frame(btn_frame, bg="#2c3e50")
    row_frame.pack(fill="x", pady=3)
    for val in row_vals:
        color = btn_colors.get(val, "#ecf0f1")
        fg    = "white" if val in btn_colors else "#2c3e50"
        tk.Button(row_frame, text=val,
                  command=lambda v=val: button_click(v),
                  font=("Arial", 14, "bold"),
                  bg=color, fg=fg,
                  width=5, height=2,
                  relief="flat", cursor="hand2",
                  activebackground="#bdc3c7").pack(side="left", padx=3)

root.mainloop()
"""

# 05 - Login Form with Validation
"""


import tkinter as tk
from tkinter import messagebox

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    username = user_entry.get().strip()
    password = pass_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Empty Fields", "Please enter both username and password.")
        return
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {username}! Login successful.")
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        pass_entry.delete(0, tk.END)

def toggle_password():
    if pass_entry.cget("show") == "*":
        pass_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        pass_entry.config(show="*")
        show_btn.config(text="Show")

def clear_form():
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Login Form")
root.geometry("380x380")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

# Header
tk.Label(root, text="Login", font=("Arial", 20, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=25)

# Form frame
frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

# Username
tk.Label(frame, text="Username:", font=("Arial", 12), bg="#f0f4f8", anchor="w",
         width=10).grid(row=0, column=0, pady=10, sticky="w")
user_entry = tk.Entry(frame, font=("Arial", 12), width=20, relief="solid", bd=1)
user_entry.grid(row=0, column=1, columnspan=2, pady=10)

# Password
tk.Label(frame, text="Password:", font=("Arial", 12), bg="#f0f4f8", anchor="w",
         width=10).grid(row=1, column=0, pady=10, sticky="w")
pass_entry = tk.Entry(frame, font=("Arial", 12), width=15, relief="solid", bd=1, show="*")
pass_entry.grid(row=1, column=1, pady=10)
show_btn = tk.Button(frame, text="Show", command=toggle_password, font=("Arial", 9),
                     bg="#bdc3c7", relief="flat", cursor="hand2", width=5)
show_btn.grid(row=1, column=2, padx=5)

# Hint
tk.Label(root, text="Hint: admin / 1234", font=("Arial", 9, "italic"),
         bg="#f0f4f8", fg="#95a5a6").pack()

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="Login",  command=login,      font=("Arial", 12), bg="#27ae60",
          fg="white", padx=16, pady=7, relief="flat", cursor="hand2").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear",  command=clear_form, font=("Arial", 12), bg="#95a5a6",
          fg="white", padx=16, pady=7, relief="flat", cursor="hand2").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Cancel", command=root.destroy, font=("Arial", 12), bg="#e74c3c",
          fg="white", padx=16, pady=7, relief="flat", cursor="hand2").grid(row=0, column=2, padx=10)

user_entry.focus()
root.mainloop()
"""

# 06 - Registration Form
"""


import tkinter as tk
from tkinter import messagebox, ttk

def register():
    name    = name_entry.get().strip()
    email   = email_entry.get().strip()
    phone   = phone_entry.get().strip()
    gender  = gender_var.get()
    course  = course_combo.get()
    password = pass_entry.get().strip()
    confirm  = confirm_entry.get().strip()

    if not all([name, email, phone, gender, course, password, confirm]):
        messagebox.showwarning("Incomplete", "Please fill in all fields.")
        return
    if "@" not in email or "." not in email:
        messagebox.showerror("Invalid", "Please enter a valid email address.")
        return
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Invalid", "Phone must be 10 digits.")
        return
    if password != confirm:
        messagebox.showerror("Mismatch", "Passwords do not match.")
        return

    info = (f"Name   : {name}\nEmail  : {email}\nPhone  : {phone}\n"
            f"Gender : {gender}\nCourse : {course}")
    messagebox.showinfo("Registered!", f"Registration Successful!\n\n{info}")

def clear_form():
    for widget in [name_entry, email_entry, phone_entry, pass_entry, confirm_entry]:
        widget.delete(0, tk.END)
    gender_var.set("")
    course_combo.set("")

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("460x540")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="📋 Student Registration", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=15)

frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(pady=5)

def make_row(parent, label, row, widget_fn):
    tk.Label(parent, text=label, font=("Arial", 11), bg="#f8f9fa",
             anchor="e", width=14).grid(row=row, column=0, pady=7, padx=5, sticky="e")
    w = widget_fn(parent)
    w.grid(row=row, column=1, pady=7, sticky="w")
    return w

name_entry    = make_row(frame, "Full Name :",    0, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1))
email_entry   = make_row(frame, "Email :",        1, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1))
phone_entry   = make_row(frame, "Phone :",        2, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1))

# Gender (Radio buttons)
tk.Label(frame, text="Gender :", font=("Arial", 11), bg="#f8f9fa",
         anchor="e", width=14).grid(row=3, column=0, pady=7, sticky="e")
gender_var = tk.StringVar()
gender_frame = tk.Frame(frame, bg="#f8f9fa")
gender_frame.grid(row=3, column=1, sticky="w")
for g in ["Male", "Female", "Other"]:
    tk.Radiobutton(gender_frame, text=g, variable=gender_var, value=g,
                   font=("Arial", 11), bg="#f8f9fa").pack(side="left", padx=4)

# Course (Combobox)
tk.Label(frame, text="Course :", font=("Arial", 11), bg="#f8f9fa",
         anchor="e", width=14).grid(row=4, column=0, pady=7, sticky="e")
course_combo = ttk.Combobox(frame, font=("Arial", 11), width=22, state="readonly",
                             values=["B.Sc CS", "BCA", "B.Tech", "MCA", "M.Sc CS"])
course_combo.grid(row=4, column=1, sticky="w")

pass_entry    = make_row(frame, "Password :",     5, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1, show="*"))
confirm_entry = make_row(frame, "Confirm Pass :", 6, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1, show="*"))

# Buttons
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=15)
tk.Button(btn_frame, text="Register", command=register,   font=("Arial", 12), bg="#27ae60",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear",    command=clear_form, font=("Arial", 12), bg="#95a5a6",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Exit",     command=root.destroy, font=("Arial", 12), bg="#e74c3c",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=2, padx=10)

root.mainloop()
"""

# 07 - MessageBox and Dialog Demos
"""


import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser, filedialog

root = tk.Tk()
root.title("MessageBox & Dialog Demo")
root.geometry("420x480")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

result_var = tk.StringVar(value="Result will appear here...")

tk.Label(root, text="Dialog Box Examples", font=("Arial", 15, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=15)

def show_info():
    messagebox.showinfo("Information", "This is an Information dialog box.")
    result_var.set("Showed: Info dialog")

def show_warning():
    messagebox.showwarning("Warning", "This is a Warning dialog box!")
    result_var.set("Showed: Warning dialog")

def show_error():
    messagebox.showerror("Error", "This is an Error dialog box!")
    result_var.set("Showed: Error dialog")

def ask_yesno():
    ans = messagebox.askyesno("Question", "Do you like Python?")
    result_var.set(f"Yes/No Answer: {'Yes' if ans else 'No'}")

def ask_okcancel():
    ans = messagebox.askokcancel("Confirm", "Proceed with the action?")
    result_var.set(f"OK/Cancel Answer: {'OK' if ans else 'Cancel'}")

def ask_input():
    val = simpledialog.askstring("Input", "Enter your name:")
    result_var.set(f"Input received: {val}" if val else "Input cancelled")

def pick_color():
    color = colorchooser.askcolor(title="Choose a Color")
    if color[1]:
        result_label.config(bg=color[1])
        result_var.set(f"Color chosen: {color[1]}")

def open_file():
    filepath = filedialog.askopenfilename(title="Open File",
               filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")])
    result_var.set(f"File: {filepath}" if filepath else "No file selected")

# Buttons
btn_cfg = {"font": ("Arial", 11), "fg": "white", "padx": 10, "pady": 6,
           "relief": "flat", "cursor": "hand2", "width": 18}

tk.Button(root, text="Show Info",       command=show_info,    bg="#3498db", **btn_cfg).pack(pady=4)
tk.Button(root, text="Show Warning",    command=show_warning, bg="#f39c12", **btn_cfg).pack(pady=4)
tk.Button(root, text="Show Error",      command=show_error,   bg="#e74c3c", **btn_cfg).pack(pady=4)
tk.Button(root, text="Yes / No",         command=ask_yesno,   bg="#27ae60", **btn_cfg).pack(pady=4)
tk.Button(root, text="OK / Cancel",     command=ask_okcancel, bg="#8e44ad", **btn_cfg).pack(pady=4)
tk.Button(root, text="Input Dialog",    command=ask_input,    bg="#16a085", **btn_cfg).pack(pady=4)
tk.Button(root, text="Color Chooser",  command=pick_color,   bg="#d35400", **btn_cfg).pack(pady=4)
tk.Button(root, text="Open File",       command=open_file,   bg="#2980b9", **btn_cfg).pack(pady=4)

result_label = tk.Label(root, textvariable=result_var, font=("Arial", 10, "italic"),
                        bg="#f0f4f8", fg="#2c3e50", wraplength=380)
result_label.pack(pady=12)

root.mainloop()
"""

# 08 - Radiobutton and Checkbutton Widgets
"""


import tkinter as tk
from tkinter import messagebox

def submit():
    gender  = gender_var.get()
    hobbies = [h for h, v in hobby_vars.items() if v.get()]
    if not gender:
        messagebox.showwarning("Missing", "Please select a gender.")
        return
    if not hobbies:
        messagebox.showwarning("Missing", "Please select at least one hobby.")
        return
    result = f"Gender  : {gender}\nHobbies : {', '.join(hobbies)}"
    messagebox.showinfo("Your Selection", result)

root = tk.Tk()
root.title("Radiobutton & Checkbutton")
root.geometry("380x400")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="Select Options", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=15)

# --- Radiobutton (Gender) ---
gender_frame = tk.LabelFrame(root, text=" Gender ", font=("Arial", 12, "bold"),
                              bg="#f8f9fa", fg="#2c3e50", padx=15, pady=10)
gender_frame.pack(fill="x", padx=30, pady=8)
gender_var = tk.StringVar()
for g in ["Male", "Female", "Other"]:
    tk.Radiobutton(gender_frame, text=g, variable=gender_var, value=g,
                   font=("Arial", 12), bg="#f8f9fa", activebackground="#f8f9fa",
                   cursor="hand2").pack(side="left", padx=12)

# --- Checkbutton (Hobbies) ---
hobby_frame = tk.LabelFrame(root, text=" Hobbies ", font=("Arial", 12, "bold"),
                             bg="#f8f9fa", fg="#2c3e50", padx=15, pady=10)
hobby_frame.pack(fill="x", padx=30, pady=8)
hobbies_list = ["Reading", "Gaming", "Cooking", "Travelling", "Music", "Coding"]
hobby_vars = {}
for i, h in enumerate(hobbies_list):
    var = tk.BooleanVar()
    hobby_vars[h] = var
    tk.Checkbutton(hobby_frame, text=h, variable=var,
                   font=("Arial", 11), bg="#f8f9fa", activebackground="#f8f9fa",
                   cursor="hand2").grid(row=i//3, column=i%3, padx=8, pady=4, sticky="w")

# Buttons
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="Submit", command=submit, font=("Arial", 12), bg="#27ae60",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Exit",   command=root.destroy, font=("Arial", 12), bg="#e74c3c",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=1, padx=10)

root.mainloop()
"""

# 09 - Listbox Widget Demo
"""


import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get().strip()
    if not item:
        messagebox.showwarning("Empty", "Please type an item to add.")
        return
    listbox.insert(tk.END, item)
    entry.delete(0, tk.END)

def delete_item():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("None Selected", "Please select an item to delete.")
        return
    listbox.delete(selected[0])

def clear_all():
    listbox.delete(0, tk.END)

def show_selected():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Selection", "No item selected.")
        return
    item = listbox.get(selected[0])
    messagebox.showinfo("Selected Item", f"You selected: {item}")

def move_up():
    selected = listbox.curselection()
    if not selected or selected[0] == 0:
        return
    idx  = selected[0]
    item = listbox.get(idx)
    listbox.delete(idx)
    listbox.insert(idx - 1, item)
    listbox.select_set(idx - 1)

def move_down():
    selected = listbox.curselection()
    if not selected or selected[0] == listbox.size() - 1:
        return
    idx  = selected[0]
    item = listbox.get(idx)
    listbox.delete(idx)
    listbox.insert(idx + 1, item)
    listbox.select_set(idx + 1)

root = tk.Tk()
root.title("Listbox Demo")
root.geometry("420x460")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

tk.Label(root, text="Listbox Widget", font=("Arial", 16, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=12)

# Entry + Add
top_frame = tk.Frame(root, bg="#f0f4f8")
top_frame.pack(pady=5)
entry = tk.Entry(top_frame, font=("Arial", 12), width=22, relief="solid", bd=1)
entry.pack(side="left", padx=5)
tk.Button(top_frame, text="Add", command=add_item, font=("Arial", 11),
          bg="#27ae60", fg="white", padx=10, pady=4, relief="flat", cursor="hand2").pack(side="left")

# Listbox with scrollbar
lb_frame = tk.Frame(root, bg="#f0f4f8")
lb_frame.pack(pady=10)
scrollbar = tk.Scrollbar(lb_frame, orient=tk.VERTICAL)
listbox = tk.Listbox(lb_frame, font=("Arial", 12), width=28, height=10,
                     yscrollcommand=scrollbar.set, relief="solid", bd=1,
                     selectbackground="#3498db", selectforeground="white", activestyle="none")
scrollbar.config(command=listbox.yview)
listbox.pack(side="left")
scrollbar.pack(side="right", fill="y")

# Pre-fill items
for item in ["Python", "Java", "C++", "JavaScript", "Go", "Rust", "Kotlin"]:
    listbox.insert(tk.END, item)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=10)
cfg = {"font": ("Arial", 10), "fg": "white", "padx": 8, "pady": 5, "relief": "flat", "cursor": "hand2"}
tk.Button(btn_frame, text="Show",       command=show_selected, bg="#3498db", **cfg).grid(row=0, column=0, padx=4)
tk.Button(btn_frame, text="Delete",     command=delete_item,   bg="#e74c3c", **cfg).grid(row=0, column=1, padx=4)
tk.Button(btn_frame, text="Clear All",  command=clear_all,     bg="#95a5a6", **cfg).grid(row=0, column=2, padx=4)
tk.Button(btn_frame, text="Move Up",    command=move_up,       bg="#9b59b6", **cfg).grid(row=0, column=3, padx=4)
tk.Button(btn_frame, text="Move Down",  command=move_down,     bg="#e67e22", **cfg).grid(row=0, column=4, padx=4)

tk.Label(root, text="Tip: Click an item to select it first.", font=("Arial", 9, "italic"),
         bg="#f0f4f8", fg="#95a5a6").pack()

root.mainloop()
"""

# 10 - Menu Bar with Frames (Notepad-like App)
"""


import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont

def new_file():
    text_area.delete("1.0", tk.END)
    root.title("Notepad - New File")

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f.read())
        root.title(f"Notepad - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Saved", f"File saved to {filepath}")
        root.title(f"Notepad - {filepath}")

def cut():   text_area.event_generate("<<Cut>>")
def copy():  text_area.event_generate("<<Copy>>")
def paste(): text_area.event_generate("<<Paste>>")

def select_all():
    text_area.tag_add("sel", "1.0", tk.END)

def increase_font():
    current = text_area.cget("font")
    f = tkfont.Font(font=current)
    f.config(size=f.cget("size") + 2)
    text_area.config(font=f)

def decrease_font():
    current = text_area.cget("font")
    f = tkfont.Font(font=current)
    size = max(8, f.cget("size") - 2)
    f.config(size=size)
    text_area.config(font=f)

def about():
    messagebox.showinfo("About", "Simple Notepad\nBuilt with Python Tkinter")

root = tk.Tk()
root.title("Notepad - New File")
root.geometry("650x480")

# Menu bar
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New",   command=new_file,   accelerator="Ctrl+N")
file_menu.add_command(label="Open",  command=open_file,  accelerator="Ctrl+O")
file_menu.add_command(label="Save",  command=save_file,  accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit",  command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut",        command=cut,        accelerator="Ctrl+X")
edit_menu.add_command(label="Copy",       command=copy,       accelerator="Ctrl+C")
edit_menu.add_command(label="Paste",      command=paste,      accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
menubar.add_cascade(label="Edit", menu=edit_menu)

view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Increase Font Size", command=increase_font)
view_menu.add_command(label="Decrease Font Size", command=decrease_font)
menubar.add_cascade(label="View", menu=view_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# Keyboard shortcuts
root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())
root.bind("<Control-a>", lambda e: select_all())

# Text area with scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

scrollbar_y = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
text_area = tk.Text(frame, font=("Consolas", 12), wrap=tk.NONE,
                    yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set,
                    undo=True, relief="flat", padx=5, pady=5)
scrollbar_y.config(command=text_area.yview)
scrollbar_x.config(command=text_area.xview)
scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")
text_area.pack(fill="both", expand=True)

# Status bar
status_bar = tk.Label(root, text="Ready", anchor="w", font=("Arial", 9),
                      bg="#ecf0f1", fg="#7f8c8d", relief="flat", padx=5)
status_bar.pack(fill="x", side="bottom")

def update_status(event=None):
    line, col = text_area.index(tk.INSERT).split(".")
    status_bar.config(text=f"Line: {line}  Column: {int(col)+1}")

text_area.bind("<KeyRelease>", update_status)
text_area.bind("<ButtonRelease>", update_status)

root.mainloop()
"""

# 11 - Canvas Drawing Shapes
"""


import tkinter as tk

root = tk.Tk()
root.title("Canvas - Drawing Shapes")
root.geometry("600x500")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

tk.Label(root, text=" Canvas Drawing Demo", font=("Arial", 15, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=8)

# Canvas
canvas = tk.Canvas(root, width=560, height=370, bg="white",
                   relief="solid", bd=1, highlightthickness=0)
canvas.pack(padx=20, pady=5)

def draw_all():
    canvas.delete("all")

    # Rectangle
    canvas.create_rectangle(30, 30, 160, 110, fill="#3498db", outline="#2980b9", width=2)
    canvas.create_text(95, 70, text="Rectangle", fill="white", font=("Arial", 11, "bold"))

    # Oval
    canvas.create_oval(200, 30, 360, 120, fill="#e74c3c", outline="#c0392b", width=2)
    canvas.create_text(280, 75, text="Oval", fill="white", font=("Arial", 11, "bold"))

    # Triangle (Polygon)
    canvas.create_polygon(420, 115, 480, 25, 540, 115, fill="#27ae60", outline="#1e8449", width=2)
    canvas.create_text(480, 85, text="Triangle", fill="white", font=("Arial", 10, "bold"))

    # Line
    canvas.create_line(30, 160, 180, 160, fill="#8e44ad", width=4, arrow=tk.LAST)
    canvas.create_text(105, 145, text="Arrow Line", fill="#8e44ad", font=("Arial", 10, "bold"))

    # Arc
    canvas.create_arc(200, 140, 360, 220, start=0, extent=270,
                      fill="#f39c12", outline="#d68910", width=2)
    canvas.create_text(280, 185, text="Arc", fill="white", font=("Arial", 10, "bold"))

    # Star (Polygon)
    import math
    cx, cy, r_outer, r_inner, points = 480, 185, 45, 20, 5
    coords = []
    for i in range(points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        angle = math.pi / points * i - math.pi / 2
        coords += [cx + r * math.cos(angle), cy + r * math.sin(angle)]
    canvas.create_polygon(coords, fill="#e67e22", outline="#d35400", width=2)
    canvas.create_text(480, 185, text="★", fill="white", font=("Arial", 14, "bold"))

    # Text
    canvas.create_text(95, 260, text="Hello, Canvas!", fill="#2c3e50",
                       font=("Arial", 14, "bold italic"))

    # Circle (filled)
    canvas.create_oval(200, 235, 300, 310, fill="#16a085", outline="#0e6655", width=2)
    canvas.create_text(250, 272, text="Circle", fill="white", font=("Arial", 10, "bold"))

    # Dashed Rectangle
    canvas.create_rectangle(330, 235, 545, 310, dash=(8, 4),
                             outline="#e74c3c", width=2)
    canvas.create_text(437, 272, text="Dashed Border", fill="#e74c3c", font=("Arial", 10, "bold"))

    # Grid lines
    for x in range(0, 561, 70):
        canvas.create_line(x, 340, x, 370, fill="#bdc3c7", width=1)
    for y in range(340, 371, 15):
        canvas.create_line(0, y, 560, y, fill="#bdc3c7", width=1)
    canvas.create_text(280, 355, text="Grid Pattern", fill="#7f8c8d", font=("Arial", 9))

draw_all()

btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Redraw", command=draw_all, font=("Arial", 11),
          bg="#3498db", fg="white", padx=14, pady=5, relief="flat", cursor="hand2").grid(row=0, column=0, padx=8)
tk.Button(btn_frame, text="Clear",  command=lambda: canvas.delete("all"), font=("Arial", 11),
          bg="#95a5a6", fg="white", padx=14, pady=5, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)
tk.Button(btn_frame, text="Exit",   command=root.destroy, font=("Arial", 11),
          bg="#e74c3c", fg="white", padx=14, pady=5, relief="flat", cursor="hand2").grid(row=0, column=2, padx=8)

root.mainloop()
"""

# 12 - Student Record Manager (CRUD with Treeview)
"""


import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("720x530")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

tk.Label(root, text="🎓 Student Record Manager", font=("Arial", 16, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=10)

# ---- Form ----
form = tk.Frame(root, bg="#f0f4f8")
form.pack(pady=5)

fields  = ["Roll No", "Name", "Branch", "Semester", "Marks"]
entries = {}
for i, field in enumerate(fields):
    tk.Label(form, text=f"{field}:", font=("Arial", 11), bg="#f0f4f8",
             anchor="e", width=10).grid(row=0, column=i*2, padx=5)
    e = tk.Entry(form, font=("Arial", 11), width=10, relief="solid", bd=1)
    e.grid(row=0, column=i*2+1, padx=3)
    entries[field] = e

# ---- Treeview ----
tree_frame = tk.Frame(root)
tree_frame.pack(padx=20, pady=8, fill="both")

cols = ("Roll No", "Name", "Branch", "Semester", "Marks")
tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=12)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=118, anchor="center")

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Style
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
style.configure("Treeview", font=("Arial", 11), rowheight=26)
style.map("Treeview", background=[("selected", "#3498db")])

def get_entries():
    return [entries[f].get().strip() for f in fields]

def clear_entries():
    for e in entries.values():
        e.delete(0, tk.END)

def add_record():
    vals = get_entries()
    if not all(vals):
        messagebox.showwarning("Missing", "Please fill all fields.")
        return
    tree.insert("", tk.END, values=vals)
    clear_entries()

def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("None", "Please select a record to delete.")
        return
    if messagebox.askyesno("Confirm", "Delete selected record?"):
        tree.delete(selected[0])

def edit_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("None", "Please select a record to edit.")
        return
    vals = get_entries()
    if not all(vals):
        messagebox.showwarning("Missing", "Please fill all fields with new data.")
        return
    tree.item(selected[0], values=vals)
    clear_entries()

def load_to_form(event):
    selected = tree.selection()
    if not selected:
        return
    vals = tree.item(selected[0])["values"]
    for field, val in zip(fields, vals):
        entries[field].delete(0, tk.END)
        entries[field].insert(0, str(val))

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all records?"):
        tree.delete(*tree.get_children())

tree.bind("<<TreeviewSelect>>", load_to_form)

# Pre-load sample data
samples = [
    ("101", "Amit",   "CS",          "3", "85"),
    ("102", "Priya",  "Electronics", "3", "92"),
    ("103", "Rahul",  "Mechanical",  "4", "78"),
]
for s in samples:
    tree.insert("", tk.END, values=s)

# ---- Buttons ----
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=8)
cfg = {"font": ("Arial", 11), "fg": "white", "padx": 12, "pady": 6, "relief": "flat", "cursor": "hand2"}
tk.Button(btn_frame, text="➕ Add",    command=add_record,   bg="#27ae60", **cfg).grid(row=0, column=0, padx=6)
tk.Button(btn_frame, text="✏ Edit",   command=edit_record,  bg="#f39c12", **cfg).grid(row=0, column=1, padx=6)
tk.Button(btn_frame, text="🗑 Delete", command=delete_record, bg="#e74c3c", **cfg).grid(row=0, column=2, padx=6)
tk.Button(btn_frame, text="🧹 Clear",  command=clear_entries, bg="#95a5a6", **cfg).grid(row=0, column=3, padx=6)
tk.Button(btn_frame, text="❌ Clear All", command=clear_all, bg="#7f8c8d", **cfg).grid(row=0, column=4, padx=6)

root.mainloop()
"""

# 13 - Scale, Spinbox and Combobox Widgets
"""


import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Scale, Spinbox & Combobox")
root.geometry("440x480")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="Widget Showcase", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=12)

frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(padx=30, pady=5, fill="x")

# --- Scale (Slider) ---
scale_frame = tk.LabelFrame(frame, text=" Scale (Slider) ", font=("Arial", 11, "bold"),
                             bg="#f8f9fa", fg="#2c3e50", padx=10, pady=8)
scale_frame.pack(fill="x", pady=6)

age_var = tk.IntVar(value=20)
tk.Label(scale_frame, text="Select Age:", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
scale = tk.Scale(scale_frame, from_=1, to=100, orient=tk.HORIZONTAL,
                 variable=age_var, length=340, font=("Arial", 10),
                 bg="#f8f9fa", troughcolor="#3498db", activebackground="#2980b9",
                 highlightthickness=0, cursor="hand2")
scale.pack(fill="x")
age_label = tk.Label(scale_frame, textvariable=age_var, font=("Arial", 12, "bold"),
                     bg="#f8f9fa", fg="#e74c3c")
age_label.pack()

# --- Spinbox ---
spin_frame = tk.LabelFrame(frame, text=" Spinbox ", font=("Arial", 11, "bold"),
                            bg="#f8f9fa", fg="#2c3e50", padx=10, pady=8)
spin_frame.pack(fill="x", pady=6)

tk.Label(spin_frame, text="Select Semester:", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
spinbox = tk.Spinbox(spin_frame, from_=1, to=8, width=5, font=("Arial", 14, "bold"),
                     justify="center", relief="solid", bd=1)
spinbox.pack(anchor="w", pady=4)

tk.Label(spin_frame, text="Select Score (Step 5):", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
spinbox2 = tk.Spinbox(spin_frame, from_=0, to=100, increment=5, width=6, font=("Arial", 13),
                      justify="center", relief="solid", bd=1)
spinbox2.pack(anchor="w", pady=4)

# --- Combobox ---
combo_frame = tk.LabelFrame(frame, text=" Combobox (Dropdown) ", font=("Arial", 11, "bold"),
                             bg="#f8f9fa", fg="#2c3e50", padx=10, pady=8)
combo_frame.pack(fill="x", pady=6)

tk.Label(combo_frame, text="Select Branch:", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
branch_combo = ttk.Combobox(combo_frame, font=("Arial", 11), state="readonly", width=30,
                             values=["Computer Science", "Electronics", "Mechanical",
                                     "Civil", "Information Technology", "BCA", "MCA"])
branch_combo.set("Computer Science")
branch_combo.pack(anchor="w", pady=4)

# Submit
def show_values():
    info = (f"Age      : {age_var.get()}\n"
            f"Semester : {spinbox.get()}\n"
            f"Score    : {spinbox2.get()}\n"
            f"Branch   : {branch_combo.get()}")
    messagebox.showinfo("Selected Values", info)

tk.Button(root, text="Show Selected Values", command=show_values,
          font=("Arial", 12), bg="#3498db", fg="white",
          padx=14, pady=7, relief="flat", cursor="hand2").pack(pady=12)

root.mainloop()
"""

# 14 - Frame and Grid Layout Demo
"""


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Frame & Grid Layout")
root.geometry("500x520")
root.configure(bg="#ecf0f1")
root.resizable(False, False)

tk.Label(root, text="📐 Layout Demo with Frames", font=("Arial", 15, "bold"),
         bg="#ecf0f1", fg="#2c3e50").pack(pady=10)

# ---- TOP FRAME - personal info ----
top_frame = tk.LabelFrame(root, text=" Personal Information ", font=("Arial", 11, "bold"),
                           bg="#ecf0f1", fg="#2c3e50", padx=15, pady=10)
top_frame.pack(fill="x", padx=20, pady=5)

labels_entries = [
    ("First Name:",  0, 0), ("Last Name:",   0, 2),
    ("Email:",       1, 0), ("Phone:",       1, 2),
    ("City:",        2, 0), ("Country:",     2, 2),
]
entry_widgets = {}
for text, row, col in labels_entries:
    tk.Label(top_frame, text=text, font=("Arial", 11), bg="#ecf0f1",
             anchor="e", width=12).grid(row=row, column=col, padx=5, pady=6, sticky="e")
    e = tk.Entry(top_frame, font=("Arial", 11), width=15, relief="solid", bd=1)
    e.grid(row=row, column=col+1, padx=5, pady=6)
    entry_widgets[text] = e

# ---- MIDDLE FRAME - academic info ----
mid_frame = tk.LabelFrame(root, text=" Academic Information ", font=("Arial", 11, "bold"),
                           bg="#ecf0f1", fg="#2c3e50", padx=15, pady=10)
mid_frame.pack(fill="x", padx=20, pady=5)

acad_fields = [("Roll No:", 0, 0), ("Course:", 0, 2), ("Year:", 1, 0), ("CGPA:", 1, 2)]
for text, row, col in acad_fields:
    tk.Label(mid_frame, text=text, font=("Arial", 11), bg="#ecf0f1",
             anchor="e", width=12).grid(row=row, column=col, padx=5, pady=6, sticky="e")
    e = tk.Entry(mid_frame, font=("Arial", 11), width=15, relief="solid", bd=1)
    e.grid(row=row, column=col+1, padx=5, pady=6)
    entry_widgets[text] = e

# ---- BOTTOM FRAME - buttons ----
bottom_frame = tk.Frame(root, bg="#ecf0f1")
bottom_frame.pack(pady=12)

def submit_form():
    filled = {k: v.get().strip() for k, v in entry_widgets.items()}
    empty  = [k for k, v in filled.items() if not v]
    if empty:
        messagebox.showwarning("Incomplete", f"Please fill: {', '.join(empty)}")
        return
    result = "\n".join(f"{k:<14} {v}" for k, v in filled.items())
    messagebox.showinfo("Form Data", result)

def clear_form():
    for e in entry_widgets.values():
        e.delete(0, tk.END)

cfg = {"font": ("Arial", 12), "fg": "white", "padx": 14, "pady": 7, "relief": "flat", "cursor": "hand2"}
tk.Button(bottom_frame, text="Submit", command=submit_form, bg="#27ae60", **cfg).grid(row=0, column=0, padx=10)
tk.Button(bottom_frame, text="Clear",  command=clear_form,  bg="#95a5a6", **cfg).grid(row=0, column=1, padx=10)
tk.Button(bottom_frame, text="Exit",   command=root.destroy, bg="#e74c3c", **cfg).grid(row=0, column=2, padx=10)

root.mainloop()
"""

# 15 - Simple Paint / Drawing App using Canvas
"""


import tkinter as tk
from tkinter import colorchooser, messagebox

root = tk.Tk()
root.title("🎨 Simple Paint App")
root.geometry("700x540")
root.configure(bg="#2c3e50")
root.resizable(False, False)

# Drawing state
draw_color  = "#000000"
brush_size  = 5
last_x = last_y = None
draw_mode   = tk.StringVar(value="pen")

def get_color():
    global draw_color
    color = colorchooser.askcolor(title="Pick Color", color=draw_color)
    if color[1]:
        draw_color = color[1]
        color_btn.config(bg=draw_color)

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    mode = draw_mode.get()
    size = brush_size_scale.get()

    if mode == "pen":
        canvas.create_line(last_x, last_y, event.x, event.y,
                           fill=draw_color, width=size, capstyle=tk.ROUND, smooth=True)
        last_x, last_y = event.x, event.y
    elif mode == "eraser":
        canvas.create_oval(event.x - size, event.y - size,
                           event.x + size, event.y + size,
                           fill="white", outline="white")
        last_x, last_y = event.x, event.y

def draw_shape(event):
    global last_x, last_y
    mode = draw_mode.get()
    size = brush_size_scale.get()
    if mode == "circle":
        canvas.create_oval(event.x - size*3, event.y - size*3,
                           event.x + size*3, event.y + size*3,
                           outline=draw_color, width=2)
    elif mode == "rect":
        canvas.create_rectangle(last_x, last_y, event.x, event.y,
                                 outline=draw_color, width=2)

def clear_canvas():
    canvas.delete("all")

def fill_bg():
    canvas.configure(bg=draw_color)

# ---- Toolbar ----
toolbar = tk.Frame(root, bg="#34495e", pady=5)
toolbar.pack(fill="x")

tk.Label(toolbar, text="Mode:", font=("Arial", 10), bg="#34495e", fg="white").pack(side="left", padx=8)
modes = [("Pen", "pen"), ("Eraser", "eraser"), ("Circle", "circle"), ("Rectangle", "rect")]
for label, val in modes:
    tk.Radiobutton(toolbar, text=label, variable=draw_mode, value=val,
                   font=("Arial", 10), bg="#34495e", fg="white",
                   selectcolor="#2c3e50", activebackground="#34495e",
                   activeforeground="white", cursor="hand2").pack(side="left", padx=5)

tk.Label(toolbar, text="  Size:", font=("Arial", 10), bg="#34495e", fg="white").pack(side="left", padx=5)
brush_size_scale = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL,
                             bg="#34495e", fg="white", troughcolor="#3498db",
                             highlightthickness=0, length=100)
brush_size_scale.set(5)
brush_size_scale.pack(side="left")

color_btn = tk.Button(toolbar, text="  Color  ", command=get_color,
                      bg=draw_color, fg="white", font=("Arial", 10, "bold"),
                      relief="flat", padx=6, cursor="hand2")
color_btn.pack(side="left", padx=10)

tk.Button(toolbar, text="Clear", command=clear_canvas,
          bg="#e74c3c", fg="white", font=("Arial", 10),
          relief="flat", padx=8, cursor="hand2").pack(side="left", padx=4)

tk.Button(toolbar, text="Fill BG", command=fill_bg,
          bg="#8e44ad", fg="white", font=("Arial", 10),
          relief="flat", padx=8, cursor="hand2").pack(side="left", padx=4)

# ---- Canvas ----
canvas = tk.Canvas(root, bg="white", cursor="crosshair",
                   highlightthickness=0)
canvas.pack(fill="both", expand=True, padx=10, pady=8)

canvas.bind("<ButtonPress-1>",  start_draw)
canvas.bind("<B1-Motion>",      draw)
canvas.bind("<ButtonRelease-1>", draw_shape)

# Status bar
status = tk.Label(root, text="Draw on the canvas. Use toolbar to switch modes.",
                  font=("Arial", 9), bg="#2c3e50", fg="#bdc3c7", anchor="w", padx=10)
status.pack(fill="x")

def update_status(event):
    status.config(text=f"X: {event.x}  Y: {event.y}  | Mode: {draw_mode.get()} | Size: {brush_size_scale.get()}")

canvas.bind("<Motion>", update_status)

root.mainloop()
"""

# 16 - Quiz Application
"""


import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the output of print(type([]))?",
        "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": 1
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["2", "4", "3", "1"],
        "answer": 2
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": ["tuple", "string", "list", "int"],
        "answer": 2
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": 2
    },
]

class QuizApp:
    def __init__(self, root):
        self.root  = root
        self.root.title("Python Quiz")
        self.root.geometry("540x440")
        self.root.configure(bg="#1a252f")
        self.root.resizable(False, False)

        self.index  = 0
        self.score  = 0
        self.selected = tk.IntVar(value=-1)

        # Header
        self.header = tk.Label(root, text="🐍 Python Quiz", font=("Arial", 18, "bold"),
                               bg="#1a252f", fg="#f1c40f")
        self.header.pack(pady=12)

        # Progress
        self.progress_label = tk.Label(root, text="", font=("Arial", 11),
                                       bg="#1a252f", fg="#bdc3c7")
        self.progress_label.pack()

        # Question
        self.q_label = tk.Label(root, text="", font=("Arial", 13),
                                bg="#2c3e50", fg="white", wraplength=480,
                                justify="left", padx=20, pady=20, relief="flat")
        self.q_label.pack(fill="x", padx=30, pady=10)

        # Options frame
        self.opt_frame = tk.Frame(root, bg="#1a252f")
        self.opt_frame.pack(padx=30, fill="x")
        self.option_btns = []
        for i in range(4):
            btn = tk.Radiobutton(self.opt_frame, text="", variable=self.selected,
                                 value=i, font=("Arial", 12), bg="#1a252f", fg="white",
                                 selectcolor="#2c3e50", activebackground="#1a252f",
                                 activeforeground="white", anchor="w", cursor="hand2")
            btn.pack(fill="x", pady=3)
            self.option_btns.append(btn)

        # Feedback
        self.feedback = tk.Label(root, text="", font=("Arial", 11, "bold"),
                                 bg="#1a252f", fg="white")
        self.feedback.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#1a252f")
        btn_frame.pack(pady=8)
        self.next_btn = tk.Button(btn_frame, text="Next ➡", command=self.next_question,
                                  font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                                  padx=18, pady=7, relief="flat", cursor="hand2")
        self.next_btn.grid(row=0, column=0, padx=10)

        self.quit_btn = tk.Button(btn_frame, text="Quit", command=root.destroy,
                                  font=("Arial", 12), bg="#e74c3c", fg="white",
                                  padx=18, pady=7, relief="flat", cursor="hand2")
        self.quit_btn.grid(row=0, column=1, padx=10)

        self.load_question()

    def load_question(self):
        self.selected.set(-1)
        self.feedback.config(text="")
        q = questions[self.index]
        self.progress_label.config(text=f"Question {self.index + 1} of {len(questions)}  |  Score: {self.score}")
        self.q_label.config(text=f"Q{self.index+1}. {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.option_btns[i].config(text=f"  {chr(65+i)}.  {opt}", fg="white")
        self.next_btn.config(text="Next ➡" if self.index < len(questions)-1 else "Finish 🏁")

    def next_question(self):
        ans = self.selected.get()
        if ans == -1:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return
        correct = questions[self.index]["answer"]
        if ans == correct:
            self.score += 1
            self.feedback.config(text="✅ Correct!", fg="#2ecc71")
            self.option_btns[ans].config(fg="#2ecc71")
        else:
            self.feedback.config(text=f"❌ Wrong! Correct: {chr(65+correct)}. {questions[self.index]['options'][correct]}", fg="#e74c3c")
            self.option_btns[ans].config(fg="#e74c3c")
            self.option_btns[correct].config(fg="#2ecc71")

        self.root.after(1200, self.advance)

    def advance(self):
        self.index += 1
        if self.index < len(questions):
            self.load_question()
        else:
            pct = (self.score / len(questions)) * 100
            grade = "Excellent! 🏆" if pct >= 80 else "Good! 👍" if pct >= 60 else "Keep Practising! 📚"
            messagebox.showinfo("Quiz Finished",
                                f"Quiz Complete!\n\nScore : {self.score}/{len(questions)}\n"
                                f"Percentage : {pct:.0f}%\nResult : {grade}")
            self.root.destroy()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
"""

# 17 - Digital Clock and Stopwatch
"""


import tkinter as tk
import time

root = tk.Tk()
root.title("Clock & Stopwatch")
root.geometry("440x380")
root.configure(bg="#1a252f")
root.resizable(False, False)

# ---- DIGITAL CLOCK ----
clock_frame = tk.LabelFrame(root, text=" 🕐 Digital Clock ", font=("Arial", 11, "bold"),
                             bg="#1a252f", fg="#f1c40f", padx=10, pady=10)
clock_frame.pack(fill="x", padx=20, pady=12)

time_label = tk.Label(clock_frame, text="", font=("Courier", 38, "bold"),
                      bg="#1a252f", fg="#2ecc71")
time_label.pack()

date_label = tk.Label(clock_frame, text="", font=("Arial", 13),
                      bg="#1a252f", fg="#bdc3c7")
date_label.pack()

def update_clock():
    now = time.localtime()
    time_label.config(text=time.strftime("%H : %M : %S", now))
    date_label.config(text=time.strftime("%A, %d %B %Y", now))
    root.after(1000, update_clock)

update_clock()

# ---- STOPWATCH ----
sw_frame = tk.LabelFrame(root, text=" ⏱ Stopwatch ", font=("Arial", 11, "bold"),
                          bg="#1a252f", fg="#f1c40f", padx=10, pady=10)
sw_frame.pack(fill="x", padx=20, pady=5)

sw_running    = False
sw_elapsed    = 0.0
sw_start_time = 0.0

sw_display = tk.Label(sw_frame, text="00 : 00 . 00", font=("Courier", 30, "bold"),
                      bg="#1a252f", fg="#e74c3c")
sw_display.pack()

def format_time(elapsed):
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    centiseconds = int((elapsed % 1) * 100)
    return f"{minutes:02d} : {seconds:02d} . {centiseconds:02d}"

def update_stopwatch():
    if sw_running:
        elapsed = sw_elapsed + (time.time() - sw_start_time)
        sw_display.config(text=format_time(elapsed))
        root.after(10, update_stopwatch)

def start_stop():
    global sw_running, sw_start_time, sw_elapsed
    if not sw_running:
        sw_start_time = time.time()
        sw_running = True
        start_btn.config(text="⏸ Pause", bg="#e67e22")
        update_stopwatch()
    else:
        sw_elapsed += time.time() - sw_start_time
        sw_running = False
        start_btn.config(text="▶ Start", bg="#27ae60")

def reset_sw():
    global sw_running, sw_elapsed
    sw_running = False
    sw_elapsed = 0.0
    start_btn.config(text="▶ Start", bg="#27ae60")
    sw_display.config(text="00 : 00 . 00")

sw_btn_frame = tk.Frame(sw_frame, bg="#1a252f")
sw_btn_frame.pack(pady=8)
start_btn = tk.Button(sw_btn_frame, text="▶ Start", command=start_stop,
                      font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                      padx=14, pady=6, relief="flat", cursor="hand2")
start_btn.grid(row=0, column=0, padx=8)

tk.Button(sw_btn_frame, text="↺ Reset", command=reset_sw,
          font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
          padx=14, pady=6, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)

root.mainloop()
"""

# 18 - To-Do List Application
"""


import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("460x540")
        self.root.configure(bg="#f8f9fa")
        self.root.resizable(False, False)

        self.tasks = []

        # Header
        tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"),
                 bg="#f8f9fa", fg="#2c3e50").pack(pady=12)

        # Input frame
        input_frame = tk.Frame(root, bg="#f8f9fa")
        input_frame.pack(padx=20, fill="x")

        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), relief="solid", bd=1)
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        tk.Button(input_frame, text="Add", command=self.add_task,
                  font=("Arial", 11, "bold"), bg="#27ae60", fg="white",
                  padx=12, pady=6, relief="flat", cursor="hand2").pack(side="left")

        # Task listbox with scrollbar
        lb_frame = tk.Frame(root, bg="#f8f9fa")
        lb_frame.pack(padx=20, pady=10, fill="both", expand=True)

        scrollbar = tk.Scrollbar(lb_frame)
        self.listbox = tk.Listbox(lb_frame, font=("Arial", 12), relief="solid", bd=1,
                                  yscrollcommand=scrollbar.set, height=14,
                                  selectbackground="#3498db", selectforeground="white",
                                  activestyle="none")
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.listbox.bind("<Double-Button-1>", lambda e: self.toggle_done())

        # Status bar
        self.status_var = tk.StringVar(value="0 tasks")
        tk.Label(root, textvariable=self.status_var, font=("Arial", 10, "italic"),
                 bg="#f8f9fa", fg="#7f8c8d").pack()

        # Buttons
        btn_frame = tk.Frame(root, bg="#f8f9fa")
        btn_frame.pack(pady=10)
        cfg = {"font": ("Arial", 11), "fg": "white", "padx": 10, "pady": 6, "relief": "flat", "cursor": "hand2"}
        tk.Button(btn_frame, text="✔ Done",    command=self.toggle_done,  bg="#3498db", **cfg).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="✏ Edit",    command=self.edit_task,    bg="#f39c12", **cfg).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🗑 Delete",  command=self.delete_task,  bg="#e74c3c", **cfg).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="🧹 Clear All", command=self.clear_all, bg="#95a5a6", **cfg).grid(row=0, column=3, padx=5)

        # Sample tasks
        for t in ["Buy groceries", "Study Python Tkinter", "Complete assignment", "Read a book"]:
            self.add_task(t)

    def add_task(self, text=None):
        task = text if text else self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Empty", "Please enter a task.")
            return
        self.tasks.append({"text": task, "done": False})
        self.listbox.insert(tk.END, f"  ○  {task}")
        self.task_entry.delete(0, tk.END)
        self.update_status()

    def toggle_done(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        idx = selected[0]
        task = self.tasks[idx]
        task["done"] = not task["done"]
        if task["done"]:
            self.listbox.itemconfig(idx, fg="#27ae60")
            self.listbox.delete(idx)
            self.listbox.insert(idx, f"  ✔  {task['text']}")
            self.listbox.itemconfig(idx, fg="#27ae60")
        else:
            self.listbox.delete(idx)
            self.listbox.insert(idx, f"  ○  {task['text']}")
            self.listbox.itemconfig(idx, fg="black")
        self.update_status()

    def edit_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("None", "Select a task to edit.")
            return
        idx = selected[0]
        old = self.tasks[idx]["text"]
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(0, old)
        self.tasks.pop(idx)
        self.listbox.delete(idx)
        self.update_status()

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("None", "Select a task to delete.")
            return
        idx = selected[0]
        if messagebox.askyesno("Confirm", f"Delete '{self.tasks[idx]['text']}'?"):
            self.tasks.pop(idx)
            self.listbox.delete(idx)
            self.update_status()

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Clear all tasks?"):
            self.tasks.clear()
            self.listbox.delete(0, tk.END)
            self.update_status()

    def update_status(self):
        done  = sum(1 for t in self.tasks if t["done"])
        total = len(self.tasks)
        self.status_var.set(f"{total} tasks  |  {done} completed  |  {total-done} pending")

root = tk.Tk()
app  = TodoApp(root)
root.mainloop()
"""
