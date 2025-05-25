import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

motos_cadastradas = [
    { "id": 1, "placa": "ABC1234", "modelo": "Mottu-e", "setor_cadastrado": "Manutenção","setor_atual": "Disponível","status": "No setor incorreto"},
    { "id": 2, "placa": "DEF5678", "modelo": "Mottu Pop", "setor_cadastrado": "Manutenção","setor_atual": "Manutenção", "status": "No pátio" },
    { "id": 3, "placa": "GHI9012", "modelo": "Mottu-e","setor_cadastrado": "Disponível","setor_atual": "Disponível", "status": "No pátio" },
    { "id": 4, "placa": "JKL3456", "modelo": "Mottu Sport","setor_cadastrado": "Triagem","setor_atual": "Manutenção", "status": "No setor incorreto" },
    { "id": 5, "placa": "MNO7890", "modelo": "Mottu Sport", "setor_cadastrado": "Disponível","setor_atual": "Disponível","status": "No pátio" }
]

output_folder = "qrcodes_motos"
os.makedirs(output_folder, exist_ok=True)

try:
    font = ImageFont.truetype("arial.ttf", 28)
except:
    font = ImageFont.load_default()

for moto in motos_cadastradas:
    moto_id = moto["id"]
    placa = moto["placa"]
    qr_data = f"https://meuappmotos.com/veiculo?placa={placa}"
    
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
    
    caminho = f"{output_folder}/moto_{moto_id}.png"
    imagem_final.save(caminho)

print("QR Codes gerados com sucesso na pasta 'qrcodes_motos'.")
from IPython.display import display, Image as IPImage

for moto in motos_cadastradas:
    moto_id = moto["id"]
    print(f"Moto {moto_id} - {moto['placa']}")
    display(IPImage(filename=f"qrcodes_motos/moto_{moto_id}.png"))
