from __future__ import print_function
from ast import AsyncFunctionDef
import enum
from re import I
import time
from dashing import *
from psutil import *
from functions import conversao_bytes
import os
from functions import codeCleaner, sistema


def dashboard():

    ui = HSplit(
        VSplit(
            HSplit(
                VGauge(title='RAM'),
                title='Memória',
                border_color=3
            ),
            HSplit(
                Text(
                    '',
                    title='Disco',
                    border_color=6
                ),
                Text(
                    'Teste',
                    title='Processos',
                    border_color=1,
                ),
            )

        ),
        VSplit(
            HGauge(title='CPU %'),
            HGauge(title='cpu_1 %'),
            HGauge(title='cpu_2 %'),
            HGauge(title='cpu_3 %'),
            HGauge(title='cpu_4 %'),
            HGauge(title='cpu_5 %'),
            HGauge(title='cpu_6 %'),
            HGauge(title='cpu_7 %'),
            HGauge(title='cpu_8 %'),
            title="CPU",
            border_color=5,
        )
    )

    while True:

        # Memoria
        usoMemoria = memoriaDisponivel = ui.items[0]
        ram = ui.items[0].items[0].items[0]

        memoriaDisponivel.value = virtual_memory().total
        ram.value = virtual_memory().percent
        usoMemoria.value = virtual_memory().percent

        ram.title = f"RAM: {usoMemoria.value}% "

        # CPU
        cpu = ui.items[1]
        cpuPercentGraph = cpu.items[0]
        cpuPercent = cpu_percent()
        cpuPercentGraph.value = cpuPercent
        cpuPercentGraph.title = f"CPU {cpuPercent}%"

        usoPorCore = cpu_percent(percpu=True)

        cpuPercentCoreGraph = cpu.items[1:9]

        for i, (core, value) in enumerate(zip(cpuPercentCoreGraph, usoPorCore)):
            core.value = value
            core.title = f"cpu_{i} {value}%"

        # DISCO
        disco = ui.items[0].items[1].items[0]

        disco.text = f"{'Partição':<15}{'Uso':<10}"

        particoes = []
        if sistema == "Windows":
            for part in disk_partitions(all=False): # identificando partições
                if part[0] == "F:\\":
                    break
                elif part[0] == "E:\\":
                    break
                else:
                    particoes.append(part[0])
        elif sistema == "Linux":
            particoes.append("/")


        porcentagemOcupados = []
        for j in enumerate(particoes[0:8]):
            porcentagemOcupados.append(disk_usage(j[1]).percent)

            disco.text += '\n{:<15}{:<10}'.format(
                particoes[j[0]],
                porcentagemOcupados[j[0]]
            )

        # Processos
        processos = ui.items[0].items[1].items[1]
        listaProcessos = []

        for proc in process_iter():
            infoProc = proc.as_dict(['name','cpu_percent'])
            if infoProc['cpu_percent'] > 0:
                listaProcessos.append(infoProc)

        def func(e):
            return e['cpu_percent']

        listaProcessos.sort(key=func, reverse=True)

        processos.text = f"{'Nome':<25}CPU"

        for proc in listaProcessos[:10]:
            processos.text += f"\n{proc['name']:<25} {proc['cpu_percent']}"

        os.system(codeCleaner)

        try:
            ui.display()
            time.sleep(1)
        except KeyboardInterrupt:
            return "0"