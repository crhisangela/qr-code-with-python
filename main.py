import qrcode

#what do you whant in your qr?
data = 'https://www.instagram.com/crhisangela/'

## simplified
# img = qrcode.make(data)

qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'grey', back_color = 'white')

#saving
img.save(f"qrcode.png")
