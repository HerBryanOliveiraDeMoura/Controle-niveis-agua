from colorama import Fore, Style

#Processamento
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
    "Nível não encontrado"
]
def nivel_repositorio(nivel):
    if nivel == 1:
        return Fore.RED + situacoes[0] + Style.RESET_ALL
    
    elif nivel == 2:
        return Fore.YELLOW + situacoes[1] + Style.RESET_ALL
    elif nivel == 3:
        return Fore.GREEN + situacoes[2] + Style.RESET_ALL
    elif nivel == 4:
        return Fore.CYAN + situacoes[3] + Style.RESET_ALL
    elif nivel == 5:
        return Fore.BLUE + situacoes[4] + Style.RESET_ALL
    else:
        return situacoes[5] + Style.RESET_ALL
#Entrada
for nivel in range(1, 6):
    #Saída
    print(nivel_repositorio(nivel))
