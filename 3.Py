import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Button 연습")
root.geometry("500x400")
root.configure(bg="white")

click_count = 0
status_var = tk.StringVar()
status_var.set("버튼을 클릭해보세요!")

status_label = tk.Label(root, textvariabel=status_var, font=("맑은 고딕", 14))
status_label.pack(pady=20)

def basic_click():
    global click_count
    