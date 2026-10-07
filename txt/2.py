'''
Exercício 02: Diário de Bordo (Adicionando Texto com Modo "a")
Crie um programa que permita ao usuário registrar uma anotação rápida.
Solicite que o usuário digite uma frase ou mensagem do dia.
Abra o arquivo "diario.txt" no modo de anexo "a" com encoding="utf-8".
Adicione a mensagem do usuário ao final do arquivo acompanhada de uma quebra de linha \n.
Exiba a mensagem: "Anotação adicionada ao diário!".
'''

frase_do_dia = input("digite a frase/mensagem do dia: ").strip().title()

with open ("diario.txt", "a", encoding="utf-8") as  arquivo:
    arquivo.write(f"a frase/mensagem do dia é: {frase_do_dia}\n")

    print("frase adicionada cum sucesso.")