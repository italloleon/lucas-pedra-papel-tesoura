import utils
lista = ["Tesoura","Papel","Tesoura"]

nome = (input("Insira seu nome: "))


print(utils.bemVindo(nome))

opcao_jogador = (input("Oque você vai escolher?: "))

print(utils.sua_escolha(opcao_jogador))

opcao_maquina = utils.escolha_aleatoria(lista)

print(f"A opção da maquina foi essa:{opcao_maquina} ")

print(utils.comparacao(opcao_jogador, opcao_maquina))


     

     






