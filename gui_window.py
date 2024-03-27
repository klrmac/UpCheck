# gui_window.py
import tkinter as tk
from domain_checker import check_domain_status

class UpCheckGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("UpCheck")

        self.domain_label = tk.Label(self.master, text="Enter Domain:")
        self.domain_label.pack()

        self.domain_entry = tk.Entry(self.master)
        self.domain_entry.pack()

        self.check_button = tk.Button(self.master, text="Check Status", command=self.check_domain)
        self.check_button.pack()

        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack()

    def check_domain(self):
        domain = self.domain_entry.get()
        status = check_domain_status(domain)
        self.status_label.config(text=f"Domain status: {status}")

def create_gui():
    root = tk.Tk()
    app = UpCheckGUI(root)
    root.mainloop()