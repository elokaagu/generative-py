from PIL import Image

def generate_art():
    print("Generating Art")
    image = Image.new("RGB", (128, 128), (255, 255, 255))
    image.save("test_image.png")

if __name__ == "__main__":
    generate_art()