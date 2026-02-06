import os
from pypdf import PdfReader, PdfWriter

def merge_pdfs(input_folder, output_pdf):
    writer = PdfWriter()

    for file in os.listdir(input_folder):
        if file.endwith(".pdf"):
            file_path = os.path.join(input_folder, file)
            reader = PdfReader(file_path)

            for page in reader.pages:
                writer.add_page(page)
    with open (output_pdf, "wb") as output_file:
        writer.write(output_file)

    print("pdf merged success fully")
merge_pdfs("pdfs", "merged_output.pdf")