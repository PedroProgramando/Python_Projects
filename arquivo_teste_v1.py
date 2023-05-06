from unidecode import unidecode

respostas_sim = ['sim', 's', 'yes', 'y', 'claro']
respostas_nao = ['não', 'ñ', 'n', 'no', 'nunca mais']

import time
import os 
import pyinputplus as pyip

def clear_page():
    os.system('cls' if os.name == 'nt' else 
              'clear')



print('Seja bem vindo à central de criação de criaturas!')


lista_criaturas = []

def adicionar_criatura():
    nova_criatura = input('Digite o nome da criatura que deseja adicionar: ').capitalize()
    
    lista_criaturas.append(nova_criatura)

    atributos_criatura = {}
    atributos_criatura['força'] = pyip.inputNum(f'Digite a força da criatura {nova_criatura}: ')
    atributos_criatura['agilidade']= input(f'Digite a agilidade da criatura {nova_criatura}: ')
    atributos_criatura['destreza']= input(f'Digte a destreza da criatura {nova_criatura}: ')
    atributos_criatura['defesa'] = input(f'Digte a Defesa da criatura {nova_criatura}: ')
    atributos_criatura['HP'] = input(f'Digite o HP da criatura {nova_criatura}: ')
    lista_criaturas.append({nova_criatura: atributos_criatura})
    

    with open('copia_teste_listagem_criaturas.txt', 'a') as listagem_criaturas:
        listagem_criaturas.write(nova_criatura + '\n')
    
    return nova_criatura






while True:
    resposta = input('Deseja acrescentar criaturas? (S/N)\n').lower()
    
    if resposta in respostas_nao:
        encerrar_processo = print('Até a proxima, invocador! \n[PROCESSO FINALIZADO]')
        for apagando in range(3, 0, -1):
            clear_page()
            print(f'Até a proxima, invocador!\nApagando tudo em... {apagando}')
            time.sleep(1)
        break
    
    elif resposta in respostas_sim:
        adicionar_criatura()
        


            

    else:
        clear_page()
        print('Você digitou algo incorretamente, tente novamente.')
        continue
