# 🏍️ Gerador de QR Codes para Motos – Python

Este script em Python gera imagens de QR Code com base nos dados de motos cadastradas. Cada imagem contém um QR Code com uma legenda personalizada indicando o ID da moto.

---

## 🐍 Requisitos

- Python 3 instalado
- Bibliotecas:
  - `qrcode`
  - `Pillow` (PIL)

---

## ⚙️ Instalação das dependências

Execute o comando abaixo no terminal para instalar as bibliotecas necessárias:

```bash
pip install qrcode Pillow
```

---

## ▶️ Como Executar

1. Execute o script no terminal:

```bash
python3 gerar_qrcode.py
```

3. Após a execução, os arquivos de imagem serão gerados automaticamente dentro da pasta `qrcodes_motos/`.

---

## 📲 Integração com App Mobile

Este gerador é pensado para funcionar em conjunto com o app **React Native com Expo**, que poderá utilizar a câmera para escanear os QR Codes gerados e realizar a leitura ou navegação de acordo com o ID da moto.

---
