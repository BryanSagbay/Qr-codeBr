import qrcode

url= "https://github.com/BryanSagbay"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5 
)

qr.add_data(url)
qr.make(fit=True)
 
imagenqr = qr.make_image(fill='black', back_color='white') 
imagenqr.save('qrcode.png')