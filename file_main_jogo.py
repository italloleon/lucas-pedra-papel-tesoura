import utils
lista = ["Pedra","Papel","Tesoura"]

nome = input("Insira seu nome: ")


print(utils.bemVindo(nome))

print(utils.escolha_por_numero(nome))

opcao_jogador = input("Oque você vai escolher? 1, 2 ou 3: ")

print(utils.sua_escolha(opcao_jogador))

opcao_maquina = utils.escolha_aleatoria(lista)

print(f"A opção da maquina foi essa:{opcao_maquina} ")

print(utils.comparacao(opcao_jogador, opcao_maquina))


     

     






