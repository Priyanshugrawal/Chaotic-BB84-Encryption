from PIL import Image
import numpy as np
import os


def correlation(x, y):

    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    covariance = np.mean((x - mean_x) * (y - mean_y))

    sigma_x = np.std(x)
    sigma_y = np.std(y)

    return covariance / (sigma_x * sigma_y)


def calculate_correlation(image_path):

    if not os.path.exists(image_path):
        image_path = os.path.join("..", image_path)

    image = Image.open(image_path).convert("L")

    image = np.array(image)

    horizontal_x = []
    horizontal_y = []

    vertical_x = []
    vertical_y = []

    diagonal_x = []
    diagonal_y = []

    rows, cols = image.shape

    # Horizontal
    for i in range(rows):
        for j in range(cols - 1):
            horizontal_x.append(image[i, j])
            horizontal_y.append(image[i, j + 1])

    # Vertical
    for i in range(rows - 1):
        for j in range(cols):
            vertical_x.append(image[i, j])
            vertical_y.append(image[i + 1, j])

    # Diagonal
    for i in range(rows - 1):
        for j in range(cols - 1):
            diagonal_x.append(image[i, j])
            diagonal_y.append(image[i + 1, j + 1])

    h = correlation(horizontal_x, horizontal_y)
    v = correlation(vertical_x, vertical_y)
    d = correlation(diagonal_x, diagonal_y)

    print("\n" + "=" * 65)
    print("          CORRELATION COEFFICIENT ANALYSIS")
    print("=" * 65)

    print("Image :", image_path)
    print()

    print(f"Horizontal Correlation : {h:.6f}")
    print(f"Vertical Correlation   : {v:.6f}")
    print(f"Diagonal Correlation   : {d:.6f}")

    print("\nInterpretation")

    if abs(h) < 0.01:
        print("Horizontal : Excellent")
    elif abs(h) < 0.05:
        print("Horizontal : Good")
    else:
        print("Horizontal : Weak")

    if abs(v) < 0.01:
        print("Vertical   : Excellent")
    elif abs(v) < 0.05:
        print("Vertical   : Good")
    else:
        print("Vertical   : Weak")

    if abs(d) < 0.01:
        print("Diagonal   : Excellent")
    elif abs(d) < 0.05:
        print("Diagonal   : Good")
    else:
        print("Diagonal   : Weak")

    print("=" * 65)


image_path = input("Enter Encrypted Image : ").strip()

calculate_correlation(image_path)