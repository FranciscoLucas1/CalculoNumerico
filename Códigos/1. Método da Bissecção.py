import math
import os

# Mapeamento de termos para funções
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
    print("\033[1mAlgoritmo: Método da Bissecção:\033[m")
    print("Menu:")
    print("1. Calcular")
    print("2. Instruções")
    print("3. Encerrar")

def instrucoes():
    i = (
        "\033[1mFuncionamento:\033[m\n"
        "Este programa permite calcular raízes de funções usando o método da bisseção.\n"
        "Você pode escolher entre diferentes funções matemáticas, como seno, cosseno, tangente, logaritmo etc.\n"
        "Digite a função desejada, os valores de 'a' e 'b' do intervalo, e a precisão desejada.\n"
        "O programa então realizará as iterações até encontrar uma raiz aproximada.\n\n"
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
    input("Pressione ENTER para voltar ao menu.")


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
                print("Não há como afirmar se há raiz neste intervalo.")
            else:
                print("Iteração |      x      |      f(x)      |      b - a")
                print("-" * 58)

                while math.fabs(b - a) > p:
                    xi = (a + b) / 2.0
                    f_xi = func(xi, f)

                    print(f"   {i:2d}    | {xi:12.6f} | {f_xi:14.6f} | {b - a:14.6f}")
                    if func(a, f) * f_xi < 0.0:
                        b = xi
                    else:
                        a = xi
                    i += 1

                print(f"O valor da raiz é aproximadamente: {xi:.6f}")
                print(f"f({xi:.6f}) = {f_xi:.6f}")
                print(f"Número de iterações: {i-1}")
                
                input("\n\nPressione enter para retornar para o menu.")
               
        case '2':
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal
            instrucoes()
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpa o terminal
        
        case '3':
            print("Programa encerrado.")
            exit(0)
        case _:
            print("\033[1m\nOpção inválida. Por favor selecione uma opção válida.\n\n\033[m")
         
