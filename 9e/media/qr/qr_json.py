import os
import re
import json

base_dir = './img'

with open('name_mapping.json') as f:
    name_mapping = json.load(f)

file_structure = []

for topic_dir in os.listdir(base_dir):
    topic_path = os.path.join(base_dir, topic_dir)
    if os.path.isdir(topic_path):
        topic = {
            "name": topic_dir,
            "subsections": []
        }
        for subtopic_dir in os.listdir(topic_path):
            subtopic_path = os.path.join(topic_path, subtopic_dir)
            if os.path.isdir(subtopic_path):
                subtopic = {
                    "name": subtopic_dir,
                    "images": sorted([img for img in os.listdir(subtopic_path) if img.endswith('.eps')], key=lambda x: int(re.search(r'\d+', x).group()))
                }
                topic["subsections"].append(subtopic)
        file_structure.append(topic)

with open('file_structure.json', 'w') as f:
    json.dump(file_structure, f, indent=4)