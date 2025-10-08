#classes.py

import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa o módulo de caixas de diálogo
from tkinter import ttk  # Importa o módulo ttk para widgets modernos
import random  # Importa o módulo random para gerar números aleatórios
import string  # Importa o módulo string para aceder a conjuntos de caracteres
from constantes import *  # Importa todas as constantes definidas no arquivo constantes.py

class PasswordGeneratorApp:
    def __init__(self, janela):
        self.janela = janela  # Inicializa a janela principal
        self.janela.title("Gerador de Passwords")  # Define o título da janela
        self.janela.configure(bg=COR_FUNDO)  # Define a cor de fundo da janela
        self.janela.geometry('400x400')  # Define o tamanho inicial da janela

        self.style = ttk.Style()  # Cria um objeto de estilo para personalizar widgets
        self._configurar_estilo()  # Chama o método para configurar os estilos

        # Inicializa as variáveis de controle
        self.comprimento_var = tk.StringVar(value="12")  # Variável para o comprimento da password
        self.maiusculas_var = tk.BooleanVar(value=True)  # Variável para incluir maiúsculas
        self.minusculas_var = tk.BooleanVar(value=True)  # Variável para incluir minúsculas
        self.numeros_var = tk.BooleanVar(value=True)  # Variável para incluir números
        self.simbolos_var = tk.BooleanVar(value=True)  # Variável para incluir símbolos
        self.resultado = tk.StringVar()  # Variável para armazenar a password gerada

        self._criar_widgets()  # Chama o método para criar os elementos da interface

    def _configurar_estilo(self):
        self.style.theme_use('clam')  # Define o tema base para os widgets
        # Configura o estilo dos botões
        self.style.configure('TButton', padding=PADDING, font=FONTE)
        self.style.map('TButton',
            background=[('active', FUNDO_BTN_ATIVO), ('!active', FUNDO_BTN_INATIVO)],
            foreground=[('active', 'white'), ('!active', 'white')])
        # Configura o estilo das checkboxes
        self.style.configure('TCheckbutton', font=FONTE, background=COR_FUNDO, foreground=COR_TEXTO)
        # Configura o estilo das labels
        self.style.configure('TLabel', font=FONTE, background=COR_FUNDO, foreground=COR_TEXTO)
        # Configura o estilo das spinboxes
        self.style.configure('TSpinbox', padding=5, background='white')
        # Configura o estilo dos frames
        self.style.configure('TFrame', background=COR_FUNDO)

    def _criar_widgets(self):
        # Cria o frame principal
        main_frame = ttk.Frame(self.janela, padding="20", style='TFrame')
        main_frame.pack(fill='both', expand=True)

        # Cria e configura o spinbox para selecionar o comprimento
        ttk.Label(main_frame, text="Comprimento da password:").pack()
        ttk.Spinbox(main_frame, from_=8, to=18, textvariable=self.comprimento_var, width=20).pack(pady=5)

        # Cria o frame para as checkboxes
        check_frame = ttk.Frame(main_frame, style='TFrame')
        check_frame.pack(pady=10)

        # Cria as checkboxes para as opções de caracteres
        ttk.Checkbutton(check_frame, text="Incluir Maiúsculas", variable=self.maiusculas_var).pack()
        ttk.Checkbutton(check_frame, text="Incluir Minúsculas", variable=self.minusculas_var).pack()
        ttk.Checkbutton(check_frame, text="Incluir Números", variable=self.numeros_var).pack()
        ttk.Checkbutton(check_frame, text="Incluir Símbolos", variable=self.simbolos_var).pack()

        # Cria o frame para os botões
        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.pack(pady=10)

        # Cria o botão para gerar a password
        ttk.Button(button_frame, text="Gerar Password", command=self.gerar_password, style='TButton').pack(pady=10)

        # Cria o campo de texto para mostrar a password gerada
        entry = ttk.Entry(button_frame, textvariable=self.resultado, width=40, state="readonly", font=FONTE)
        entry.pack(pady=10)

        # Cria o botão para copiar a password
        ttk.Button(button_frame, text="Copiar Password", command=self.copiar_password, style='TButton').pack(pady=5)

    def gerar_password(self):
        comprimento = int(self.comprimento_var.get())  # Obtém o comprimento desejado
        caracteres = []  # Lista para armazenar os caracteres possíveis

        # Adiciona os tipos de caracteres selecionados
        if self.maiusculas_var.get():
            caracteres += list(string.ascii_uppercase)
        if self.minusculas_var.get():
            caracteres += list(string.ascii_lowercase)
        if self.numeros_var.get():
            caracteres += list(string.digits)
        if self.simbolos_var.get():
            caracteres += list(string.punctuation)

        # Verifica se pelo menos um tipo de caractere foi selecionado
        if not caracteres:
            messagebox.showwarning("Atenção", "Selecione pelo menos um tipo de caractere!")
            return

        # Gera a password aleatória
        password = ''.join(random.choices(caracteres, k=comprimento))
        self.resultado.set(password)  # Atualiza o campo de resultado

    def copiar_password(self):
        self.janela.clipboard_clear()  # Limpa a área de transferência
        self.janela.clipboard_append(self.resultado.get())  # Copia a password para a área de transferência
        self.janela.update()  # Atualiza a janela
        messagebox.showinfo("Copiado", "Password copiada para a área de transferência!")  # Mostra mensagem de confirmação
