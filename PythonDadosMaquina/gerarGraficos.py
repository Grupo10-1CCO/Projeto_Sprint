import time
import matplotlib.pyplot as plt
import psutil
import os
import datetime
from database import select
from functions import conversao_bytes
from functions import codeCleaner

if os.name == 'nt':
    sistem="C:\\"
    nome='Windows'
else:
    sistem="/"
    nome='Linux'


def gerarGraficoDisco():
    uso_disco = psutil.disk_usage(sistem).used
    free_disco = psutil.disk_usage(sistem).free

    vt_dados_disco = []

    vt_dados_disco.append(uso_disco)
    vt_dados_disco.append(free_disco)

    label = []
    label.append('Espaço utilizado no disco: {}GB'.format(conversao_bytes(uso_disco, 3)))
    label.append('Espaço disponível no disco: {}GB'.format(conversao_bytes(free_disco, 3)))

    color = ['firebrick', 'limegreen']
    myexplode = [0.1, 0]

    os.system(codeCleaner)
    figura = plt.figure(figsize=(15,7))
    plt.pie(vt_dados_disco, autopct='%.1f%%', colors=color, explode=myexplode, textprops={'fontsize': 14})
    plt.legend(title='Dados', labels=label, loc='center right', bbox_to_anchor=(1.5, 0.6))
    plt.title ('Diagnostico do disco')
    plt.show()

def gerarGraficoCpu(userId):
    query = f'select usoCpu, frequenciaCpu, dataHoraRegistro from dados, Usuario where idUsuario = {userId} order by idDados desc limit 8;'
    dados = []
    dados.append(select(query, True))

    usoCpuPorc = []
    freqCpu = []
    dataHoraRegis = []

    for linha in select(query,True):
        usoCpuPorc.append(linha[0])
        freqCpu.append(linha[1])
        data_format = linha[2].strftime('%d/%m \n %H:%M:%S')
        dataHoraRegis.append(data_format)
    
    dataHoraFormatado = dataHoraRegis[::-1]

    figura = plt.figure(figsize=(15,7))
    facecolor='blue'
    plt.plot(dataHoraFormatado, usoCpuPorc)
    plt.title ('Uso da CPU (%)')
    plt.show()

def gerarGraficoCpu2(userId):
    query = f'select usoCpu, frequenciaCpu, dataHoraRegistro from dados, Usuario where idUsuario = {userId} order by idDados desc limit 8;'
    dados = []
    dados.append(select(query, True))

    usoCpuPorc = []
    freqCpu = []
    dataHoraRegis = []

    for linha in select(query,True):
        usoCpuPorc.append(linha[0])
        freqCpu.append(linha[1])
        data_format = linha[2].strftime('%d/%m \n %H:%M:%S')
        dataHoraRegis.append(data_format)

    dataHoraFormatado = dataHoraRegis[::-1]

    figura = plt.figure(figsize=(15,7))
    facecolor='blue'
    plt.plot(dataHoraFormatado, freqCpu)
    plt.title ('Frequência da CPU (Mhz)')
    plt.show()
    time.sleep(3)

def gerarGraficoMemoria(userId):
    query = f'select usoMemoria, dataHoraRegistro from dados, Usuario where idUsuario = {userId} order by idDados desc limit 8;'
    dados = []
    dados.append(select(query, True))

    usoMemoria = []
    dataHoraRegis = []

    for linha in select(query,True):
        usoMemoria.append(linha[0])
        data_format = linha[1].strftime('%d/%m \n %H:%M:%S')
        dataHoraRegis.append(data_format)

    dataHoraFormatado = dataHoraRegis[::-1]

    figura = plt.figure(figsize=(15,7))
    facecolor='blue'
    plt.plot(dataHoraFormatado, usoMemoria)
    plt.title ('Uso da Memória RAM (%)')
    plt.show()
