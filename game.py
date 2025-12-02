from typing import List, Dict
from player import Player
from copy import deepcopy
from random import randint, choice
from data import EASY_QUESTIONS, MEDIUM_QUESTIONS, HARD_QUESTIONS



class Game:
    def __init__(self, names: List[str], limit: int):
        """
        -> Lista de jogadores
        -> Jogadores disponivesis
        -> quantidade de jogadores
        -> Perguntas faceis
        -> Perguntas medias
        -. Perguntas dificeis
        """
        self.players: List[Player] = self.initialize_players(names=names, limit=limit)
        self.players_alive: List[Player] = deepcopy(self.players)
        self.num_players: int = len(self.players)
        self.easy_questions: List[Dict[str, List[str], int]] = EASY_QUESTIONS
        self.medium_questions = MEDIUM_QUESTIONS
        self.hard_questions = HARD_QUESTIONS
    

    def initialize_players(self, names: List[str], limit: int) -> List[Player]:
        list_players  = list()
        for name in names:
            player = Player(name=name, limit=limit)
            list_players.append(player)

        for p in list_players:
            p.get_info()
        return list_players

    
    def show_question(self, cur_player: str, cur_question: str, alternatives: List[str]) -> None:
        print(f'Jogador Escolhido: {cur_player.name}\n')
        print(f'Pergunta: {cur_question}\n')
        print(f'Alternativas: \n')

        letters_alternatives = ['A', 'B', 'C', 'D']
        for i in range(len(alternatives)):
            print(f'{letters_alternatives[i]}) {alternatives[i]}')
        

        print("\nResposta: ")



    def run(self) -> None:
        # Choose a player
        cur_player = choice(self.players_alive)

        # Choose the question acording to its level
        hits = cur_player.get_hits()

        if hits < 3:
            cur_question = choice(self.easy_questions)
        elif hits < 8:
            cur_question = choice(self.medium_questions)
        else:
            cur_question = choice(self.hard_questions)
        print(cur_question)
        alternatives = cur_question['Alternativas']
        pergunta = cur_question['Pergunta']
        self.show_question(cur_player=cur_player, cur_question=pergunta, alternatives=alternatives)
                


if __name__ == '__main__':
    game = Game(names=['Vitor', 'Gabriel', 'Davi', 'Joao', 'Micael'], limit=10)

    j1 = Player(name='Vitor', limit=5)
    
    questao_atual = [
      {
        'Pergunta': 'anfjlsfjsnjkfasj',
        'Alternativas': ['Vasco', 'Flamengo', 'Ceara', 'Fortaleza'],
        'Resposta': 0
    }
     ]   
    cur_question = choice(questao_atual)
    q = questao_atual[0]['Pergunta']
    a = questao_atual[0]['Alternativas']
    game.show_question(cur_player=j1, cur_question=q, alternatives=a)