# Algoritmo Método de Newton-Rhapson,
# Aluno: Francisco Lucas Benvindo da Silva (BCC S4/ Cálculo Númerico)

import csv
import math
import os

# Dicionário (chave:valor) para funções matemáticas
funcoes_matematicas = {
    "sen": math.sin,
    "cos": math.cos,
    "tg": math.tan,
    "log": math.log,
    "exp": math.exp,
    "sqrt": math.sqrt,
    "e": math.e,
}


# Função para definir a função matemática
def func(x, funcao):
    for termo, funcao_matematica in funcoes_matematicas.items():
        if termo in funcao:
            if termo == "sen":
                funcao = funcao.replace(f"{termo}(", f"math.sin(")
            elif termo == "tg":
                funcao = funcao.replace(f"{termo}(", f"math.tan(")
            elif termo == "e":
                funcao = funcao.replace(f"{termo}", f"math.{termo}")
            else:
                funcao = funcao.replace(f"{termo}(", f"math.{termo}(")
    return eval(funcao)


def dfunc(x):
    h = 0.000001
    return (func(x + h, f) - func(x, f)) / h


def notacao(precisao):
    return eval(precisao)


def limparT():
    os.system("clear" if os.name == "posix" else "cls")  # Limpa o terminal


def menu():
    print("\033[1mAlgoritmo: Método de Newton-Rhapson\033[m")
    print("\033[1;36m->>> MENU <<<-\033[m")
    print("\033[1;32m1. Calcular\033[m")
    print("\033[1;33m2. Instruções\033[m")
    print("\033[1;31m3. Encerrar\033[m")


def instrucoes():
    i = (
        "\033[1mFuncionamento:\033[m\n"
        "Este programa permite calcular raízes de funções usando o método de Newton-Rhapson.\n"
        "Você pode escolher entre diferentes funções matemáticas, como seno, cosseno, tangente, logaritmo etc.\n"
        "Digite a função desejada, a aproximação inicial e a precisão desejada (em notação científica ou formato decimal).\n"
        "O programa então realizará as iterações até encontrar uma raiz aproximada\n"
        "Ao final, os resultados serão salvos em um arquivo CSV (arquivo de planilha)\n"
        "O arquivo pode ser aberto pelo usuário em um editor de planilhas desejado.\n\n"
        "\033[1mNeste algoritmo, as funções são organizadas seguindo os padrões abaixo:\033[m\n"
        "* representa uma multiplicação (Ex: 9*x)\n"
        "** representa uma potência (Ex: x**2)\n"
        "sen(x), cos(x) e tg(x) representam, respectivamente, seno, cosseno e tangente de x\n"
        "sqrt(x) é a raiz quadrada de x e log(x) é logaritmo natural de x\n"
        "exp(x) é o número 'e' elevado a uma potência de x\n"
        "'e' representa o número de Euler\n\n"
        "\033[1mExemplos de entradas seguindo o padrão apresentado acima:\033[m\n"
        "x**2 - x - 2\n"
        "tg(x) - 2\n"
        "log(x) - 2\n"
        "x**3 + sen(3)\n"
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
        case "1":
            limparT()
            f = input("Digite a função desejada: ")
            x0 = float(input("Digite a aproximação inicial (x0): "))
            p = notacao(input("Digite o valor de precisão desejado: "))

            i = 0  # número de iterações
            xi = x0  # valor inicial

            print("Iteração |      x       |      f(x)      |     ")
            print("-" * 65)
            cabecalho_info = [
                "Informações:",
                f"Função escolhida: {f}",
                f"Aproximação inicial (x0): {x0}",
                f"Precisão: {p}",
            ]
            cabecalho_resultados = ["Iteração", "Valor de x", "Valor de f(x)"]

            dados_resultados = []

            while True:
                dados_resultados.append([i, xi, func(xi, f)])
                print(f"   {i:2d}    | {xi:12.6f} | {func(xi,f):14.6f} |")

                x = xi - func(xi, f) / dfunc(xi)
                xi = x

                i += 1
                if math.fabs(func(xi, f)) < p:
                    dados_resultados.append([i, xi, func(xi, f)])
                    print(f"   {i:2d}    | {xi:12.6f} | {func(xi,f):14.6f} |")
                    break

            print("\033[1;32m\n->>> Informações <<<-\033[m")
            print(f"\033[1mO valor da raiz é aproximadamente: {xi:.6f}\033[m")
            print(f"\033[1mf({xi:.6f}) = {func(xi,f):.6f}\033[m")
            print(f"\033[1mNúmero de iterações: {i+1}\033[m")

            nome_arquivo = encontrar_nome_arquivo("resultados")
            with open(nome_arquivo, mode="w", newline="", encoding="utf-16") as arquivo:
                escrever_no_arquivo = csv.writer(arquivo)
                escrever_no_arquivo.writerows([cabecalho_info])
                escrever_no_arquivo.writerows([cabecalho_resultados])
                escrever_no_arquivo.writerows(dados_resultados)

            print(f"\033[1;32marquivo.csv: '{nome_arquivo}' gerado com sucesso.\033[m")
            print(
                "\033[1;32mOs resultados foram salvos no arquivo e podem ser visualizados posteriormente no editor de planilha desejado.\033[m"
            )
            input("\033[1;33mPressione ENTER para voltar ao menu.\033[m")
            limparT()

        case "2":
            limparT()  # Limpa o terminal
            instrucoes()
            limparT()  # Limpa o terminal

        case "3":
            print("\033[1;33m\nPrograma encerrado.\n\n\033[m")
            exit(0)
        case _:
            print(
                "\033[1;31m\nOpção inválida. Por favor selecione uma opção válida.\n\n\033[m"
            )
