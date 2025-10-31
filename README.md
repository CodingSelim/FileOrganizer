# 🗂️ File Organizer

A Python automation script that cleans up messy folders by organizing files into categorized subfolders based on their extensions.  
Perfect for managing cluttered directories like **Downloads**, **Desktop**, or **Documents**.

---

## Features
- Automatically detects file types (`.pdf`, `.jpg`, `.zip`, etc.)
- Creates subfolders such as `pdf_files`, `jpg_files`, `zip_files`
- Moves each file into its respective folder
- Handles unknown or extensionless files by placing them in an `others_files` folder
- Safe → skips any existing folders

---

## Skills Learned
- Working with `os` and `shutil` modules  
- File system navigation and automation  
- String manipulation and error handling  
- Writing reusable functions and clean code

---

##  How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/CodingSelim/FileOrganizer.git
   cd FileOrganizer
2. **Run the script** 
   ```bash
   python file_organizer.py
   ```
3. **Enter the path of the folder you want to organize when prompted:**
    ```
    Enter the path of the folder to organize: /path/to/your/folder
    ```
4. **Watch it automatically create folders like:**
   - `pdf_files`
   - `jpg_files`
   - `zip_files`
   - `others_files`


# Example output
```bash
Moved: resume.pdf → /home/selim/Downloads/pdf_files
Moved: photo.png → /home/selim/Downloads/png_files
Moved: archive.zip → /home/selim/Downloads/zip_files
```

# Requirements
- Python 3.x
- No external libraries required


