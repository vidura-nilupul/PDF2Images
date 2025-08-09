import fitz  # PyMuPDF
import os
from pathlib import Path
import ttkbootstrap as tb
from tkinter import filedialog
from ttkbootstrap.constants import *

# ------------------------
# PDF to Images Converter
# ------------------------
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
    status_label.config(text="", foreground="")

    if not pdf_path or not output_folder:
        status_label.config(text="Please select both a PDF file and an output folder.", foreground="red")
        return

    if not os.path.exists(pdf_path):
        status_label.config(text="The selected PDF does not exist.", foreground="red")
        return

    try:
        pdf_document = fitz.open(pdf_path)
        total_pages = len(pdf_document)
        pdf_name = Path(pdf_path).stem

        progress_bar["maximum"] = total_pages
        progress_bar["value"] = 0

        for page_number in range(total_pages):
            page = pdf_document[page_number]
            pix = page.get_pixmap(dpi=300)
            image_filename = f"{pdf_name}_page_{page_number + 1}.png"
            image_path = os.path.join(output_folder, image_filename)
            pix.save(image_path)

            progress_bar["value"] = page_number + 1
            root.update_idletasks()

        pdf_document.close()

        # Success message
        status_label.config(text=f"Conversion completed! Saved in: {output_folder}", foreground="green")

        # Reset for next run
        pdf_path_var.set("")
        output_folder_var.set("")
        progress_bar["value"] = 0

    except Exception as e:
        status_label.config(text=f"Error: {e}", foreground="red")


def toggle_theme():
    if style.theme.name == "darkly":
        style.theme_use("flatly")  # Light theme
        theme_toggle_btn.config(text="Switch to Dark Mode")
    else:
        style.theme_use("darkly")  # Dark theme
        theme_toggle_btn.config(text="Switch to Light Mode")

# ------------------------
# GUI Setup
# ------------------------
root = tb.Window(themename="darkly")  # Start in dark mode
root.title("PDF2Image")
root.geometry("")  # Let Tkinter size the window automatically
root.resizable(False, False)

style = tb.Style()

# Variables
pdf_path_var = tb.StringVar()
output_folder_var = tb.StringVar()

# Title
tb.Label(root, text="PDF2Image", font=("Segoe UI", 20, "bold")).pack(pady=10)

# PDF selection
tb.Label(root, text="PDF File:").pack(anchor="w", padx=20)
tb.Entry(root, textvariable=pdf_path_var, width=50).pack(padx=20, pady=5)
tb.Button(root, text="Browse PDF", bootstyle=PRIMARY, command=select_pdf).pack(pady=(0, 10))

# Output folder selection
tb.Label(root, text="Output Folder:").pack(anchor="w", padx=20)
tb.Entry(root, textvariable=output_folder_var, width=50).pack(padx=20, pady=5)
tb.Button(root, text="Browse Folder", bootstyle=INFO, command=select_output_folder).pack(pady=(0, 15))

# Convert button
tb.Button(root, text="Convert to Images", bootstyle=SUCCESS, command=convert_pdf_to_images, width=20).pack(pady=5)

# Progress bar
progress_bar = tb.Progressbar(root, length=400, mode="determinate", bootstyle=SUCCESS)
progress_bar.pack(pady=10)

# Status label
status_label = tb.Label(root, text="", font=("Segoe UI", 10))
status_label.pack()

# Theme toggle
theme_toggle_btn = tb.Button(root, text="Switch to Light Mode", bootstyle=SECONDARY, command=toggle_theme)
theme_toggle_btn.pack(pady=5)

# Footer / Branding
footer_frame = tb.Frame(root)
footer_frame.pack(side="bottom", fill="x", pady=5)
tb.Label(footer_frame, text="Product of The Solution Z", font=("Segoe UI", 8), anchor="e").pack(side="right", padx=10)

root.mainloop()
# End of PDF2Image.py