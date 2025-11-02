import datetime
from PIL import Image
import os


def add_message(messages):
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
    
        print("Select unlock date: ")
        print()
        print(f"Current date and time: {current_datetime.strftime('%Y-%m-%d %H:%M')}")
        print()

        date_time_input = input("Enter date and time (YYYY MM DD HH MM): ")
        year, month, day, hour, minute = map(int, date_time_input.split())
        
        unlock_datetime = datetime.datetime(year, month, day, hour, minute)
        if unlock_datetime <= current_datetime:
            print("Error: Unlock date must be in the future!")
            print()
            print("Your message was not saved. Please try again.")
            return

        print(f"Your message is saved until: {unlock_datetime}")    
        print()
    except ValueError:
        print("Invalid input! Please enter valid numbers for date and time.")
        print()
        return
    
    message = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}|{text}|{image_file}"
    messages.append(message)
    print()
    print("Message sealed in time capsule!")
    print()
    save_capsule(messages)

    def save_capsule(messages):
        with open("capsule.txt", "w") as file:
            for msg in messages:
                file.write(msg + "\n")
    
    def load_capsule():
        messages = []
        try:
            with open("capsule.txt") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        messages.append(line)
        except FileNotFoundError:
            print("No capsule found. Starting fresh!")
            print()
        return messages
    
    def is_unlocked(date_part):
        try:

            unlock_dt = datetime.datetime.strptime(date_part, "%Y-%m-%d %H:%M")
        except ValueError:
            try:
                
                unlock_dt = datetime.datetime.strptime(date_part.strip(), "%Y-%m-%d-%H:%M")
            except ValueError:
                return False
            return datetime.datetime.now() >= unlock_dt
        
        def view_unlocked_messages(messages):
            unlocked = []
            for msg in messages:
                parts = msg.split("|", 2)
                if len(parts) >= 2:
                    date_part = parts[0]
                    text = parts[1]
                    image_file = parts[2] if len(parts) > 2 else ""



            
