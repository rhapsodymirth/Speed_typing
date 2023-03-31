import tkinter as tk
import time
import threading
import random

class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("How fast can you type?")
        self.root.geometry("1000x600")
        self.root.config(bg="grey")

        self.texts = open("text.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)
        self.frame.config(bg="grey")

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=["Tahoma", 24], fg="white", bg="grey")
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=["Calbri", 16], bg="gray")
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)

        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS \n0.00 CPM  \n0.00 WPS \n0.00WPM", font=["Helvetica", 18], bg="grey")
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=["Helvetica", 20], bg="#FFA500")
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running =True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.config(fg="#39FF14")

    def time_thread(self):
        while self.running:
            time.sleep((0.1))
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n {wps:.2f} WPS\n {wpm:.2f} WPM ")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS \n0.00 CPM \n0.00 WPS \n0.00WPM ")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)

TypeSpeedGUI()




