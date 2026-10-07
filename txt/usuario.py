'''
Exercício 01: Meu Primeiro Arquivo de Texto (Criando com Modo "w")
Crie um programa que solicite ao usuário o seu nome e sua idade.
Abra um arquivo chamado "usuario.txt" no modo de escrita "w" com encoding="utf-8".
Escreva as informações no arquivo formatadas em duas linhas: "Nome: [Nome]" e "Idade: [Idade]".
Utilize a quebra de linha \n ao final de cada frase e confirme na tela: "Dados salvos com sucesso!".
'''

nome = input("qual seu nome?: ")
idade = int(input("digite sua idade: "))

with open ("usuario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome: {nome} | idade: {idade}\n")

    print("dados adicionados com sucesso.")