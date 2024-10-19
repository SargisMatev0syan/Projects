import qrcode

data = input("Enter some text or url: ").strip()
filename = input("Enter the filename:" ).strip() # bacati hamar
qr = qrcode.QRCode(box_size= 10 ,    border = 4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color ='white')
image.save(filename)
print(f'QR code saved as {filename}')