import requests
import qrcode
from PIL import Image, ImageDraw, ImageFont
import sqlite3
import os

# Colocar a URL da API para pegar a lista de motos
api_url = "http://seu-servidor/api/motos"

# Função para fazer a requisição à API e obter a lista de motos
def get_motos():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # Retorna os dados da API (lista de motos)
    else:
        print("Erro ao buscar motos:", response.status_code)
        return []

# Função para gerar o QR Code e salvar a imagem
def generate_qr_code(moto_id, save_directory):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # URL do QR Code (moto_id é o ID da moto)
    url = f"http://seusistema.com/moto/{moto_id}"

    qr.add_data(url)
    qr.make(fit=True)

    # Gerar a imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')

    # Adicionar o código (ID da moto) abaixo do QR Code
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # Usando a fonte padrão (pode substituir por uma personalizada)
    text = f"Código: {moto_id}"
    text_width, text_height = draw.textsize(text, font)
    text_position = ((img.width - text_width) // 2, img.height - text_height - 10)
    draw.text(text_position, text, font=font, fill='black')

    # Criar diretório se não existir
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Salvar a imagem com o nome do código da moto
    img_path = os.path.join(save_directory, f"qrcode_{moto_id}.png")
    img.save(img_path)

    return img_path  # Retorna o caminho do QR Code gerado

# Função para salvar o QR Code no banco de dados
def save_qr_code_in_db(moto_id, img_url):
    # Conectando ao banco de dados (substitua com o seu banco de dados real)
    conn = sqlite3.connect('seu_banco_de_dados.db')  # Altere para o caminho do seu banco
    cursor = conn.cursor()

    # Certifique-se de que a tabela qr_codes exista
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS qr_codes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        moto_id TEXT NOT NULL,
        qr_code_url TEXT NOT NULL
    )
    """)

    # Inserir o link do QR Code e o ID da moto
    insert_query = "INSERT INTO qr_codes (moto_id, qr_code_url) VALUES (?, ?)"
    cursor.execute(insert_query, (moto_id, img_url))

    # Commit e fechamento da conexão
    conn.commit()
    conn.close()

# Função principal que executa o processo de geração e armazenamento dos QR Codes
def main():
    motos = get_motos()  # Obter a lista de motos da API
    if motos:
        save_directory = "qrcodes"  # Diretório onde os QR Codes serão salvos

        for moto in motos:
            moto_id = moto['id']  # ID da moto, que será usado na URL do QR Code
            print(f"Gerando QR Code para a moto: {moto_id}")

            # Gerar o QR Code e salvar no servidor
            img_path = generate_qr_code(moto_id, save_directory)

            # Salvar a URL do QR Code no banco de dados
            qr_code_url = f"/{save_directory}/{os.path.basename(img_path)}"  # URL relativa
            save_qr_code_in_db(moto_id, qr_code_url)

            print(f"QR Code para a moto {moto_id} gerado e salvo com sucesso!")

if __name__ == "__main__":
    main()
