import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import get_connection

def open_user_panel(root):
    root.destroy()
    user_root = tk.Tk()
    user_root.title("User Panel - Car Rental System")
    user_root.configure(bg='black')
    user_root.geometry("800x600")

    title = tk.Label(user_root, text="Available Cars", bg='black', fg='lime', font=("Helvetica", 18, "bold"))
    title.pack(pady=20)

    tree = ttk.Treeview(user_root, columns=("Car ID", "Brand", "Model", "Year", "Price Per Day"), show='headings')
    tree.heading("Car ID", text="Car ID")
    tree.heading("Brand", text="Brand")
    tree.heading("Model", text="Model")
    tree.heading("Year", text="Year")
    tree.heading("Price Per Day", text="Price/Day (₹)")
    tree.pack(pady=20, fill=tk.BOTH, expand=True)

    # Display green style
    style = ttk.Style()
    style.configure("Treeview", background="black", foreground="lime", fieldbackground="black", rowheight=30)
    style.map('Treeview', background=[('selected', 'dark green')])

    def load_available_cars():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT car_id, brand, model, year, price_per_day FROM cars WHERE availability = 1")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert('', tk.END, values=row)
        conn.close()

    def book_selected_car():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Select Car", "Please select a car to book.")
            return
        car_id = tree.item(selected[0])['values'][0]
        confirm = messagebox.askyesno("Confirm Booking", f"Do you want to book Car ID {car_id}?")
        if confirm:
            # For now, assume user_id is 1 (can be improved later with login session)
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO bookings (user_id, car_id, start_date, end_date, status)
                    VALUES (1, %s, CURDATE(), CURDATE() + INTERVAL 3 DAY, 'pending')
                """, (car_id,))
                cursor.execute("UPDATE cars SET availability = 0 WHERE car_id = %s", (car_id,))
                conn.commit()
                messagebox.showinfo("Success", "Car booked successfully!")
                tree.delete(*tree.get_children())
                load_available_cars()
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Error", f"Booking failed: {str(e)}")
            finally:
                conn.close()

    load_available_cars()

    book_btn = tk.Button(user_root, text="Book Selected Car", command=book_selected_car,
                         bg="dark green", fg="white", font=("Helvetica", 12, "bold"))
    book_btn.pack(pady=10)

    user_root.mainloop()
