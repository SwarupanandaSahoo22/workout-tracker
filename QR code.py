#QR code

# import qrcode

# url = input("Enter the URL: ").strip()
# file_path = r"C:\Users\Acer\OneDrive\python\qrcode.png"

# qr = qrcode.QRCode()
# qr.add_data(url)

# img = qr.make_image()
# img.save(file_path)

# print("QR Code was created successfully!")









import qrcode

url = input("Enter your URL: ").strip()
file_path = r"C:\Users\Acer\OneDrive\python\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR was created successfully")