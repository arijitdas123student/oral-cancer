import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import subprocess
import platform

# Function to save patient info and command output to PDF
def save_to_pdf(patient_info, file_column1, file_column2, command_output):
    file_name = f"{patient_info['name'].replace(' ', '_')}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, f"Patient Information")
    c.drawString(100, 730, f"Name: {patient_info['name']}")
    c.drawString(100, 710, f"Age: {patient_info['age']}")
    c.drawString(100, 690, f"Gender: {patient_info['gender']}")
    c.drawString(100, 670, f"Contact Number: {patient_info['contact']}")
    c.drawString(100, 650, f"Location: {patient_info['location']}")

    y = 630
    c.drawString(100, y, f"Attached File (Column 1):")
    y -= 20
    c.drawString(100, y, file_column1)

    y -= 40
    c.drawString(100, y, f"Attached File (Column 2):")
    y -= 20
    c.drawString(100, y, file_column2)

    y -= 40
    c.drawString(100, y, f"Command Output:")
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
    command_output = ""

    try:
        command_output = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Script execution failed: {e.output}")
        return

    messagebox.showinfo("Success", "Script executed successfully.")
    save_to_pdf(patient_info, file_column1, file_column2, command_output)

# Function to open the file attachment window
def open_file_attachment_window(patient_info):
    file_window = tk.Toplevel(root)
    file_window.title("Attach Files")
    file_window.configure(bg="#f0f0f0")

    tk.Label(file_window, text="ML Model", bg="#e0f7fa", fg="#00796b").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(file_window, text="Image", bg="#e0f7fa", fg="#00796b").grid(row=0, column=1, padx=10, pady=5)

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
root.title("Patient Information")
root.configure(bg="#f0f0f0")

# Define vibrant colors
bg_color = "#e0f7fa"
label_color = "#00796b"
entry_bg_color = "#ffffff"
button_color = "#004d40"
button_text_color = "#ffffff"

# Create and place the labels and entries with colors
tk.Label(root, text="Name", bg=bg_color, fg=label_color).grid(row=0, sticky=tk.W, pady=2)
tk.Label(root, text="Age", bg=bg_color, fg=label_color).grid(row=1, sticky=tk.W, pady=2)
tk.Label(root, text="Gender", bg=bg_color, fg=label_color).grid(row=2, sticky=tk.W, pady=2)
tk.Label(root, text="Contact Number", bg=bg_color, fg=label_color).grid(row=3, sticky=tk.W, pady=2)
tk.Label(root, text="Location", bg=bg_color, fg=label_color).grid(row=4, sticky=tk.W, pady=2)

entry_name = tk.Entry(root, bg=entry_bg_color)
entry_age = tk.Entry(root, bg=entry_bg_color)
entry_gender = tk.Entry(root, bg=entry_bg_color)
entry_contact = tk.Entry(root, bg=entry_bg_color)
entry_location = tk.Entry(root, bg=entry_bg_color)

entry_name.grid(row=0, column=1, pady=2, padx=5)
entry_age.grid(row=1, column=1, pady=2, padx=5)
entry_gender.grid(row=2, column=1, pady=2, padx=5)
entry_contact.grid(row=3, column=1, pady=2, padx=5)
entry_location.grid(row=4, column=1, pady=2, padx=5)

# Create and place the next button with colors
tk.Button(root, text="Next", command=submit, bg=button_color, fg=button_text_color).grid(row=5, column=1, pady=10)

# Run the application
root.mainloop()
