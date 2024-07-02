import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import subprocess
from PIL import Image, ImageTk

# Function to save patient info and command output to PDF
def save_to_pdf(patient_info, file_column1, file_column2, command_output):
    file_name = f"{patient_info['name'].replace(' ', '_')}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, "Oral Cancer Test")
    c.drawString(100, 730, f"Name: {patient_info['name']}")
    c.drawString(100, 710, f"Age: {patient_info['age']}")
    c.drawString(100, 690, f"Gender: {patient_info['gender']}")
    c.drawString(100, 670, f"Contact Number: {patient_info['contact']}")
    c.drawString(100, 650, f"Location: {patient_info['location']}")

    y = 630
    c.drawString(100, y, "Attached File (ML Model):")
    y -= 20
    c.drawString(100, y, file_column1)

    y -= 40
    c.drawString(100, y, "Attached File (Image Inserted):")
    y -= 20
    c.drawString(100, y, file_column2)

    y -= 40
    c.drawString(100, y, "Command Output:")
    y -= 20
    for line in command_output.splitlines():
        c.drawString(100, y, line)
        y -= 20

    c.save()
    messagebox.showinfo("Success", f"PDF saved as {file_name}")

# Function to submit patient info and open file attachment window
def submit():
    patient_info = {
        "name": entry_name.get(),
        "age": entry_age.get(),
        "gender": entry_gender.get(),
        "contact": entry_contact.get(),
        "location": entry_location.get()
    }
    root.withdraw()
    open_file_attachment_window(patient_info)

# Function to browse and add files to an entry
def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# Function to execute the classify-image.py script with the selected files
def execute_script(patient_info, file_column1, file_column2):
    command = f"python3 classify-image.py \"{file_column1}\" \"{file_column2}\""
    try:
        command_output = subprocess.check_output(command, shell=True, text=True)
        messagebox.showinfo("Success", "Script executed successfully.")
    except subprocess.CalledProcessError as e:
        command_output = e.output
        messagebox.showerror("Error", f"Script execution failed: {e.output}")

    save_to_pdf(patient_info, file_column1, file_column2, command_output)

# Function to open the file attachment window
def open_file_attachment_window(patient_info):
    file_window = tk.Toplevel(root)
    file_window.title("Attach Files")
    file_window.configure(bg="#000000")

    tk.Label(file_window, text="ML Model", bg="#004d40", fg="#ffffff").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(file_window, text="Image", bg="#004d40", fg="#ffffff").grid(row=0, column=1, padx=10, pady=5)

    entry1 = tk.Entry(file_window, bg="#ffffff", width=50)
    entry2 = tk.Entry(file_window, bg="#ffffff", width=50)
    entry1.grid(row=1, column=0, padx=10, pady=5)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(file_window, text="Upload", command=lambda: browse_file(entry1), bg="#004d40", fg="#ffffff").grid(row=2, column=0, pady=10)
    tk.Button(file_window, text="Upload", command=lambda: browse_file(entry2), bg="#004d40", fg="#ffffff").grid(row=2, column=1, pady=10)

    tk.Button(file_window, text="Save to PDF", command=lambda: save_to_pdf(patient_info, entry1.get(), entry2.get(), ""), bg="#004d40", fg="#ffffff").grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(file_window, text="Execute Script", command=lambda: execute_script(patient_info, entry1.get(), entry2.get()), bg="#004d40", fg="#ffffff").grid(row=4, column=0, columnspan=2, pady=10)

# Create the main window
root = tk.Tk()
root.title("Oral Cancer Test")
root.geometry("600x350")

# Load the background image
bg_image = Image.open("bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to place the background image
canvas = tk.Canvas(root, width=bg_image.width, height=bg_image.height)
canvas.pack(fill="both", expand=True)

# Place the background image
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create and place the labels and entries with colors
tk.Label(root, text="Name", bg="#000000", fg="#ffffff").place(x=50, y=50)
tk.Label(root, text="Age", bg="#000000", fg="#ffffff").place(x=50, y=100)
tk.Label(root, text="Gender", bg="#000000", fg="#ffffff").place(x=50, y=150)
tk.Label(root, text="Contact Number", bg="#000000", fg="#ffffff").place(x=50, y=200)
tk.Label(root, text="Location", bg="#000000", fg="#ffffff").place(x=50, y=250)

entry_name = tk.Entry(root, bg="#ffffff")
entry_age = tk.Entry(root, bg="#ffffff")
entry_gender = tk.Entry(root, bg="#ffffff")
entry_contact = tk.Entry(root, bg="#ffffff")
entry_location = tk.Entry(root, bg="#ffffff")

entry_name.place(x=200, y=50)
entry_age.place(x=200, y=100)
entry_gender.place(x=200, y=150)
entry_contact.place(x=200, y=200)
entry_location.place(x=200, y=250)

# Create and place the next button with colors
tk.Button(root, text="Next", command=submit, bg="#004d40", fg="#ffffff").place(x=300, y=300)

# Run the application
root.mainloop()
