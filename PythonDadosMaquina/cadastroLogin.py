import getpass
import os
import time
from database import *
from functions import codeCleaner, conversao_bytes, randomSerial
import cpuinfo
from psutil import *
import platform



def login():
    os.system(codeCleaner)
    print('\033[1mLogin\033[0m \n\n')
    user = input("User: ")
    senha = getpass.getpass("Senha: ")

    query = f"SELECT idUsuario, nome, serialNumber FROM Usuario JOIN maquina ON fkUsuario = idUsuario where usuario = '{user}' and senha = MD5('{senha}');"
    
    dados = select(query)

    if type(dados) == type(None):
        print('\033[1mFalha no login\033[0m\n\nUsuário ou senha inválidos')
        time.sleep(2)
        login()

    else: 
        os.system(codeCleaner)
        print("\033[1mSucesso no Login\033[0m\n\nLogin feito com sucesso\nAbrindo menu inicial...\n")
        userId = dados[0]
        nomeUser = dados[1]
        serialNumber = dados[2]
        time.sleep(2)
        return userId, nomeUser, serialNumber



def cadastro():
    os.system(codeCleaner)
    print('\033[1mCadastro\033[0m \n\n')
    nome = input("Nome: ")
    user = input("User: ")
    senha = getpass.getpass("Senha: ")
    confSenha = getpass.getpass("Confirme a senha: ")

    if senha == confSenha:
        query = f"INSERT INTO Usuario VALUES (NULL, '{nome}', '{user}', MD5('{senha}'));"

        retorno = insert(query)
        if retorno == 1:
            os.system(codeCleaner)
            print('\033[1mCadastro\033[0m\n\nCadastro realizado com sucesso!')
            time.sleep(2)
            os.system(codeCleaner)
            print("Para prosseguir é necessário que recolhamos algumas informações sobre sua máquina... \n\n Aguarde alguns instantes enquanto esse processo é realizado\n\n")
            queryId = f"SELECT idUsuario FROM Usuario where nome = '{nome}' and senha = MD5('{senha}');"
            dados = select(queryId)
            idUsuario = dados[0]
            dados = cadastroComponentes(idUsuario)

            if dados:
                return 0
            else:
                cadastro()

        else:
            print('Username já é utlizado!')
            time.sleep(2)
            cadastro()

    else:
        print("As senhas não coincidem")
        time.sleep(1)
        cadastro()


def cadastroComponentes(idUsuario):
    
    sistema = platform.system()

    particoes = []
    if sistema == "Windows":
        for part in disk_partitions(all=False): # identificando partições
            if part[0] == "F:\\":
                break
            else:
                particoes.append(part[0])
    elif sistema == "Linux":
        particoes.append("/")

    porcentagemOcupados = []
    for j in particoes:
        porcentagemOcupados.append(disk_usage(j).percent)

    freqCpu = f'{round(cpu_freq().max, 0)}Mhz'
    freqMinCpu = f'{cpu_freq().min, 0}Mhz'
    qtdCores = cpu_count()
    qtdThreads = cpu_count(logical=False)
    processador = cpuinfo.get_cpu_info()['brand_raw']
    discoPrincipal = particoes[0]
    capacidadeDiscoPrincipal = porcentagemOcupados[0]
    memoriaTotal = f'{conversao_bytes(virtual_memory().total, 3)}GB'

    arquitetura = cpuinfo.get_cpu_info()['arch']
    if arquitetura == "X86_32":
        arquitetura = "32 bits"
    elif arquitetura == "X86_64":
        arquitetura = "64 bits"

    serial = randomSerial()

    if sistema == "Windows":
        query = f"INSERT INTO maquina VALUES ('{serial}', {idUsuario}, '{sistema}', '{processador}', {qtdCores}, {qtdThreads}, '{freqCpu}', '{freqMinCpu}', '{memoriaTotal}', '{discoPrincipal}\\', '{capacidadeDiscoPrincipal}')"
    elif sistema == "Linux":
        query = f"INSERT INTO maquina VALUES ('{serial}', {idUsuario}, '{sistema}', '{processador}', {qtdCores}, {qtdThreads}, '{freqCpu}', '{freqMinCpu}', '{memoriaTotal}', '{discoPrincipal}', '{capacidadeDiscoPrincipal}')"

    time.sleep(2)

    retorno = insert(query)

    if retorno == 1:
        print("Cadastro dos componetes realizado com sucesso, seu cadastro está completo")
        time.sleep(2)
        return True
    else:
        print(retorno)
        print("erro")
        time.sleep(2)
        return False
