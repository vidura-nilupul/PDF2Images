import fitz  # PyMuPDF
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

def select_pdf():
    file_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    pdf_path_var.set(file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    output_folder_var.set(folder_path)

def convert_pdf_to_images():
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()

    if not pdf_path or not output_folder:
        messagebox.showerror("Error", "Please select both a PDF file and an output folder.")
        return

    if not os.path.exists(pdf_path):
        messagebox.showerror("Error", f"The file '{pdf_path}' does not exist.")
        return

    try:
        pdf_document = fitz.open(pdf_path)
        pdf_name = Path(pdf_path).stem  # File name without extension

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            pix = page.get_pixmap(dpi=300)  # High-quality DPI
            image_filename = f"{pdf_name}_page_{page_number + 1}.png"
            image_path = os.path.join(output_folder, image_filename)
            pix.save(image_path)

        pdf_document.close()
        messagebox.showinfo("Success", f"PDF converted successfully!\nImages saved in:\n{output_folder}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI
root = tk.Tk()
root.title("PDF to Images Converter")
root.geometry("500x250")
root.resizable(False, False)

# Variables
pdf_path_var = tk.StringVar()
output_folder_var = tk.StringVar()

# PDF File selection
tk.Label(root, text="PDF File:").pack(pady=(10, 0))
tk.Entry(root, textvariable=pdf_path_var, width=50).pack(pady=5)
tk.Button(root, text="Browse PDF", command=select_pdf).pack()

# Output folder selection
tk.Label(root, text="Output Folder:").pack(pady=(10, 0))
tk.Entry(root, textvariable=output_folder_var, width=50).pack(pady=5)
tk.Button(root, text="Browse Folder", command=select_output_folder).pack()

# Convert button
tk.Button(root, text="Convert to Images", command=convert_pdf_to_images, bg="green", fg="white", width=20).pack(pady=20)

root.mainloop()
