import webview
from funcao_api import Api  # supondo que sua classe Api está em api.py

if __name__ == '__main__':
    api = Api()

    # Cria a janela com seu HTML
    webview.create_window(
        "Molecule Builder",
        "index.html",  # caminho para seu arquivo HTML
        width=800,
        height=600,
        resizable=True,
        js_api=api  # conecta a API Python ao JS
    )

    # Inicia o app
    webview.start()
