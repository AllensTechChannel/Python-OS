import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as tkFont

root = tk.Tk()
root.title("About PythonOS")
root.geometry("456x420")
root.resizable(False, False)

# --- Image ---
img = Image.open("python-logo.png")
tk_img = ImageTk.PhotoImage(img)
image_label = tk.Label(root, image=tk_img)
image_label.image = tk_img  # prevent garbage collection
image_label.pack(pady=5)

# --- Title ---
title_font = tkFont.Font(family="Arial", size=25)
ttk.Label(root, text="PythonOS 4", font=title_font).pack()

# --- Divider line ---
horizontal_line = tk.Frame(root, height=1, bg="black")
horizontal_line.pack(fill="x", padx=10, pady=10)

# --- Version info ---
info_font = tkFont.Font(family="Arial", size=12)
ttk.Label(root, text="Version: PythonOS 4.14.0", font=info_font).pack(pady=2)
ttk.Label(root, text="Copyright: All programs are property of their respective owners",
          font=info_font, wraplength=400, justify="center").pack(pady=2)

# --- Owner info from file ---
try:
    with open("owner.txt", "r", encoding="utf-8") as text_file:
        content = text_file.read().strip()
    ttk.Label(root, text=f"This product is regestered to:                                                                       {content}", font=info_font, wraplength=400,
              justify="center").pack(pady=5)
except FileNotFoundError:
    ttk.Label(root, text="Owner: (owner.txt not found)", font=info_font,
              wraplength=400, justify="center", foreground="red").pack(pady=5)




try:
    with open("ownercompany.txt", "r", encoding="utf-8") as text_file:
        content = text_file.read().strip()
    ttk.Label(root, text=f" {content}", font=info_font, wraplength=400,
              justify="center").pack(pady=5)
except FileNotFoundError:
    ttk.Label(root, text="Owner: (owner.txt not found)", font=info_font,
              wraplength=400, justify="center", foreground="red").pack(pady=5)


# --- OK button ---
bottom_button = tk.Button(root, text="OK", command=root.destroy)
bottom_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

root.mainloop()

