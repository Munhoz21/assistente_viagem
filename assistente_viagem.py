import flet as ft
from google import genai
from dotenv import load_dotenv
import os

# --- CONFIGURAÇÃO ---
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Em 2026, precisamos garantir que o cliente use a versão estável
client = genai.Client(api_key=API_KEY, http_options={'api_version': 'v1'})

def main(page: ft.Page):
    page.title = "Assistente de Viagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    destino = ft.TextField(label="Para onde vamos?", width=300)
    interesses = ft.TextField(label="O que você gosta? (ex: Museus)", width=300)
    dias = ft.TextField(label="Quantos dias?", width=300)
    
    # Usamos um container para o texto para evitar erros de renderização
    resultado = ft.Text(value="", selectable=True)

    def clique_gerar(e):
        if not destino.value or not interesses.value or not dias.value:
            return
        
        resultado.value = "Consultando o Gemini... aguarde."
        page.update()

        try:
            # Recuperando seu prompt original que funcionava bem
            prompt_completo = f"""
            Crie um roteiro de viagem resumido e direto com base nas seguintes informações:

            Informações fornecidas pelo usuário:
            - Destino: {destino.value}
            - Duração: {dias.value} dias
            - Interesses: {interesses.value}

            Gere um roteiro, dia a dia, usando tópicos. Seja conciso e vá direto ao ponto. Responda em português do Brasil.
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_completo
            )
            resultado.value = response.text
            resultado.value = response.text
        except Exception as err:
            resultado.value = f"Erro persistente: {err}"
        
        page.update()

    page.add(
        ft.Text("Assistente de Viagem", size=30, weight="bold"),
        destino, interesses, dias,
        ft.ElevatedButton("Gerar Roteiro", on_click=clique_gerar),
        ft.Divider(),
        resultado
    )

if __name__ == "__main__":
    ft.app(target=main)