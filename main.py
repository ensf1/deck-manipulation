from Deque import Deque


def main():
    D = Deque(int(input('Informe o tamanho do deque: ')))
    empty_message = 'Deque está vazio'
    D.add_first((E:=input('Informe um valor para adicionar ao início do deque: ')))
    D.add_last((E:=input('Informe um valor para adicionar ao fim do deque: ')))
    delete = D.delete_first()
    print(f'{delete} foi removido do inicio do deque' if delete else empty_message)
    delete = D.delete_last()
    print(f'{delete} foi removido do fim do deque' if delete else empty_message)
    first = D.first()
    print(f'O primeiro elemento do deque é {first}' if first else empty_message)
    last = D.last()
    print(f'O último elemento do deque é {last}' if last else empty_message)
    print(f'O deque não está vazio' if not D.is_empty() else empty_message)
    print(f'O número de elementos do deque é {len(D)}')
    D.add_first(E)
    D.add_last((E := input('Informe um valor para adicionar ao fim do deque: ')))
    first = D.first()
    print(f'O primeiro elemento do deque é {first}' if first else empty_message)
    last = D.last()
    print(f'O último elemento do deque é {last}' if last else empty_message)
    print(f'O número de elementos do deque agora é {len(D)}')
    print('Depois de rotacionar 1 vez:')
    D.rotate(1)
    first = D.first()
    print(f'O primeiro elemento do deque é {first}' if first else empty_message)
    last = D.last()
    print(f'O último elemento do deque é {last}' if last else empty_message)



if __name__ == '__main__':
    main()
