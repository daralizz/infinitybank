from banco import obterConta, banco

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] = cliente['saldo'] - valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente!')

    else:
        print('Cliente não existe!')

if __name__ == "__main__":
    sacar(1, 100)
    print(banco)
