from PIL import Image
import math
from collections import Counter
import os


def calculate_entropy(image_path):

    if not os.path.exists(image_path):
        image_path = os.path.join("..", image_path)

    image = Image.open(image_path).convert("RGB")

    data = image.tobytes()

    total_bytes = len(data)

    frequency = Counter(data)

    entropy = 0

    for count in frequency.values():

        probability = count / total_bytes

        entropy -= probability * math.log2(probability)

    print("\n" + "=" * 60)
    print("        INFORMATION ENTROPY")
    print("=" * 60)

    print("Image :", image_path)
    print("Image Size :", image.width, "x", image.height)
    print("Total Bytes :", total_bytes)
    print("Entropy :", round(entropy, 6), "bits")

    print("\nInterpretation")

    if entropy >= 7.99:
        print("Excellent Encryption")
    elif entropy >= 7.95:
        print("Good Encryption")
    else:
        print("Weak Encryption")

    print("=" * 60)


image_path = input("Enter Encrypted Image : ").strip()

calculate_entropy(image_path)