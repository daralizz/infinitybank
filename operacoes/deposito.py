from banco import obterConta, banco

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] = cliente['saldo'] + valor
        print('Deposito realizado com sucesso!')
    else:
        print('Cliente não existe!')

if __name__ == "__main__":
    depositar(1, 300)
    print(banco)
