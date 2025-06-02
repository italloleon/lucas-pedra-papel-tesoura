nome = (input("Insira seu nome: "))

def bemVindo(nome):
     return 'Bem vindo ao jogo do pedra, papel e tesoura ' + nome + "!"
print(bemVindo(nome))

opcao = (input("Oque você vai escolher?: "))
def sua_escolha(opcao):
    if opcao == "Pedra":
         return 'Então você vai escolher Pedra!'
    elif opcao == "Papel":
         return 'Então você vai escolher Papel!'
    elif opcao == "Tesoura":
         return 'Então você vai escolher Tesoura!'
    else:
         return
print(sua_escolha(opcao))

     






