import re
import os

folder_path = '/path/to/your/folder'

markdown_files = [file for file in os.listdir(folder_path) if file.endswith('.md')]

for file_name in markdown_files:
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    markdown_content = re.sub(r'<img[^>]+src="([^"]+)"[^>]*>', r'![](\1)', markdown_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

print("Done")
