import qrcode
img = qrcode.make('https://rs4anti.github.io/hairtech-follicles/')
img.save('qr_buono.png')
