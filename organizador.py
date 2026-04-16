# organizador.py
# Script para organizar automaticamente uma pasta (ex.: Downloads)
# Desenvolvido por Barbara Carvalho

import os
import shutil

# ===================== CONFIGURAÇÃO =====================
# Altere o caminho abaixo para a pasta que você deseja organizar
# Exemplo Windows: r"C:\Users\SeuNome\Downloads"
# Exemplo Linux/Mac: "/home/seunome/Downloads"
pasta_alvo = r"C:\Users\barbara\Downloads"
# =========================================================

# Mapeamento de extensões para as pastas de destino
MAPA_EXTENSOES = {
    # Documentos
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".doc": "Documentos",
    ".txt": "Documentos",
    ".xlsx": "Planilhas",
    ".xls": "Planilhas",
    ".pptx": "Apresentações",
    ".ppt": "Apresentações",
    # Imagens
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".bmp": "Imagens",
    # Vídeos
    ".mp4": "Vídeos",
    ".avi": "Vídeos",
    ".mkv": "Vídeos",
    ".mov": "Vídeos",
    # Compactados e instaladores
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",
    ".exe": "Instaladores",
    ".msi": "Instaladores",
}

def organizar():
    # Verifica se a pasta informada existe
    if not os.path.exists(pasta_alvo):
        print(f"Erro: O diretório '{pasta_alvo}' não foi encontrado.")
        print("Verifique o caminho e tente novamente.")
        return

    arquivos_movidos = 0

    # Percorre todos os itens dentro da pasta alvo
    for item in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, item)

        # Processa apenas arquivos (ignora subpastas)
        if os.path.isfile(caminho_completo):
            # Separa o nome do arquivo da extensão
            nome_arquivo, extensao = os.path.splitext(item)
            extensao = extensao.lower()  # Converte para minúsculas

            # Verifica se a extensão está no nosso mapeamento
            if extensao in MAPA_EXTENSOES:
                pasta_destino_nome = MAPA_EXTENSOES[extensao]
                caminho_destino = os.path.join(pasta_alvo, pasta_destino_nome)

                # Cria a pasta de destino se ela não existir
                if not os.path.exists(caminho_destino):
                    os.makedirs(caminho_destino)
                    print(f"📁 Pasta criada: {pasta_destino_nome}")

                # Move o arquivo para a pasta correspondente
                destino_final = os.path.join(caminho_destino, item)
                try:
                    shutil.move(caminho_completo, destino_final)
                    print(f"➡️  {item}  ->  {pasta_destino_nome}/")
                    arquivos_movidos += 1
                except Exception as e:
                    print(f"⚠️  Não foi possível mover '{item}': {e}")

    print("\n" + "=" * 50)
    print(f"✅ Organização concluída! Total de arquivos movidos: {arquivos_movidos}")
    print("=" * 50)

if __name__ == "__main__":
    organizar()
    input("\nPressione Enter para sair...")
