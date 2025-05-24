import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
from motos import motos_cadastradas

output_folder = "qrcodes_motos"
os.makedirs(output_folder, exist_ok=True)

try:
    font = ImageFont.truetype("arial.ttf", 28)
except:
    font = ImageFont.load_default()

for moto in motos_cadastradas:
    moto_id = moto["id moto"]
    qr_data = ""
    
    qr = qrcode.make(qr_data).convert("RGB")  
    
    largura, altura = qr.size
    nova_altura = altura + 60
    
    imagem_final = Image.new("RGB", (largura, nova_altura), "white")
    imagem_final.paste(qr, (0, 0))
    
    draw = ImageDraw.Draw(imagem_final)
    texto = f"Moto {moto_id}"
    largura_texto = draw.textlength(texto, font=font)
    pos_x = (largura - largura_texto) // 2
    pos_y = altura + 15
    
    draw.text((pos_x, pos_y), texto, fill="black", font=font)
    
    imagem_final.save(f"{output_folder}/moto_{moto_id}.png")

print("QR Codes gerados com sucesso na pasta 'qrcodes_motos'.")
