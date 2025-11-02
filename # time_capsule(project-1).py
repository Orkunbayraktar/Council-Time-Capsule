import datetime
from PIL import Image
import os


def add_message(message):
    try:
        current_datetime = datetime.datetime.now()
        text = input("Enter your message: ")
        print()

        attach_image = input("Do you want to attach an image (yes/no): ").strip().lower()
        image_file = ""

        if attach_image in ['yes', 'y']:
            image_path = input("Enter the path to the image file: ").strip()
            if os.path.exist(image_path):
                try:
                    img = Image.open(image_path)
                    img.verify()

                    if not os.path.exists("capsule_images"):
                        os.makedirs("capsule_images")
                    timestamp = current_datetime.strftime("%Y%m%d%H%M%S")
                    file_extension = os.path.splitext(image_path)[1]
                    image_file = f"capsule_images/image_{timestamp}{file_extension}"

                    img = Image.open(image_path)
                    img.save(image_file)
                    print(f"Image atached: {image_file}")
                    print()
                except Exception as e:
                    print(f"Error when processing image: {e}")
                    print()
                    print("Message will be saved without an image.")
                    image_file = ""
            else:
                print("Image file not found. Message will be saved without an image.")
                print()        
    

            