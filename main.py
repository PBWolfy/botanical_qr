import qrcode
import os

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data("https://npgsweb.ars-grin.gov/gringlobal/taxon/taxonomydetail?id=27923")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('img.png')
