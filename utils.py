import random

def bemVindo(nome):
     return '𝘽𝙚𝙢 𝙫𝙞𝙣𝙙𝙤 𝙖𝙤 𝙟𝙤𝙜𝙤 𝙙𝙤 𝙥𝙚𝙙𝙧𝙖 𝙥𝙖𝙥𝙚𝙡 𝙚 𝙩𝙚𝙨𝙤𝙪𝙧𝙖 ' + nome + "!"     

def escolha_por_numero(nome):
     return f"Seguinte {nome}, voce tem que escolher entre os números 1, 2 e 3 que são respectivamente Pedra, Papel e Tesoura"

def sua_escolha(opcao):
    if opcao == "1":
         return 'Então você vai escolher Pedra!'
    elif opcao == "2":
         return 'Então você vai escolher Papel!'
    elif opcao == "3":
         return 'Então você vai escolher Tesoura!'
    else:
         return


def escolha_aleatoria(lista):
     return random.choice(lista)

def comparacao(opcao_jogador, opcao_maquina):
     if opcao_jogador == opcao_maquina:
          return "Empate!" 
     elif opcao_jogador == "1" and opcao_maquina == "Tesoura":
          return "Você ganhou!!"
     elif opcao_jogador == "1" and opcao_maquina == "Papel":
          return "Você pedeu:("
     elif opcao_jogador == "2" and opcao_maquina == "Pedra":
          return "Você ganhou!!"
     elif opcao_jogador == "2" and opcao_maquina == "Tesoura":
          return "Você pedeu:("
     elif opcao_jogador == "3" and opcao_maquina == "Papel":
          return "Você ganhou!!"
     elif opcao_jogador == "3" and opcao_maquina == "Pedra":
          return "Você pedeu:("
     
     