from lorenz.lorenz import generate_lorenz_key
from BB84.bb84 import run_bb84
from aes_image_encryt import encrypt_image

chaotic_key = generate_lorenz_key()
result = run_bb84(chaotic_key[:64])
encrypt_image(result["alice_key"])