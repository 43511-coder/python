import random

#lista de times
times=["Palmeiras","Flamengo","Cruzeiro","Ibis","RDS Futsal","Time de Esquina","Corinthias" ]

#pontuação inicial
pontuacao={}

for time in times:
    pontuacao[time]=0

#Frase inicial
print("=== FACE MASH DE TIMES ===")
print("Escolha o melhor time!\n")

#Quantidade de rodas
for rodada in range(5):
    #escolha dois times
    time1, time2= random.sample(times, 2)

    print(f"Rodada {rodada + 1}")
    print("1 - ", time1)
    print("2 - ", time2)

    escolha= input("escolha (1 ou 2): ")

    if escolha == "1":
        pontuacao[time1] += 1
        print("voce escolheu {time1}\n")
    elif escolha == "2":
        pontuacao[time2] += 1
        print("voce escolheu {time2}\n")
    else:
        print("opcao invalida!\n")
    
# mostra o rank final
print("=== RANKING FINAL ===")

ranking= sorted(
    pontuacao.times(),
    key=lambda item:[1],
    reverse=True
)
for time, pontos in ranking:
    print(f"{time}: {pontos} votos")