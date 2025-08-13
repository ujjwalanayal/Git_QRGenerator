from PIL import Image, ImageDraw, ImageFont
import qrcode

github_url = input("Enter the URL you want to encode in the QR: ").strip()
username = input("Enter the username to display below the QR: ").strip()

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data(github_url)
qr.make()

img = qr.make_image(fill_color="#0D1117", back_color="white").convert('RGB')

logo = Image.open("git.png")
logo_size = 160
logo = logo.resize((logo_size, logo_size))

qr_width, qr_height = img.size
logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
img.paste(logo, logo_pos)

extra_height = 20
final_img = Image.new("RGB", (qr_width, qr_height + extra_height), "white")
final_img.paste(img, (0, 0))

draw = ImageDraw.Draw(final_img)
try:
    font = ImageFont.truetype("tahoma.ttf", 12)
except:
    font = ImageFont.load_default()

text = username
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

text_x = (qr_width - text_width) // 2
text_y = qr_height + (extra_height - text_height) //  4 - bbox[3]

draw.text((text_x, text_y), text, fill="black", font=font)
final_img.save("github_profile_qr.png")

print("✅ GitHub profile QR code saved as github_profile_qr.png")
