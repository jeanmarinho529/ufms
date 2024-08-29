def consumo_combustivel(tempo, velocidade, consumo):
    return tempo * velocidade / consumo

tempo = float(input("Tempo gasto: "))
velocidade = float(input("Velocidade media: "))
consumo = float(input("Consumero de combustivel: "))

print(consumo_combustivel(tempo, velocidade, consumo))