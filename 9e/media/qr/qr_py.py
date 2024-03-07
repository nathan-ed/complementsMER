import os
import json

def calculate_columns(num_images):
    if num_images <= 4:
        return num_images
    elif num_images <= 8:
        return 3 if num_images < 7 else 4
    else:
        return num_images // 3 if num_images % 3 == 0 else (num_images // 3) + 1

# Read the name mapping and the file structure from their respective JSON files
with open('name_mapping.json', 'r') as f:
    name_mapping = json.load(f)

with open('file_structure.json', 'r') as f:
    file_structure = json.load(f)

# Open the main TeX file and write the LaTeX code for including the images
with open('main.tex', 'w') as f:
    with open('preamble.tex', 'r') as preamble:
        f.write(preamble.read())
    f.write('\\begin{document}\n\\newcommand{\\chapterName}{Quiz Moodle}\n\\newcommand{\\serieName}{QR-code}\n')  # Include the begin document command

    for section in file_structure:
        section_name = name_mapping["topics"].get(section["name"], section["name"])
        f.write('\\section*{' + section_name + '}\n')  # Add the section title

        for subsection in section["subsections"]:
            subsection_name = name_mapping["subtopics"].get(subsection["name"], section["name"])
            images = subsection["images"]
            
            num_cols = calculate_columns(len(images))  # Adjust the number of columns

            if len(images) > 1:
                f.write('\\begin{qmoodle}{' + subsection_name + '}{' + str(num_cols) + '}{\n')
                for i, image in enumerate(images):
                    image_name = os.path.splitext(image)[0]  # Remove file extension
                    f.write('\t\\begin{center}\n\t\tQ' + str(i + 1) + '\n\n')
                    f.write('\t\t\\includegraphics[scale=1]{' + 'img/' + section["name"] + '/' + subsection["name"] + '/' + image_name + '}\n\t\\end{center}\n')
                f.write('}\n\\end{qmoodle}\n\n')
            else:
                image = images[0]
                image_name = os.path.splitext(image)[0]  # Remove file extension
                f.write('\\begin{qmun}{' + subsection_name + '}{\n')
                f.write('\t\\begin{center}\n\t\tQ1\n\n')
                f.write('\t\t\\includegraphics[scale=1]{' + 'img/' + section["name"] + '/' + subsection["name"] + '/' + image_name + '}\n\t\\end{center}\n')
                f.write('}\n\\end{qmun}\n\n')
                
    f.write('\\end{document}\n')
