import random

class Baralho:
    def __init__(self):
        self.cartas = ['A_e', 'A_c', 'A_t', 'A_o', 'K_e', 'K_c', 'K_t', 'K_o',
                       'Q_e', 'Q_c', 'Q_t', 'Q_o', 'J_e', 'J_c', 'J_t', 'J_o',
                       '10_e', '10_c', '10_t', '10_o', '9_e', '9_c', '9_t', '9_o',
                       '8_e', '8_c', '8_t', '8_o', '7_e', '7_c', '7_t', '7_o',
                       '6_e', '6_c', '6_t', '6_o', '5_e', '5_c', '5_t', '5_o',
                       '4_e', '4_c', '4_t', '4_o', '3_e', '3_c', '3_t', '3_o',
                       '2_e', '2_c', '2_t', '2_o']
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self.cartas)


    def distribuir_cartas(self, num_jogadores, cartas_por_jogador):
        if num_jogadores * cartas_por_jogador > len(self.cartas):
            print("Não há cartas suficientes para distribuir.")
            return {}

        maos = {}
        for jogador in range(1, num_jogadores + 1):
            mao = []
            for _ in range(cartas_por_jogador):
                carta = self.cartas.pop(0)
                mao.append(carta)
            maos[f"Jogador {jogador}"] = mao
        return maos


    def distribuir_cartas_flop(self):
        enbaralhadas = list(self.cartas)
        flop = []
        turn = []
        river = []
        flop = enbaralhadas[1:4]
        turn = enbaralhadas[6]
        river = enbaralhadas[8]
        return flop, turn, river

    def quantificando_baralho(self):
        carta_split = []
        for carta in self.cartas:
            carta_split.append(carta.split('_'))
        #if carta_split[[0]] is  # stop here


# Exemplo de uso:

baralho = Baralho()
num_jogadores = 6
cartas_por_jogador = 2
baralho.quantificando_baralho()
maos = baralho.distribuir_cartas(num_jogadores, cartas_por_jogador)
print(maos)


flop, turn, river = baralho.distribuir_cartas_flop()
print(f'flop: {flop}')
print(f'turn: {turn}')
print(f'river: {river}')