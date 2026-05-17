from tkinter import Toplevel, Frame, Button, ttk, messagebox
import db_connection  # Ensure your db_connection logic is correct.

def open_admin_panel(root):
    admin_window = Toplevel(root)
    admin_window.title("Admin Panel")
    admin_window.geometry("800x600")
    admin_window.configure(bg='black')  # Dark background

    heading = ttk.Label(admin_window, text="ADMIN PANEL", font=("Helvetica", 20, "bold"), background="black", foreground="lime")
    heading.pack(pady=20)

    button_frame = Frame(admin_window, bg="black")
    button_frame.pack(pady=10)

    # Button style options
    button_style = {
        "bg": "#006400",
        "fg": "white",
        "font": ("Helvetica", 12, "bold"),
        "width": 20,
        "height": 2,
        "bd": 0,
        "activebackground": "#228B22",  # brighter green on click
        "activeforeground": "white"
    }

    # Adding buttons for each functionality
    Button(button_frame, text="View All Cars", command=lambda: view_data("cars", admin_window), **button_style).grid(row=0, column=0, padx=10, pady=10)
    Button(button_frame, text="View Bookings", command=lambda: view_data("bookings", admin_window), **button_style).grid(row=0, column=1, padx=10, pady=10)
    Button(button_frame, text="View Payments", command=lambda: view_data("payments", admin_window), **button_style).grid(row=0, column=2, padx=10, pady=10)

    # Treeview styling
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="black")
    style.configure("Treeview.Heading",
                    background="darkgreen",
                    foreground="white",
                    font=('Helvetica', 12, 'bold'))

def view_data(table_name, admin_window):
    # Clear any existing widgets in admin_window before displaying new data
    for widget in admin_window.winfo_children():
        widget.destroy()

    # Add the heading back after clearing
    heading = ttk.Label(admin_window, text="ADMIN PANEL", font=("Helvetica", 20, "bold"), background="black", foreground="lime")
    heading.pack(pady=20)

    button_frame = Frame(admin_window, bg="black")
    button_frame.pack(pady=10)

    # Button style options
    button_style = {
        "bg": "#006400",
        "fg": "white",
        "font": ("Helvetica", 12, "bold"),
        "width": 20,
        "height": 2,
        "bd": 0,
        "activebackground": "#228B22",  # brighter green on click
        "activeforeground": "white"
    }

    Button(button_frame, text="View All Cars", command=lambda: view_data("cars", admin_window), **button_style).grid(row=0, column=0, padx=10, pady=10)
    Button(button_frame, text="View Bookings", command=lambda: view_data("bookings", admin_window), **button_style).grid(row=0, column=1, padx=10, pady=10)
    Button(button_frame, text="View Payments", command=lambda: view_data("payments", admin_window), **button_style).grid(row=0, column=2, padx=10, pady=10)

    # Get the database connection
    connection = db_connection.get_connection()

    # Check if the connection was successful
    if connection is None or not connection.is_connected():
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Set up a Treeview to display data
        tree = ttk.Treeview(admin_window, columns=("ID", "Name", "Details"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Details", text="Details")

        # Populate the tree with rows from the database
        for row in rows:
            tree.insert("", "end", values=row)

        # Treeview positioning and layout
        tree.pack(fill="both", expand=True, padx=20, pady=20)
    
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to load {table_name}: {err}")
    finally:
        cursor.close()
        connection.close()
