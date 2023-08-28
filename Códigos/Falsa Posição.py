# Algoritmo Método Falsa Posição, 
# Aluno: Francisco Lucas Benvindo da Silva (BCC S4/ Cálculo Númerico)

import csv
import math
import os

# Dicionário (chave:valor) para funções matemáticas
funcoes_matematicas = {
    'sen': math.sin,
    'cos': math.cos,
    'tg': math.tan,
    'log': math.log,
    'exp': math.exp,
    'sqrt': math.sqrt,
    'e': math.e
}

# Função para definir a função matemática
def func(x, funcao):
    for termo, funcao_matematica in funcoes_matematicas.items():
        if termo in funcao:
            if termo == 'sen':
                funcao = funcao.replace(f'{termo}(', f'math.sin(')
            elif termo == 'tg':
                funcao = funcao.replace(f'{termo}(', f'math.tan(')
            elif termo == 'e':
                funcao = funcao.replace(f'{termo}', f'math.{termo}')
            else:
                funcao = funcao.replace(f'{termo}(', f'math.{termo}(')
    return eval(funcao)

def menu():
    print("\033[1mAlgoritmo: Método da Falsa Posição\033[m")
    print("\033[1;36m->>> MENU <<<-\033[m")
    print("\033[1;32m1. Calcular\033[m")
    print("\033[1;33m2. Instruções\033[m")
    print("\033[1;31m3. Encerrar\033[m")

def instrucoes():
    i = (
        "\033[1mFuncionamento:\033[m\n"
        "Este programa permite calcular raízes de funções usando o método da bisseção.\n"
        "Você pode escolher entre diferentes funções matemáticas, como seno, cosseno, tangente, logaritmo etc.\n"
        "Digite a função desejada, os valores de 'a' e 'b' do intervalo, e a precisão desejada.\n"
        "O programa então realizará as iterações até encontrar uma raiz aproximada\n"
        "Ao final os resultados seram salvos em arquivo csv (arquivo de planilha)\n" 
        "O arquivo poderá ser aberto pelo ususário em um editor de planilha desejado.\n\n"

        "\033[1mNeste algoritmo, as funções são organizadas seguindo os padrões abaixo:\033[m\n"
        "* represente uma multiplicação (Ex: 9*x)\n"
        "sen(x), cos(x) e tg(x) representam respectivamente seno, cosseno e tangente de x\n"
        "sqrt(x) é a raiz quadrada de x e log(x) é logaritmo natural de x\n"
        "exp(x) é o número 'e' elevado a uma potência de x\n"
        "'e' representa o número de Euler\n\n"
        "\033[1mExemplos de entradas seguindo o padrão apresentado acima:\033[m\n"
        "x**2 - x - 2\n"
        "tg(x) - 2\n"
        "log(x) - 2\n"
        "x**3 + sen(3)"
    )
    print(i)
    input("\033[1;32mPressione ENTER para voltar ao menu.\033[m")

def encontrar_nome_arquivo(nome_base):
    contador = 1
    nome_arquivo = f"{nome_base}_{contador}.csv"
    while os.path.exists(nome_arquivo):
        contador += 1
        nome_arquivo = f"{nome_base}_{contador}.csv"
    return nome_arquivo

while True:
    menu()
    opcao = input("Escolha uma opção (1/2/3): ")

    match opcao:
        case '1':
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal
            f = input("Digite a função desejada: ")
            a = float(input("Digite o valor de 'a' do intervalo [a,b]: "))
            b = float(input("Digite o valor de 'b' do intervalo [a,b]: "))
            p = float(input("Digite o valor de precisão desejado: "))
    
            i = 1  # número de iterações
            Fa = func(a, f)  # valor de a aplicado na função
            Fb = func(b, f)  # valor de b aplicado na função

            if Fa * Fb > 0.0:
                os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal
                print("\033[1mNão há como afirmar se há raiz neste intervalo. Retornando ao menu\033[m")
            else:
                print("Iteração |      x       |      f(x)      |      b - a")
                print("-" * 65)
                cabecalho_info = ["Informações:", f"Função escolhida: {f}", f"Intervalo: [{a}, {b}]", f"Precisão: {p}"]
                cabecalho_resultados = ["Iteração", "Valor de x", "Valor de f(x)", "Intervalo (b - a)"]
        
                dados_resultados = []

                while math.fabs(b - a) > p:
                    xi = (a*Fb - b*Fa)/(Fb - Fa)
                    f_xi = func(xi, f)

                    dados_resultados.append([i, xi, f_xi, b - a])
                    print(f"   {i:2d}    | {xi:12.6f} | {f_xi:14.6f} | {b - a:14.6f}")
                    if func(a, f) * f_xi < 0.0:
                        b = xi
                    else:
                        a = xi
                    i += 1

                print("\033[1;32m\n->>> Informações <<<-\033[m")
                print(f"\033[1mO valor da raiz é aproximadamente: {xi:.6f}\033[m")
                print(f"\033[1mf({xi:.6f}) = {f_xi:.6f}\033[m")
                print(f"\033[1mNúmero de iterações: {i-1}\033[m")

                nome_arquivo = encontrar_nome_arquivo("resultados")
                with open(nome_arquivo, mode='w', newline='', encoding='utf-16') as arquivo:
                    escrever_no_arquivo = csv.writer(arquivo)
                    escrever_no_arquivo.writerows([cabecalho_info])
                    escrever_no_arquivo.writerows([cabecalho_resultados])
                    escrever_no_arquivo.writerows(dados_resultados)
                
                print(f"\033[1;32marquivo.csv: '{nome_arquivo}' gerado com sucesso.\033[m")
                print("\033[1;32mOs resultados foram salvos no arquivo e podem ser visualizados posteriormente no editor de planilha desejado.\033[m")
                input("\033[1;33mPressione ENTER para voltar ao menu.\033[m")
                os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal

        case '2':
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal
            instrucoes()
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal
        
        case '3':
            print("\033[1;33m\nPrograma encerrado.\n\n\033[m")
            exit(0)
        case _:
            print("\033[1;31m\nOpção inválida. Por favor selecione uma opção válida.\n\n\033[m")