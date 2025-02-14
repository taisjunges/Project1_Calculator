# Atividade - Exercício módulo 1

print('Bem-vindo à calculadora!')
escolha = input('Você deseja fazer uma operação? (s/n): ').strip().lower()

while escolha == 's':

    try:
        val_1 = float(input('Adicione um valor: '))
        val_2 = float(input('Adicione outro valor: '))
        op = input('Escolha uma operação (+, -, *, /): ').strip()

        if op == '+':
            resultado = val_1 + val_2
        elif op == '-':
            resultado = val_1 - val_2
        elif op == '*':
            resultado = val_1 * val_2
        elif op == '/':
            if val_2 == 0:
                print('Erro: divisão por zero não é permitida')
                escolha = input('Você deseja fazer outra operação? (s/n): ').strip().lower()
                continue
            resultado = val_1 / val_2
        else:
            print('Operação inválida. Tente novamente.')
            continue

        print('Resultado:', resultado)

    except:
        print('Erro: digite apenas números válidos.')
        continue

    escolha = input('Você deseja fazer outra operação? (s/n):').strip().lower()

print('Até a próxima!')
