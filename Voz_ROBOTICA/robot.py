from colorama import init, Fore
from gtts import gTTS
import os
import time

# Inicializa o colorama para colorir o terminal
init(autoreset=True)


def loading():
    # Exibir a mensagem inicial
    print(Fore.GREEN + 'Robot Google', end='')

    # Loop para simular o carregamento com pontos
    for _ in range(10):
        print('.', end='', flush=True)  # Exibir os pontos de forma contínua
        time.sleep(0.5)  # Aguardar 0.5 segundos entre cada ponto

    # Exibir a mensagem de carregamento completo
    print(Fore.GREEN + '\nRobot Google Completed')


# Função para gerar áudio a partir de texto usando gTTS
def texto_para_audio(texto, nome_arquivo):
    tts = gTTS(text=texto, lang='pt')
    tts.save(nome_arquivo)

    # Reproduzir o arquivo gerado
    if os.name == 'posix':  # Para sistemas Linux/macOS
        os.system(f'open {nome_arquivo}')
    elif os.name == 'nt':  # Para sistemas Windows
        os.system(f'start {nome_arquivo}')


# Exibir a arte ASCII colorida
def mostrar_ascii():
    print(Fore.RED + '_________')
    print(Fore.GREEN + '|         |')
    print(Fore.CYAN + '| Voice   |')
    print(Fore.YELLOW + '| Mod     |')
    print(Fore.RED + ' |_________|')
    print(Fore.GREEN + '  |   | ')
    print(Fore.BLUE + '  |   |')
    print(Fore.RED + ' --|---|--')
    print(Fore.CYAN + ' /     \\    ')
    print(Fore.GREEN + '|  MIC IN   |')
    print(Fore.YELLOW + ' \\_________/')
    print(Fore.RED + '      ||')
    print(Fore.RED + '  [ ]   [ ]  Slider')
    print(Fore.GREEN + '  [ ]    [ ]  Controls')
    print(Fore.YELLOW + '[MODIFYING VOICE...]')


# Executar a função de loading
loading()

# Mostrar a arte ASCII
mostrar_ascii()

# Perguntar ao usuário por texto e gerar o áudio
texto = input(Fore.RED + 'Digite algo para o Robot falar: ')
saida_arquivo = 'Robot.mp3'

# Gerar o áudio
texto_para_audio(texto, saida_arquivo)

# Exibir a mensagem de sucesso
print(Fore.GREEN + f'[+] Gerador de áudio criado: {saida_arquivo}')
