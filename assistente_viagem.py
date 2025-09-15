import flet as ft
import google.generativeai as genai
from dotenv import load_dotenv
import os

# --- CONFIGURAÇÃO DA API ---
load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

# --- MODELO DA INTERFACE ---
def main(page: ft.Page):
    page.title = "Assistente de Viagem Inteligente"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    destino_input = ft.TextField(
        label="Destino da Viagem",
        hint_text="Ex: Paris, Tóquio, Nova York",
        width=300
    )

    interesses_input = ft.TextField(
        label="Seus Interesses",
        hint_text="Ex: museus, gastronomia, vida noturna",
        width=300
    )

    duracao_input = ft.TextField(
        label="Duração da Viagem (em dias)",
        hint_text="Ex: 3, 7, 10",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300
    )
    
    # --- NOVO: Área que fará a transição animada ---
    resultado_roteiro = ft.AnimatedSwitcher(
        content=ft.Markdown(value="", selectable=True),
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=300,
        reverse_duration=100
    )
    
    def gerar_roteiro(e):
        destino = destino_input.value
        interesses = interesses_input.value
        duracao = duracao_input.value

        if not destino or not interesses or not duracao:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()
            return
        
        page.snack_bar = ft.SnackBar(ft.Text(f"Gerando roteiro para {destino}..."))
        page.snack_bar.open = True
        page.update()
        
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
Crie um roteiro de viagem resumido e direto com base nas seguintes informações:

Informações fornecidas pelo usuário:
- Destino: {destino}
- Duração: {duracao} dias
- Interesses: {interesses}

Gere um roteiro, dia a dia, usando tópicos. Seja conciso e vá direto ao ponto. Responda em português do Brasil.
"""
            
            response = model.generate_content(prompt)
            
            # --- NOVO: Altera o conteúdo do AnimatedSwitcher ---
            resultado_roteiro.content = ft.Markdown(value=response.text, selectable=True)
            
            page.snack_bar = ft.SnackBar(ft.Text("Roteiro gerado com sucesso!"))
            page.snack_bar.open = True
        
        except Exception as ex:
            # --- NOVO: Altera o conteúdo do AnimatedSwitcher em caso de erro ---
            resultado_roteiro.content = ft.Markdown(value=f"Ocorreu um erro ao gerar o roteiro com o Gemini: {ex}", selectable=True)
            page.snack_bar = ft.SnackBar(ft.Text("Erro ao gerar roteiro."))
            page.snack_bar.open = True

        page.update()

    btn_gerar_roteiro = ft.ElevatedButton(
        text="Gerar Roteiro",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        on_click=gerar_roteiro
    )

    page.add(
        ft.Column(
            [
                ft.Text("Planeje sua próxima viagem!", size=24, weight="bold"),
                ft.Text("Preencha os campos para receber uma sugestão de roteiro.", size=16),
                ft.Container(height=20),
                destino_input,
                interesses_input,
                duracao_input,
                ft.Container(height=20),
                btn_gerar_roteiro,
                ft.Container(height=20),
                ft.Text("Seu roteiro aparecerá aqui:", size=14, weight="bold"),
                resultado_roteiro,
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)