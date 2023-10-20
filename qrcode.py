import tkinter as tk
from tkinter import messagebox
import segno
from PIL import Image, ImageTk

# Function to generate QR code and display it
def generate_qrcode():
    link = link_entry.get()
    qrcode = segno.make_qr(link)
    qrcode.save("basic_qrcode.png", scale=20)
    qr_image = Image.open("basic_qrcode.png")
    tk_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=tk_image)
    qr_label.image = tk_image
    qr_label.pack()
    qr_label.pack()


app = tk.Tk()
app.title("QR Code Generator")

# Styling improvements
app.geometry("400x400")  # Set the initial window size
app.configure(bg="#8E8FFA")  # Background color


# Header label
header_label = tk.Label(app, text="QR Code Generator", font=("Helvetica", 16, "bold"), bg="#8E8FFA", fg="white")
header_label.pack(pady=10)

# Label for instructions
instruction_label = tk.Label(app, text="Enter the link and click the button to generate a QR code.", bg="#8E8FFA", fg="white")
instruction_label.pack()

# Entry field for the link
link_entry = tk.Entry(app, width=40)
link_entry.pack(pady=10)

# Button to generate QR code
generate_button = tk.Button(app, text="Generate QR Code", command=generate_qrcode, bg="#4CAF50", fg="white", relief="solid")
generate_button.pack()

# Label to display the QR code
qr_label = tk.Label(app, bg="#8E8FFA")

# Close the application when the window is closed
app.protocol("WM_DELETE_WINDOW", app.quit)

app.mainloop()