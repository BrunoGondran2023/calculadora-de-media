# Função para obter a nota do usuário.


def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


# Função para calcular a média das notas.


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


# Função para verificar o status do aluno com base na média.


def verificar_status(media, media_necessaria, minimo):
    if media >= media_necessaria:
        return "aprovado(a)"
    elif media < media_necessaria > minimo:
        return "recuperação"
    else:
        return "reprovado(a)"


# Função principal do programa.


def main():
    nota1 = obter_nota("Digite o valor da primeira nota: ")
    nota2 = obter_nota("Digite o valor da segunda nota: ")
    minimo = obter_nota("Digite o valor mínimo necessário: ")
    media_necessaria = obter_nota("Digite o valor da média necessária: ")

    media = calcular_media(nota1, nota2)

    status = verificar_status(media, media_necessaria, minimo)

    print("A média é: {}, {}!".format(media, status))


if __name__ == "__main__":
    main()
