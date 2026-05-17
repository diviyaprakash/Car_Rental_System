import tkinter as tk
from user_panel import open_user_panel
from admin_panel import open_admin_panel  # You can leave this empty for now if not yet made

def main():
    root = tk.Tk()
    root.title("Car Rental System")
    root.geometry("700x500")
    root.configure(bg="#0D0D0D")

    tk.Label(root, text="Car Rental System", font=("Helvetica", 22, "bold"), fg="#00FF00", bg="#0D0D0D").pack(pady=40)

    tk.Button(root, text="User Login", font=("Helvetica", 14), bg="#00cc44", fg="white", width=20,
              command=lambda: open_user_panel(root)).pack(pady=10)

    tk.Button(root, text="Admin Login", font=("Helvetica", 14), bg="#0099cc", fg="white", width=20,
              command=lambda: open_admin_panel(root)).pack(pady=10)

    tk.Button(root, text="Exit", font=("Helvetica", 14), bg="#d11a2a", fg="white", width=20, command=root.quit).pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    main()
