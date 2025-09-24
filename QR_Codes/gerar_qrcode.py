import requests
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

BASE_URL = "https://qmove-net.onrender.com/api"  # rotas da API

# Buscar todas as motos cadastradas
response = requests.get(f"{BASE_URL}/motos")
if response.status_code != 200:
    print("Erro ao buscar motos:", response.text)
    exit()

motos = response.json()

output_folder = "qrcodes_motos"
os.makedirs(output_folder, exist_ok=True)

try:
    font = ImageFont.truetype("arial.ttf", 28)
except:
    font = ImageFont.load_default()

for moto in motos:
    moto_id = moto["id"]
    placa = moto["placa"]

    # Dados que vão dentro do QR Code (aqui você pode escolher se aponta pro front ou API)
    qr_data = f"{BASE_URL}/motos/{moto_id}"

    qr = qrcode.make(qr_data).convert("RGB")
    largura, altura = qr.size
    nova_altura = altura + 60

    imagem_final = Image.new("RGB", (largura, nova_altura), "white")
    imagem_final.paste(qr, (0, 0))

    draw = ImageDraw.Draw(imagem_final)
    texto = f"Moto {placa}"
    largura_texto = draw.textlength(texto, font=font)
    pos_x = (largura - largura_texto) // 2
    pos_y = altura + 15

    draw.text((pos_x, pos_y), texto, fill="black", font=font)

    caminho = f"{output_folder}/moto_{moto_id}.png"
    imagem_final.save(caminho)

print("✅ QR Codes gerados com sucesso na pasta 'qrcodes_motos'.")
