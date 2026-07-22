from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


print("="*70)
print("             IMAGE HISTOGRAM ANALYSIS")
print("="*70)

# Input images
original_path = input("Enter Original Image  : ")
encrypted_path = input("Enter Encrypted Image : ")

# Read images
original = Image.open(original_path).convert("RGB")
encrypted = Image.open(encrypted_path).convert("RGB")


# Convert images to numpy arrays
original = np.array(original)
encrypted = np.array(encrypted)


# Extract RGB channels
orig_r = original[:, :, 0]
orig_g = original[:, :, 1]
orig_b = original[:, :, 2]

enc_r = encrypted[:, :, 0]
enc_g = encrypted[:, :, 1]
enc_b = encrypted[:, :, 2]


plt.figure(figsize=(12, 8))


# Original Histogram
plt.subplot(2, 1, 1)

plt.hist(orig_r.ravel(), bins=256, alpha=0.5, label="Red")
plt.hist(orig_g.ravel(), bins=256, alpha=0.5, label="Green")
plt.hist(orig_b.ravel(), bins=256, alpha=0.5, label="Blue")

plt.title("Original Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()


# Encrypted Histogram
plt.subplot(2, 1, 2)

plt.hist(enc_r.ravel(), bins=256, alpha=0.5, label="Red")
plt.hist(enc_g.ravel(), bins=256, alpha=0.5, label="Green")
plt.hist(enc_b.ravel(), bins=256, alpha=0.5, label="Blue")

plt.title("Encrypted Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()


plt.tight_layout()

plt.savefig("histogram_analysis.png", dpi=300)

plt.show()


print("\nHistogram analysis completed!")
print("Saved as: histogram_analysis.png")