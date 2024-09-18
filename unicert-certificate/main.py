from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

# Function to generate a certificate with an image background using fixed positions and centered text
def generate_certificate_image(name, cert_number, period, template_path, output_path):
    # Open the certificate template image
    image = Image.open(template_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load the custom fonts (Arial used here, but you can replace with Times New Roman if needed)
    font_name = ImageFont.truetype("Arial.ttf", 150)  # Font for name
    font_period = ImageFont.truetype("Arial.ttf", 50)  # Font for the period and date
    font_small = ImageFont.truetype("Arial.ttf", 50)  # Font for the certificate number

    # Get the current date
    issue_date = datetime.now().strftime("%d/%m/%Y")

    # Define the size of the blue box
    box_top = 1550
    box_bottom = 390
    box_left = 390
    box_right = 1800

    # Calculate the center of the blue box
    box_center_x = box_top + box_bottom/ 2
    box_center_y = box_left + box_right/ 2

    # Calculate the bounding box for the text (this gives the dimensions of the text)
    name_bbox = draw.textbbox((0, 0), name, font=font_name)
    name_width = name_bbox[2] - name_bbox[0]
    name_height = name_bbox[3] - name_bbox[1]

    # Adjust position to center the text within the box
    name_position = (box_center_x - name_width / 2, box_center_y - name_height / 2)

    # Certificate number and period remain fixed as before
    cert_number_position = (2985, 469)
    period_position = (248, 2346)
    issue_date_position = (1366, 2346)

    # Add the participant's name to the certificate (centered in the blue box)
    draw.text(name_position, name, font=font_name, fill="black")

    # Add the certificate number to the certificate
    draw.text(cert_number_position, cert_number, font=font_small, fill="black")

    # Add the period to the certificate
    draw.text(period_position, f"Perioada: {period}", font=font_period, fill="black")

    # Add the issue date to the certificate
    draw.text(issue_date_position, f"Data emiterii: {issue_date}", font=font_period, fill="black")

    # Save the edited image as a new file
    output_file = f"{output_path}/{name}_Certificat_{cert_number}.png"
    image.save(output_file)

    print(f"Certificate generated: {output_file}")


# Function to generate the certificate number
def generate_cert_number(current_number):
    return f"PA-{str(current_number).zfill(4)}"


# Main loop to input names and generate certificates
def main():
    template_path = "gg-cert.png"  # Path to your uploaded image template
    output_path = "output"  # Folder where certificates will be saved

    os.makedirs(output_path, exist_ok=True)  # Create output folder if it doesn't exist

    start_number = 1  # Starting certificate number
    while True:
        # Get the participant's name
        participant_name = input("Enter the participant's name (or 'exit' to stop): ")

        if participant_name.lower() == 'exit':
            break

        # Get the period
        period = input("Enter the period (e.g., 01/09/2024 - 05/09/2024): ")

        # Generate certificate number
        cert_number = generate_cert_number(start_number)
        start_number += 1

        # Generate and export the certificate
        generate_certificate_image(participant_name, cert_number, period, template_path, output_path)


if __name__ == "__main__":
    main()
