import os
directory = r"c:\Development\personal_portfolio\projects"
for file in os.listdir(directory):
    if file.endswith(".html"):
        filepath = os.path.join(directory, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(", and ", " and ")
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
