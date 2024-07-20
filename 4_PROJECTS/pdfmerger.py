import PyPDF2
import os

# New path to the resources folder
resource_folder = "PROJECTS\Resources"

# List of PDF files in the resources folder
pdfiles = [os.path.join(resource_folder, "M1.pdf"),
           os.path.join(resource_folder, "M2.pdf"),
           os.path.join(resource_folder, "M3.pdf"),
           os.path.join(resource_folder, "M4.pdf"),
           os.path.join(resource_folder, "M5.pdf")]

merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    with open(filename, 'rb') as pdfile:
        pdfReader = PyPDF2.PdfReader(pdfile)
        merger.append(pdfReader)

output_file = os.path.join(resource_folder, "Your_merged_pdf.pdf")
with open(output_file, 'wb') as merged_pdf:
    merger.write(merged_pdf)

# Open the merged PDF using the default PDF viewer
if os.name == 'nt':  # Windows
    os.startfile(output_file)
else:  # Linux or macOS
    import subprocess
    subprocess.Popen(['xdg-open', output_file])
