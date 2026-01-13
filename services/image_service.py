def salvar_imagem(caminho: str, conteudo: bytes, data: str) -> None:
    with open(caminho, 'wb') as f:
        f.write(conteudo)

def baixar_imagem(url: str, data: str, title: str, timeout: int = 10) -> bytes:
    import requests
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        nome_arquivo = data + "_" + title + "_" + obter_nome_arquivo_da_url(url)

        print(f"Baixando imagem: {nome_arquivo}")

        salvar_imagem("output/images/" + nome_arquivo, response.content, data)
        return response.content
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao baixar a imagem: {e}")
    
def obter_nome_arquivo_da_url(url: str) -> str:
    import os
    return os.path.basename(url)