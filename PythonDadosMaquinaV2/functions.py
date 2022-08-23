import datetime
import time
from psutil import *
import os
import platform
from database import insert, select
import cpuinfo
from uuid import getnode as get_mac
from random import randint


sistema = platform.system()

if sistema == "Windows":
    codeCleaner = "cls"
elif sistema == "Linux":
    codeCleaner = "clear"

def randomSerial():
    num = randint(100000000,999999999)
    serial = "BRJ" + str(num)
    return serial

def conversao_bytes(valor, tipo):
    if tipo == 1:  # KB
        return valor / 1024
    elif tipo == 2:  # MB
        return valor / 1024 / 1024
    elif tipo == 3:  # GB
        return f'{valor / 1024 / 1024 / 1024: .2f}'


def monitorar():
    while (True):
        try:
            os.system(codeCleaner)
            # MEMORIA RAM
            memoriaTotal = f'{conversao_bytes(virtual_memory().total, 3)}GB'
            memoriaDisponivel = f'{conversao_bytes(virtual_memory().available, 3)}GB'
            memoriaEmUsoPerc = virtual_memory().percent
            usoAtualMemoria = f'{conversao_bytes(virtual_memory().used, 3)}GB'

            # CPU
            usoCpuPorc = f'{cpu_percent()}%'
            usoPorCore = cpu_percent(percpu=True)

            # DISCO
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

            # Print parte da memória
            print("\033[1mInformações de memória\033[0m\n")
            print("\033[1mTotal:\033[0m", memoriaTotal)
            print("\033[1mMemória Disponível:\033[0m", memoriaDisponivel)
            print("\033[1mUso atual:\033[0m", usoAtualMemoria)
            print("\033[1mPorcentagem de uso:\033[0m", memoriaEmUsoPerc)

            print("\n", "-" * 100, "\n")

            # Print CPU
            print("\033[1mInformações de CPU\033[0m\n")
            print("\033[1mUso total:\033[0m ", usoCpuPorc)

            print("\033[1mUso por core:\033[0m")

            for i in enumerate(usoPorCore):
                print(f'CPU_{i[0]}: {i[1]}%')

            print("\n", "-" * 100, "\n")

            # Print disco
            print("\033[1mInformações do disco\033[0m\n")
            print("\033[1mPartições encontradas:\033[0m ")

            for i in enumerate(particoes):
                print(f"Uso da partição {i[1]}: {porcentagemOcupados[0]}")

            print("\n\nAperte ctrl + c para retornar")


            time.sleep(1)
        except KeyboardInterrupt:
            return "0"


def info():
    os.system(codeCleaner)
    
    freqCpu = f'{cpu_freq().max / 100}Ghz'
    qtdCores = cpu_count()
    qtdThreads = cpu_count(logical=False)
    tempoGasto = f"{round(cpu_times().user / 60 / 60, 2)} Horas"
    processador = cpuinfo.get_cpu_info()['brand_raw']

    arquitetura = cpuinfo.get_cpu_info()['arch']
    if arquitetura == "X86_32":
        arquitetura = "32 bits"
    elif arquitetura == "X86_64":
        arquitetura = "64 bits"

        mac = get_mac()

    macString = ':'.join(("%012X" % mac) [i:i+2] for i in range(0,12,2))

    # if sistema == "Windows":
    #    serialNumber = subprocess.check_output('wmic bios get serialnumber').decode("utf-8")
    # elif sistema == "Linux":
    #    serialNumber = subprocess.check_output('').decode("utf-8")




    versaoSistemas = platform.version()
    memoriaTotal = f'{conversao_bytes(virtual_memory().total, 3)}GB'

    print("\033[1mInformações sobre o computador\033[0m\n\n")

    print("\033[1mSistema Operacional\033[0m", sistema)
    print("\033[1mVersão do sistema\033[0m", versaoSistemas)
    print("\033[1mMac Address\033[0m", macString)
    print("\033[1mArquitetura: \033[0m", arquitetura)
    print("\033[1mProcessador:\033[0m", processador)
    print("\033[1mQuantidade total de núcleos do processador:\033[0m", qtdCores)
    print("\033[1mQuantidade de Threads:\033[0m ", qtdThreads)
    print("\033[1mFrequência do processador:\033[0m ", freqCpu)
    print("\033[1mTotal de RAM :\033[0m", memoriaTotal)
    print("\033[1mTempo gasto pelo usuário no computador desde a última vez em que foi ligado:\033[0m", tempoGasto)

    input("\n\n\033[1mPressione Enter para prosseguir...\033[0m")
    return 0 


        
def insertPeriodico(serialNumber):
    while True:
            usoAtualMemoria = conversao_bytes(virtual_memory().used, 3)
            usoCpuPorc = cpu_percent()
            freqCpu = cpu_freq().current / 100
            disco = disk_partitions()[0][0]
            usoDisco = disk_usage(disco).percent
            dataHora = datetime.datetime.now()
            
            query = f"INSERT INTO dados VALUES(NULL, {serialNumber}, {usoAtualMemoria}, {usoCpuPorc}, NULL, {freqCpu}, {usoDisco}, '{dataHora}');"

            insert(query)

            time.sleep(10)
