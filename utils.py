import random

def bemVindo(nome):
     return 'Bem vindo ao jogo do pedra, papel e tesoura ' + nome + "!"

def sua_escolha(opcao):
    if opcao == "Pedra":
         return 'Então você vai escolher Pedra!'
    elif opcao == "Papel":
         return 'Então você vai escolher Papel!'
    elif opcao == "Tesoura":
         return 'Então você vai escolher Tesoura!'
    else:
         return
 
    
def escolha_aleatoria(lista):
     return random.choice(lista)

def comparacao(opcao_jogador, opcao_maquina):
     if opcao_jogador == opcao_maquina:
          return "Empate!" 
     elif opcao_jogador == "Pedra" and opcao_maquina == "Tesoura":
          return "Você ganhou!!"
     elif opcao_jogador == "Pedra" and opcao_maquina == "Papel":
          return "Você pedeu:("
     elif opcao_jogador == "Papel" and opcao_maquina == "Pedra":
          return "Você ganhou!!"
     elif opcao_jogador == "Papel" and opcao_maquina == "Tesoura":
          return "Você pedeu:("
     elif opcao_jogador == "Tesoura" and opcao_maquina == "Papel":
          return "Você ganhou!!"
     elif opcao_jogador == "Tesoura" and opcao_maquina == "Pedra":
          return "Você pedeu:("
     
     