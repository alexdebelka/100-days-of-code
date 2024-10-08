import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
from datetime import datetime
import os
import zipfile
from io import BytesIO

# Function to generate a certificate with an image background using fixed positions and centered text
def generate_certificate_image(name, cert_number, period, template_path, output_path):
    # Open the certificate template image
    image = Image.open(template_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load the custom fonts (Arial used here, but you can replace with Times New Roman if needed)
    font_name = ImageFont.truetype("./streamlit-unicert-certificate/Arial.ttf", 150)  # Font for name
    font_period = ImageFont.truetype("./streamlit-unicert-certificate/Arial.ttf", 50)  # Font for the period and date
    font_small = ImageFont.truetype("./streamlit-unicert-certificate/Arial.ttf", 50)  # Font for the certificate number

    # Get the current date
    issue_date = datetime.now().strftime("%d/%m/%Y")

    # Define the size of the blue box
    box_top = 1550
    box_bottom = 390
    box_left = 390
    box_right = 1800

    # Calculate the center of the blue box
    box_center_x = box_top + box_bottom / 2
    box_center_y = box_left + box_right / 2

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

    # Save the edited image as a PNG file (temporary)
    png_output_file = f"{output_path}/{name}_Certificat_{cert_number}.png"
    image.save(png_output_file)

    # Convert the PNG to PDF using FPDF
    pdf_output_file = f"{output_path}/{name}_Certificat_{cert_number}.pdf"
    convert_image_to_pdf(png_output_file, pdf_output_file)

    return pdf_output_file

# Function to convert the PNG certificate to PDF using FPDF
def convert_image_to_pdf(png_file, pdf_output_file):
    pdf = FPDF(orientation='L', unit='pt', format='A4')  # Landscape, A4 size
    pdf.add_page()

    # Add the image to the PDF
    pdf.image(png_file, x=0, y=0, w=842, h=595)  # A4 size dimensions in points

    # Save the PDF
    pdf.output(pdf_output_file)

# Function to generate the certificate number
def generate_cert_number(current_number):
    return f"PA-{str(current_number).zfill(4)}"

# Save the last used certificate number
def save_last_cert_number(last_number):
    with open("last_cert_number.txt", "w") as f:
        f.write(str(last_number))

# Load the last used certificate number
def load_last_cert_number():
    try:
        with open("last_cert_number.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 1  # Start with 1 if not found

# Function to create a zip file of generated PDFs
def create_zip_of_pdfs(generated_pdfs):
    memory_zip = BytesIO()
    with zipfile.ZipFile(memory_zip, "w") as zf:
        for name, pdf_file in generated_pdfs:
            zf.write(pdf_file, os.path.basename(pdf_file))
    memory_zip.seek(0)
    return memory_zip

# Streamlit app
def main():
    st.title("Certificate Generator")

    # Step 1: Upload the certificate template
    template_file = st.file_uploader("Upload Certificate Template (PNG)", type=["png"])
    if template_file:
        template_path = "unicert_certificate_v3.png"
        with open(template_path, "wb") as f:
            f.write(template_file.getbuffer())

    # Step 2: Upload the CSV file with names and period dates
    csv_file = st.file_uploader("Upload CSV with Names and Period Dates", type=["csv"])
    if csv_file:
        df = pd.read_csv(csv_file)

    # Step 3: Input starting certificate number
    start_number = load_last_cert_number()
    st.write(f"Starting certificate number: {start_number}")
    
    # Add a reset button to reset the certificate number to 101
    if st.button("Reset Certificate Number to 101"):
        save_last_cert_number(100)
        st.success("Certificate number reset to 101")

    # Step 4: Generate certificates when the button is clicked
    if st.button("Generate Certificates"):
        output_path = "output"
        os.makedirs(output_path, exist_ok=True)
        current_number = start_number

        # A list to hold generated PDFs for the zip file
        generated_pdfs = []

        # Loop through the dataframe and generate certificates
        for index, row in df.iterrows():
            name = row['name']
            period = row['period']
            cert_number = generate_cert_number(current_number)
            pdf_file = generate_certificate_image(name, cert_number, period, template_path, output_path)

            # Store the generated PDF for the zip file
            generated_pdfs.append((name, pdf_file))

            current_number += 1

        # Save the last certificate number
        save_last_cert_number(current_number - 1)

        st.success(f"Certificates generated and saved to {output_path}.")

        # Create a zip file containing all generated PDFs
        zip_file = create_zip_of_pdfs(generated_pdfs)

        # Provide a download button for the zip file
        st.download_button(
            label="Download All Certificates as ZIP",
            data=zip_file,
            file_name="certificates.zip",
            mime="application/zip"
        )

if __name__ == "__main__":
    main()
