import qrcode
from PIL import Image

# URL for which we need to generate the QR code
url = 'google.com'

# Generate a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="white", back_color="yellow")

# Save the image to a file in a specific location
file_path = "google_qr_code.png"  # You can change this to your desired file path
img.save(file_path)

# Display the image
img.show()

# If you want to open the saved image using the default image viewer
# import os
# os.system(f'open {file_path}')  # For MacOS
# os.system(f'start {file_path}')  # For Windows
