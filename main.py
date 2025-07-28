import tkinter as tk
from tkinter import Toplevel
from ttkbootstrap import Style, ttk

# Approx standard keyboard keys
STANDARD_KEYS = set([
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9',
    'space','shift','control','alt','tab','enter','backspace','caps_lock','esc',
    'up','down','left','right',
    'insert','delete','home','end','page_up','page_down',
    'f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12',
    '`','-','=','[',']','\\',';',"'",',','.','/'
])

pressed_history = []

def create_main_window():
    style = Style("darkly")  # sleek dark theme

    root = style.master
    root.title("Keyboard Tester")
    root.geometry("550x450")
    root.configure(bg="#1e1e1e")  # Deep dark background
    root.resizable(False, False)

    # Header
    header = ttk.Label(root, text="Keyboard Tester", font=("Segoe UI", 22, "bold"), foreground="white", background="#1e1e1e")
    header.pack(pady=25)

    # Key display box
    key_box = tk.Label(root, text="", font=("Consolas", 28, "bold"), fg="#FFFFFF", bg="#2e2e2e",
                       width=12, height=2, bd=0, relief="flat")
    key_box.place(relx=0.5, rely=0.42, anchor="center")

    def show_key(event):
        key = event.keysym.lower()
        if key not in pressed_history:
            pressed_history.append(key)

        key_box.config(text=key.upper())
        if hasattr(show_key, 'timer'):
            key_box.after_cancel(show_key.timer)
        show_key.timer = key_box.after(3000, lambda: key_box.config(text=""))

    root.bind("<Key>", show_key)

    # Show Results Window
    def show_results():
        result_win = Toplevel(root)
        result_win.title("Key Test Results")
        result_win.geometry("420x420")
        result_win.configure(bg="#1e1e1e")

        ttk.Label(result_win, text="Key Press History", font=("Segoe UI", 16, "bold"), foreground="white", background="#1e1e1e").pack(pady=10)

        frame = ttk.Frame(result_win)
        frame.pack(pady=10, fill='both', expand=True)

        history_list = tk.Listbox(frame, font=("Consolas", 12), bg="#2b2b2b", fg="white", bd=0, relief="flat")
        for key in pressed_history:
            history_list.insert(tk.END, key.upper())

        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=history_list.yview)
        history_list.config(yscrollcommand=scrollbar.set)
        history_list.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        count_label = ttk.Label(result_win, text=f"Pressed: {len(set(pressed_history))}/106",
                                font=("Segoe UI", 13), background="#1e1e1e", foreground="white")
        count_label.pack(pady=15)

    # Check Results Button
    check_button = ttk.Button(root, text="Check Results", bootstyle="success-outline", command=show_results)
    check_button.pack(side="bottom", pady=30)

    # Credit Line
    credit_label = ttk.Label(root, text="Developed And Presented By Anukalp Varshney",
                             font=("Segoe UI", 10), foreground="#bbbbbb", background="#1e1e1e", anchor="center")
    credit_label.pack(side="bottom", pady=5)

    root.mainloop()

create_main_window()
