import random

class Baralho:
    def __init__(self): # baralho com cartas do poker
        self.cartas = {'o':{14:'A_o',13:'K_o',12:'Q_o',11:'J_o',10:'10_o',9:'9_o',8:'8_o',
                            7:'7_o',6:'6_o',5:'5_o',4:'4_o',3:'3_o',2:'2_o'},
                       't':{14:'A_t',13:'K_t',12:'Q_t',11:'J_t',10:'10_t',9:'9_t',8:'8_t',
                            7:'7_t',6:'6_t',5:'5_t',4:'4_t',3:'3_t',2:'2_t'},
                       'e':{14:'A_e',13:'K_e',12:'Q_e',11:'J_e',10:'10_e',9:'9_e',8:'8_e',
                            7:'7_e',6:'6_e',5:'5_e',4:'4_e',3:'3_e',2:'2_e'},
                       'c':{14:'A_c',13:'K_c',12:'Q_c',11:'J_c',10:'10_c',9:'9_c',8:'8_c',
                            7:'7_c',6:'6_c',5:'5_c',4:'4_c',3:'3_c',2:'2_c'}}
        self.baralho_dealer = []
        self.fichas = {}


    def embaralhar(self) -> dict: # embaralhando
        for naipe, cards in self.cartas.items():
            for carta in cards.values():
                self.baralho_dealer.append(carta)
        random.shuffle(self.baralho_dealer)
        return self.baralho_dealer
                
    def distribuir_cartas(self, num_jogadores:int, cartas_por_jogador:int) -> dict: # distribuindo cartas para os jogadores
        if num_jogadores * cartas_por_jogador > len(self.baralho_dealer): # teste para ver se tem mais jogadores que cartas
            print("Não há cartas suficientes para distribuir.")
            return {}

        maos = {}
        for jogador in range(1, num_jogadores + 1):
            mao = []
            for _ in range(cartas_por_jogador):
                carta = self.baralho_dealer.pop(0)
                mao.append(carta)
            maos[f"Jogador {jogador}"] = mao
        return maos

    def contandoFichas(self, maos_distribuidas, valor_incial, valor_apostado) -> dict: 
        for jogador in maos_distribuidas: # distribuindo fichas para cada jogador
            self.fichas[jogador] = valor_incial
        return self.fichas  

    # distribuindo cartas da mesa (flop)
    def distribuindo_cartas_flop(self) -> list:
        embaralhadas = self.baralho_dealer
        flop = []
        turn = []
        river = []
        flop = embaralhadas[1:4]
        turn = embaralhadas[6]
        river = embaralhadas[8]
        return flop, turn, river


class Jogadores(Baralho):
    def __init__(self):
        self.jogadores = []
        super().__init__()
        

    def jogando_cada_turno(self):
        pass





    # def quantificando_baralho(self, maos):
    #     carta_split = []
    #     num_card = []
    #     naipe_card = []
    #     for jogador, cartas in maos.items():
    #         for carta in cartas:
    #             carta_split = carta.split('_')
               
               
                

    #     print(num_card)
        #if carta_split[[0]] is  # stop here





#class poker_texas_holdem:

#    def __init__(self) -> None:
#        pass

# Exemplo de uso:
def main():
    baralho = Baralho()
    # configuração de players e modalidade do jogo
    num_jogadores = int(input('numero de jogadores? '))
    cartas_por_jogador = int(input('numero de cartas por jogador? '))
    valor_inicial = int(input('qual o valor inicial de fichas? '))
    aposta = int(input('qual o valor da aposta '))
    # embraralhar e distribuir cartas dos jogadores e flop
    baralho.embaralhar()

    maos = baralho.distribuir_cartas(num_jogadores, cartas_por_jogador)
    baralho.contandoFichas(maos, valor_inicial , aposta)
    flop, turn, river = baralho.distribuindo_cartas_flop()
    print(f'maos: {maos}')
    print(f'flop: {flop}')
    print(f'turn: {turn}')
    print(f'river: {river}')
   
if __name__ == '__main__':
    main()