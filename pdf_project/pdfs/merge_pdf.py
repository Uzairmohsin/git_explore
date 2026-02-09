import os
from pypdf import PdfReader, PdfWriter

def merge_pdfs():
    writer = PdfWriter()

    script_dir = os.path.dirname(os.path.abspath(__file__))

    for file in os.listdir(script_dir):
        if file.endswith(".pdf"):
            file_path = os.path.join(script_dir, file)
            print("Merging:", file)

            reader = PdfReader(file_path)
            for page in reader.pages:
                writer.add_page(page)

    if len(writer.pages) == 0:
        print("No pages were added. Check input PDFs.")
        return

    output_path = os.path.join(script_dir, "merged_output.pdf")
    with open(output_path, "wb") as f:
        writer.write(f)

    print("PDFs merged successfully!")

merge_pdfs()

# # Other way

# from PyPDF2 import PdfWriter
# import os

# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()