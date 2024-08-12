from PIL import Image
import random

def encrypt_image(input_image_path, output_image_path, key):
    with Image.open(input_image_path) as img:
        pixels = list(img.getdata())

    random.seed(key)
    random.shuffle(pixels)

    encrypted_image = Image.new(img.mode, img.size)
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    with Image.open(input_image_path) as img:
        pixels = list(img.getdata())

    random.seed(key)
    random.shuffle(pixels)

    decrypted_image = Image.new(img.mode, img.size)
    decrypted_image.putdata(pixels)
    decrypted_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "input.png"
    output_image_path = "output.png"
    key = 12345  # Use the same key for encryption and decryption

    # Encrypt the image
    print("Encrypting image...")
    encrypt_image(input_image_path, output_image_path, key)
    print("Image encrypted successfully!")

    # Decrypt the image
    print("Decrypting image...")
    decrypt_image(output_image_path, input_image_path, key)
    print("Image decrypted successfully!")
