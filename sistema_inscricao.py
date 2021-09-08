def main():
    dados = pedir_dados()  # dados = (nome, idade, altura, peso)
    imc = calcular_imc(dados[2], dados[3])
    verificar_imc(imc, dados[0])


def pedir_dados():
    nome = input("Por favor, insira seu nome: ")
    idade = input("Por favor, insira sua idade: ")
    altura = float(input("Por favor, insira sua altura (em m): "))
    peso = float(input("Por favor, insira seu peso (em kg): "))

    return nome, idade, altura, peso


def calcular_imc(altura, peso):
    imc = peso / (altura * altura)
    return imc


def verificar_imc(imc, nome):
    if (imc > 24.9):
        mensagem_imc_alto(nome, imc)
    elif (imc <= 24.9):
        tempo_total = pedir_treino()
        verificar_treino(tempo_total, nome)


def mensagem_imc_alto(nome, imc):
    print("Olá {}, informamos que seu IMC é de {:.2f}. Sendo assim, você esta sendo considerado como Acima do Peso.\n"
          "Logo recomendamos que normalize sua forma física, para que depois volte a se inscrever.".format(nome, imc))


def pedir_treino():
    vezes_treino = int(input("Quantas vezes você treina por semana? "))
    minutos_treino = int(input("Aproximadamente quantos minutos por sessão de treino? "))
    tempo_total = vezes_treino * minutos_treino

    return tempo_total


def verificar_treino(tempo_total, nome):
    if (tempo_total >= 300):
        exibir_mensagem_aprovado(nome)
    else:  # treina menos que 300 minutos por dia
        print("Muito obrigado, agradecemos a sua participação!")


def exibir_mensagem_aprovado(nome):
    print("Parabéns {}, você passou em todos os nossos testes, agora você fará um teste pessoal em nossa sede,\n"
          "favor comparecer ao endereço: Rua dos Atletas, 43, Bairro do Futebol. Nos vemos lá!".format(nome))


if (__name__ == '__main__'):
    main()
