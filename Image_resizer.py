import os
from PIL import Image

# 📁 Input folder containing images
input_folder = "images_input"
# 📁 Output folder to save resized images
output_folder = "images_output"

# 🧭 Desired size for resizing (width, height)
target_size = (800, 600)   # you can change as needed

# ✅ Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 🌀 Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Build full file path
    file_path = os.path.join(input_folder, filename)

    # Check if it’s a valid image file
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        try:
            # Open image
            img = Image.open(file_path)

            # Resize image
            img_resized = img.resize(target_size)

            # Convert to JPEG format (optional)
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)

            # Save resized image
            img_resized.save(output_path, "JPEG")
            print(f"✅ Resized and saved: {output_filename}")

        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

print("\n🎯 All images resized and saved successfully!")
