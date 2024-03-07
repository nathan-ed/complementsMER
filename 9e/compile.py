import json
import os
import subprocess
from PyPDF2 import PdfFileMerger

# Define json dictionary file
json_dict = "dict.json"

# Create output folder if it doesn't exist
if not os.path.exists("output"):
    os.mkdir("output")

# Open the json file
with open(json_dict, "r") as f:
    data = json.load(f)

# List to keep track of created PDFs
pdf_files = []

# Iterate over all keys in the json file (preserving order)
for filename in data.keys():
    # Check if the .tex file exists and starts with 'NO'
    if filename.startswith("GM-01") and os.path.exists(f"{filename}.tex"):
        # Compile the tex file
        subprocess.run(f'pdflatex --shell-escape -interaction=nonstopmode "{filename}.tex"', shell=True)
        
        # Get the new name from the json dictionary
        new_name = data[filename]
        
        # If there is a corresponding new name
        if new_name:
            # Rename the pdf and move it to the output folder
            os.rename(f"{filename}.pdf", f"output/{new_name}.pdf")
            pdf_files.append(f"output/{new_name}.pdf")
        else:
            # If no new name in the json, just move the file
            os.rename(f"{filename}.pdf", f"output/{filename}.pdf")
            pdf_files.append(f"output/{filename}.pdf")

        # Remove the generated files except for the .pdf
        for ext in [".aux", ".log", ".out", ".toc"]:
            if os.path.exists(f"{filename}{ext}"):
                os.remove(f"{filename}{ext}")

# Create a PDF merger object
merger = PdfFileMerger()

# Merge all the PDFs
for pdf in pdf_files:
    merger.append(pdf)

# Write the merged PDF to a file
merger.write("output/merged_output.pdf")
merger.close()