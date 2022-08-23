
from functions import conversao_bytes, monitorar, info
from psutil import * 
import time
import os
from functions import codeCleaner;
from cadastroLogin import cadastro, login
from dash import dashboard
from functions import insertPeriodico
import threading

from gerarGraficos import gerarGraficoDisco


def menu(userId, nome, serialNumber):
    threading.Thread(target=insertPeriodico, kwargs={'serialNumber':serialNumber} ).start()

    os.system(codeCleaner)

    opcaoUser = input(f"\033[1mHardware Monitor\033[0m\n\n Bem vindo(a) {nome} !!\n\n[1] - Monitorar processos atuais da máquina \n[2] - Verificar Informações sobre o dispositivo\n[3] - Análise de dados\n[4] - Sair\n\n\033[1mUsuário:\033[0m ")


    while opcaoUser == "1":
        os.system(codeCleaner)
        res = input("\033[1Como você deseja visualizar os dados?\033[0m \n\n[1] - Painel \n[2] - Informações detalhadas \n[3] - Sair\n\n\033[1mUsuário:\033[0m ")

        if res == "1":
            print("Atenção, você está prestes a entrar no painel. Para sair pressione CTRL + C")
            time.sleep(2)
            opcaoUser = dashboard()
        elif res == "2":
            opcaoUser = monitorar()
            

    while opcaoUser == "2":
        opcaoUser = info()
    while opcaoUser == "3":
        os.system(codeCleaner)
        res = input("\033[1Qual equipamento deseja efetuar a análise?\033[0m \n\n[1] - CPU \n[2] - Memória RAM \n[3] - Disco\n[4] - Sair\n\n\033[1mUsuário:\033[0m ")

        if res == "1":
            res = input("\033[1CPU?\033[0m \n\n[1] - Porcentagem de uso \n[2] - Frequência \n[3] - Sair\n\n\033[1mUsuário:\033[0m ")
            if res == "1":
                print("Atenção! Preparando seus dados para análise...")
                time.sleep(2)

            if res == "2":
                print("Atenção! Preparando seus dados para análise...")
                time.sleep(2)

        if res == "2":
            print("Atenção! Preparando seus dados para análise...")
            time.sleep(2)

        if res == "3":
            print("Atenção! Preparando seus dados para análise...")
            time.sleep(2)

            gerarGraficoDisco()

                


    while opcaoUser == "4":
        main()
        exit()
    while opcaoUser != 1 and opcaoUser != 2 and opcaoUser != 3 and opcaoUser != 4:
        menu(userId, nome, serialNumber)

def main():
    os.system(codeCleaner)

    opcao1tela = input("\033[1mHardware Monitor - BEM VINDO \033[0m\n\n[1] - Entrar \n[2] - Cadastar \n[3] - Sair\n\n\033[1mUsuário:\033[0m ")

    if opcao1tela == "1":
        dados = login()
        userId = dados[0]
        nomeUser = dados[1]
        serialNumber = dados[2]
        menu(userId, nomeUser, serialNumber)
    elif opcao1tela == "2":
        cadastro()
        main()
    elif opcao1tela == "3":
        print("Obrigado por utilizar nosso serviços")
        time.sleep(1)
        exit()
    else: 
        print("Opção Inválida")
        main()

    
print(r"""
         ___________
        ||         ||            _______
        ||  HDWR   ||           | _____ |
        || MONITOR ||           ||_____||
        ||_________||           |  ___  |
        |  + + + +  |           | |___| |
            _|_|_   \           |       |
        (_____)   \          |       |
                    \    ___  |       |
            ______  \__/   \_|       |
            |   _  |      _/  |       |
            |  ( ) |     /    |_______|
            |___|__|    /         
                \_____/

""") 

time.sleep(2)

    
main()