import qrcode
from pyzbar.pyzbar import  decode
from PIL import Image



# code the data inside QR code
data = "don't forget to"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='white')

# Codes will be saved in this folder path
img.save('C:/Users/Steph/OneDrive/Pictures/QRcodes/reese1.png')


# ===================

decodeimage = Image.open("C:/Users/Steph/OneDrive/Pictures/QRcodes/reese1.png")
result = decode(decodeimage)
print(result)