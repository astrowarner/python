import qrcode
from PIL import Image

# Your URL or text to encode in the QR code
data = "www.google.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="pink", back_color="white")

# Save the image
img.save("my_qrcode.png")

# Optionally, display the image
img.show()
