#!/usr/bin/env python3
# jogo_da_forca_tkinter.py com tela inicial e imagem

import random
import tkinter as tk
from tkinter import messagebox

palavras = [
    'python', 'computador', 'programacao', 'desenvolvedor', 'algoritmo',
    'inteligencia', 'aprender', 'telefone', 'internet', 'teclado',
    'janela', 'biblioteca', 'variavel', 'funcao', 'sistema', 'salmao', 'cao', 'lua', 'forca',
    'hardware', 'software', 'rede', 'dados', 'navegador', 'servidor', 'cliente', 'firewall',
    'criptografia', 'engenharia', 'robotica', 'matematica', 'quimica', 'fisica', 'astronomia',
    'planeta', 'galaxia', 'universo', 'estrela', 'cometa', 'asteroide', 'nebulosa', 'gravidade',
    'energia', 'eletricidade', 'corrente', 'resistor', 'condutor', 'isolante', 'transistor',
    'processador', 'memoria', 'disco', 'monitor', 'impressora', 'mouse', 'cabos', 'placa',
    'tela', 'pixel', 'interface', 'aplicativo', 'programa', 'arquivo', 'pasta',
    'sistemaoperacional', 'linux', 'windows', 'macos', 'android', 'ios', 'nuvem', 'banco',
    'dadosrelacionais', 'api', 'funcoes', 'classe', 'objeto', 'variaveis', 'constante', 'compilador',
    'interpretador', 'editor', 'codigo', 'debug', 'teste', 'versao', 'repositorio', 'commit',
    'push', 'pull', 'branch', 'merge', 'deploy', 'redeinterna', 'wifi', 'bluetooth', 'ethernet',
    'sensor', 'motor', 'arduino', 'raspberry', 'drone', 'satelite', 'radar', 'gps',
    'carro', 'bicicleta', 'aviao', 'barco', 'onibus', 'trem', 'metro', 'caminhao',
    'escola', 'universidade', 'hospital', 'mercado', 'livro', 'caderno', 'caneta', 'lapis',
    'borracha', 'mochila', 'professor', 'aluno', 'aula', 'prova', 'trabalho', 'projeto',
    'amigo', 'familia', 'cidade', 'bairro', 'rua', 'praca', 'parque', 'rio', 'montanha',
    'praia', 'ilha', 'deserto', 'floresta', 'animal', 'planta', 'fruta', 'legume', 'comida', 
    'felino', 'anfibio', 'tkinter', 'html'
]

forca_stages = [
    r"""
     _______
    |/      |
    |
    |
    |
    |
    |\    """,
    r"""
     _______
    |/      |
    |      (_)
    |
    |
    |
    |\    """,
    r"""
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |\    """,
    r"""
     _______
    |/      |
    |      (_)
    |      \|
    |       |
    |
    |\    """,
    r"""
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |
    |\    """,
    r"""
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |\    """,
    r"""
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |\    """
]

class ForcaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.configure(bg='maroon')
        self.palavra = ""
        self.letras_certas = set()
        self.letras_erradas = set()
        self.tentativas_max = len(forca_stages)-1

        # ----- FRAME INICIAL -----
        self.frame_home = tk.Frame(root, bg='maroon')
        self.frame_home.pack(fill="both", expand=True)

        # Carregar imagem
        self.img_forca = tk.PhotoImage(file="forca\\forca.png")
        self.label_img = tk.Label(self.frame_home, image=self.img_forca, bg='maroon')
        self.label_img.pack(pady=10)

        tk.Label(self.frame_home,
                 text="Bem-vindo ao Jogo da Forca!",
                 bg='maroon', fg='white', font=("Helvetica", 24)).pack(pady=10)

        instrucoes = (
    'A máquina escolhe uma palavra secreta e desenha espaços em branco representando cada letra.\n'
    'O jogador tenta adivinhar a palavra sugerindo letras do alfabeto.\n'
    'Se a letra existir na palavra, ela é revelada nos espaços corretos.\n'
    'Se a letra não existir, é desenhada uma parte da forca ou do boneco.\n'
    'O jogador perde se o desenho da forca ficar completo antes de descobrir a palavra.\n'
    'O jogador ganha se adivinhar todas as letras da palavra antes que o boneco seja enforcado.\n'
    'Apenas é possível o uso de letras\n'
        )
        tk.Label(self.frame_home,
                 text=instrucoes,
                 bg='maroon', fg='white', font=("Helvetica", 14), justify='left').pack(pady=20)

        tk.Button(self.frame_home,
                  text="Iniciar Jogo",
                  bg='white', fg='maroon',
                  font=("Helvetica", 16),
                  command=self.mostrar_jogo).pack(pady=30)

        # ----- FRAME DO JOGO -----
        self.frame_game = tk.Frame(root, bg='maroon')

        self.frame_top = tk.Frame(self.frame_game, bg='maroon')
        self.frame_top.pack(pady=10)

        self.label_forca = tk.Label(
            self.frame_top,
            text=forca_stages[0],
            bg='maroon', fg='white',
            font=("Courier", 12), justify="left"
        )
        self.label_forca.pack()

        self.label_palavra = tk.Label(
            self.frame_game,
            bg='maroon', fg='white',
            text="", font=("Helvetica", 20)
        )
        self.label_palavra.pack(pady=10)

        self.label_erradas = tk.Label(
            self.frame_game,
            bg='maroon', fg='white',
            text="Letras erradas: ", font=("Helvetica", 12)
        )
        self.label_erradas.pack(pady=5)

        self.entry_letra = tk.Entry(self.frame_game, width=5, font=("Helvetica", 16))
        self.entry_letra.bind("<Return>", self.tentar_letra_event)
        self.entry_letra.pack()

        self.btn_tentar = tk.Button(
            self.frame_game,
            bg='white', fg='maroon',
            text="Tentar", command=self.tentar_letra
        )
        self.btn_tentar.pack(pady=5)

        self.btn_novo = tk.Button(
            self.frame_game,
            bg='white', fg='maroon',
            text="Novo Jogo", command=self.novo_jogo
        )
        self.btn_novo.pack(pady=5)

    # ---------------------------
    def mostrar_jogo(self):
        """Troca da tela inicial para o jogo."""
        self.frame_home.pack_forget()
        self.frame_game.pack(fill="both", expand=True)
        self.novo_jogo()

    def escolher_palavra(self):
        return random.choice(palavras).upper()

    def atualizar_interface(self):
        mostrado = ' '.join([c if c in self.letras_certas else '_' for c in self.palavra])
        self.label_palavra.config(text=mostrado)
        self.label_erradas.config(text="Letras erradas: " + ', '.join(sorted(self.letras_erradas)))
        self.label_forca.config(text=forca_stages[min(len(self.letras_erradas), self.tentativas_max)])

    def tentar_letra(self):
        letra = self.entry_letra.get().strip().upper()
        self.entry_letra.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showinfo("Aviso", "Digite apenas UMA letra.")
            return

        if letra in self.letras_certas or letra in self.letras_erradas:
            messagebox.showinfo("Aviso", "Você já tentou essa letra.")
            return

        if letra in self.palavra:
            self.letras_certas.add(letra)
        else:
            self.letras_erradas.add(letra)

        self.atualizar_interface()
        self.verificar_fim()

    def tentar_letra_event(self, event):
        self.tentar_letra()

    def verificar_fim(self):
        if all([c in self.letras_certas for c in self.palavra]):
            messagebox.showinfo("Vitória", f"Parabéns — você acertou a palavra: {self.palavra}")
            self.novo_jogo()
        elif len(self.letras_erradas) >= self.tentativas_max:
            messagebox.showinfo("Derrota", f"Você perdeu! A palavra era: {self.palavra}")
            self.novo_jogo()

    def novo_jogo(self):
        self.palavra = self.escolher_palavra()
        self.letras_certas = set()
        self.letras_erradas = set()
        self.atualizar_interface()

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = ForcaGUI(root)
    root.iconbitmap("forca\\icon.ico")
    root.mainloop()
