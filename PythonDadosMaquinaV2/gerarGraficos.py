import matplotlib.pyplot as plt
import psutil
import os
from functions import conversao_bytes
from tkinter.font import BOLD

if os.name == 'nt':
    sistem="C:\\"
    nome='Windows'
else:
    sistem="/"
    nome='Linux'

if os.name == 'nt':
    clear_console = 'cls'
else:
    clear_console = 'clear'

def gerarGraficoDisco():
    uso_disco = psutil.disk_usage(sistem).used
    free_disco = psutil.disk_usage(sistem).free

    vt_dados_disco = []

    vt_dados_disco.append(uso_disco)
    vt_dados_disco.append(free_disco)

    label = []
    label.append('Espaço utilizado no disco: {}'.format(conversao_bytes(uso_disco, 3)))
    label.append('Espaço disponível no disco: {}'.format(conversao_bytes(free_disco, 3)))

    color = ['firebrick', 'limegreen']
    myexplode = [0.1, 0]

    os.system(clear_console)
    figura = plt.figure(figsize=(10,3))
    plt.pie(vt_dados_disco, autopct='%.1f%%', colors=color, explode=myexplode, textprops={'fontsize': 14, 'weight':BOLD })
    plt.legend(title='Dados', labels=label, loc='center right', bbox_to_anchor=(1.5, 0.6))
    plt.title ('Diagnostico do disco')
    plt.show()
