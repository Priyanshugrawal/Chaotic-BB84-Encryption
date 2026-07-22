from PIL import Image
import os

image_path = input("Enter Original Image : ").strip()

# Check if file exists exactly as entered
if not os.path.isfile(image_path):
    print("\nError: Image not found!")
    exit()

image = Image.open(image_path).convert("RGB")

width, height = image.size

# Center pixel
x = width // 2
y = height // 2

# Read original pixel
r, g, b = image.getpixel((x, y))

print("\n" + "=" * 60)
print("               MODIFY ONE PIXEL")
print("=" * 60)

print(f"Image Size        : {width} x {height}")
print(f"Modified Position : ({x}, {y})")
print(f"Original Pixel    : ({r}, {g}, {b})")

# Modify only one pixel
new_r = (r + 1) % 256
new_g = (g + 1) % 256
new_b = (b + 1) % 256

image.putpixel((x, y), (new_r, new_g, new_b))

print(f"Modified Pixel    : ({new_r}, {new_g}, {new_b})")

output_file = "modified.png"
image.save(output_file)

print("\nModified image saved successfully.")
print("Output File :", output_file)
print("=" * 60)