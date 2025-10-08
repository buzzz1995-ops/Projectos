#app.py

from tkinter import *  # Importa todos os módulos do tkinter
from classes import PasswordGeneratorApp  # Importa a classe PasswordGeneratorApp do arquivo classes.py

def main():

    # Cria a janela principal do aplicativo usando o tkinter
    janela = Tk()

    # Cria uma instância da classe PasswordGeneratorApp, passando a janela como parâmetro
    app = PasswordGeneratorApp(janela)

    # Inicia o loop principal da aplicação, mantendo a janela aberta e respondendo a eventos
    janela.mainloop()


# Verifica se o arquivo está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":

    main()  # Chama a função principal do programa