# qrcode(pip install qrcode)
# image(pip install image)

import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # the version means that code high the number bigger the code image and complicated picture
    box_size = 10, # box size where qr code will be
    border = 5 #it is the white part of image, border in all 4 sides with white color
)
data = "https://staff.am/en/trainings"   #https code


qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill='black', back_color = 'white'    )
img.save('qr_01.png')