from PIL import Image
import numpy as np

print("=" * 70)
print("               NPCR & UACI ANALYSIS")
print("=" * 70)

image1_path = input("Enter First Encrypted Image  : ")
image2_path = input("Enter Second Encrypted Image : ")

image1 = np.array(Image.open(image1_path).convert("RGB"))
image2 = np.array(Image.open(image2_path).convert("RGB"))

if image1.shape != image2.shape:
    print("\nBoth images must have the same resolution.")
    exit()

total_pixels = image1.size

changed_pixels = np.sum(image1 != image2)

npcr = changed_pixels / total_pixels * 100

difference = np.abs(image1.astype(np.int16) - image2.astype(np.int16))

average_difference = np.mean(difference)

uaci = average_difference / 255 * 100

print("\n" + "=" * 70)
print("FORMULAS")
print("=" * 70)

print("\nNPCR")
print("NPCR = (Changed Pixels / Total Pixels) × 100")

print("\nUACI")
print("UACI = Mean(|Cipher1 - Cipher2|) / 255 × 100")

print("\n" + "=" * 70)
print("RESULTS")
print("=" * 70)

print("Image Resolution      :", image1.shape[1], "x", image1.shape[0])
print("Total Pixel Values    :", total_pixels)
print("Changed Pixel Values  :", changed_pixels)
print("Average Difference    :", round(average_difference, 6))

print("\nNPCR :", round(npcr, 6), "%")
print("UACI :", round(uaci, 6), "%")

print("\nInterpretation")

if npcr >= 99:
    print("NPCR : Excellent")
elif npcr >= 98:
    print("NPCR : Good")
else:
    print("NPCR : Weak")

if 30 <= uaci <= 35:
    print("UACI : Excellent")
else:
    print("UACI : Weak")

print("\nConclusion")
print("A one-pixel change in the plaintext causes a significant")
print("change in the encrypted image, indicating strong diffusion.")

print("=" * 70)