import hashlib
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_image(bb84_key):

    print("\n" + "=" * 70)
    print("           AES-256 CTR IMAGE ENCRYPTION")
    print("=" * 70)

    # SHA-256 Key
    aes_key = hashlib.sha256(bb84_key.encode()).digest()

    print("\nBB84 Sifted Key")
    print("-" * 70)
    print(bb84_key)

    print("\nSHA-256 AES Key")
    print("-" * 70)
    print(aes_key.hex())

    print("\nAES Key Length :", len(aes_key) * 8, "bits")

    # Input Image
    image_path = input("\nEnter Image Path : ")

    image = Image.open(image_path).convert("RGB")

    width, height = image.size

    print("\nImage Loaded Successfully")
    print("Image Size :", width, "x", height)

    image_bytes = image.tobytes()

    # Random Nonce
    nonce = get_random_bytes(8)

    print("\nNonce")
    print("-" * 70)
    print(nonce.hex())

    # AES-256 CTR
    cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)

    encrypted_bytes = cipher.encrypt(image_bytes)

    encrypted_image = Image.frombytes(
        "RGB",
        (width, height),
        encrypted_bytes
    )

    output_file = "encrypted_visual.png"

    encrypted_image.save(output_file)

    print("\nImage Encrypted Successfully")
    print("Encrypted Image :", output_file)

    return {
        "image": output_file,
        "nonce": nonce
    }