import time

# Iniciando o estado das lampadas 
# 0 = apagada e fria 
# 1 = ligada
# 2 = apagada e quente

lampadas = [0, 0, 0]  # Todas começam apagadas e frias

# Ligando o primeiro interruptor (lampada 1)
lampadas[0] = 2  # Lampada 1 esquenta
time.sleep(5) # simulando tempo ligado

# Desligando o primeiro interruptor e ligando o segundo (lampada 2)
lampadas[0] = 1  # Lampada 1 apagada mas quente
lampadas[1] = 2  # Lampada 2 ligada

print(f'Lampadas{lampadas}')

# Verificando o estado das lâmpadas
def verificar_lampadas(lampadas):
    for i, lamp in enumerate(lampadas):
        if lamp == 0:
            status = "apagada e fria"
        elif lamp == 1:
            status = "Ligada"
        else:
            status = "apagada e quente"
        print(f"Lampada {i + 1}: {status}")

verificar_lampadas(lampadas)
