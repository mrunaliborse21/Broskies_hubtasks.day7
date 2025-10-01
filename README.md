# Broskies_hubtasks.day7

📝 Task 7: Image Resizer Tool

📌 Objective:
The main objective of this task was to build a Python script that can automatically resize and convert multiple images in batch. This tool helps to speed up repetitive image processing tasks, especially useful in scenarios like preparing images for websites, machine learning datasets, or optimizing storage space.


---

🛠 What I Built:

I developed an automated Image Resizer Tool using Python.
The tool scans through a folder containing images, resizes each image to a specific target size, converts it into a uniform format (JPEG), and then saves all processed images into a separate output folder.

This ensures that all images are standardized in terms of dimensions and format, making them easier to manage and use for further applications.


---

⚡ How I Built It:

1. Folder Reading with os Module:

Used the os library to read all image files from the input directory.

Automatically created an output folder if it didn’t already exist.



2. Image Processing with Pillow (PIL) Library:

Opened each image using PIL.Image.open().

Resized the image to the target dimensions using the resize() method.

Converted images to .jpg format for uniformity.



3. Batch Processing:

Implemented a loop to process multiple images one by one without manual intervention.

Saved each resized image into the output folder with proper naming.



4. Error Handling:

Added simple error handling to skip problematic files and ensure the script runs smoothly for all valid images.





---

🎯 Why I Built It:

Manually resizing and converting images one by one is time-consuming and prone to errors.

This tool automates the entire process, improving efficiency and productivity.

It is especially useful for developers, designers, or data scientists who often work with large image datasets.

It demonstrates practical use of Python scripting, file handling, and image processing, which are essential skills for backend and automation roles.



---

🏆 Outcome:

Successfully automated the batch resizing and conversion of images.

Reduced manual work and standardized image processing.

Gained hands-on experience with Python’s os module and Pillow library.

Built a reusable and scalable tool that can be adapted for different image processing requirements.



✅ Skills Used: Python, Pillow (PIL), Automation, File Handling, Image Processing
📂 Tools: Python 3, Pillow Library, VS Code / Terminal
