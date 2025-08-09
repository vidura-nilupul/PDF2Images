import fitz  # PyMuPDF
import os

# Path to your PDF
pdf_path = r"path"


# Output folder
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

# Check if the PDF file exists
if not os.path.exists(pdf_path):
    print(f"Error: The file '{pdf_path}' does not exist.")
else:
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Loop through each page
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        pix = page.get_pixmap(dpi=300)  # Set DPI for image quality
        image_path = os.path.join(output_folder, f"page_{page_number + 1}.png")
        pix.save(image_path)
        print(f"Saved: {image_path}")

    pdf_document.close()

    print("PDF conversion completed!")
