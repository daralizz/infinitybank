banco = [
    {"conta": 1, "nome": "Mariana", "saldo": 159.99},
    {"conta": 2, "nome": "Jonas", "saldo": 205.50}
]

conta_atual = 2


def adicionarConta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    cliente = {
        "conta": conta_atual,
        "nome": nome,
        "saldo": saldo
    }
    banco.append(cliente)
    print('Cliente cadastrado com sucesso!')


def obterConta(conta: int) -> dict or None:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None


def deletarConta(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        banco.remove(cliente)
        print('Cliente deletado com sucesso!')
    else:
        print('Cliente não existe!')


def editarNome(novoNome: str, conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['nome'] = novoNome
        print('Dados alterados com sucesso!')
    else:
        print('Cliente não existe!')


def consultarCliente(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"N. Conta: {conta}")
        print(f"Cliente: {cliente['nome']}")
        print(f"Saldo: {cliente['saldo']}")
    else:
        print('Cliente não existe!')

def listarTodasContas() -> None:
    for cliente in banco:
        consultarCliente(cliente['conta'])
        print('---------------------------')

if __name__ == "__main__":
    listarTodasContas()

