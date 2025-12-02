from typing import List, Dict
from player import Player
import time
from copy import copy
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
        self.players_alive: List[Player] = copy(self.players)
        self.num_players: int = len(self.players)
        self.easy_questions: List[Dict[str, List[str], int]] = EASY_QUESTIONS
        self.medium_questions: List[Dict[str, List[str], int]] = MEDIUM_QUESTIONS
        self.hard_questions: List[Dict[str, List[str], int]] = HARD_QUESTIONS
    

    def initialize_players(self, names: List[str], limit: int) -> List[Player]:
        list_players  = list()
        for name in names:
            player = Player(name=name, limit=limit)
            list_players.append(player)

        return list_players

    
    def show_question(self, cur_player: str, cur_question: str, alternatives: List[str], cur_level: str) -> None:
        print('-='*20)
        print(f'Jogador Escolhido: {cur_player.name}')
        print(f"Nível da questão: {cur_level}\n")
        print(f'Pergunta: {cur_question}\n')
        print(f'Alternativas: \n')

        alternatives_letters = ['A', 'B', 'C', 'D']
        for i in range(len(alternatives)):
            print(f'{alternatives_letters[i]}) {alternatives[i]}')
        
        
    
    def get_users_answer(self) -> str:
        alternatives_letters = ['A', 'B', 'C', 'D']
        ans = input("\nResposta: ").upper()
        while ans not in alternatives_letters:
            print("Resposta inválida, digite uma letra de A até D")
            ans = input("\nResposta: ").upper()

        return ans

    def sort_players(self) -> None:
        self.players.sort(key= lambda x: (x.hits, -x.time_played), reverse=True)
    

    def show_players(self) -> None:
        for i in range(self.num_players):
            print(f'{i+1}) Nome: {self.players[i].name} , Questões acertadas: {self.players[i].hits}, Tempo para responder: {round(self.players[i].time_played, 2)}\n')

    def run(self) -> None:
        
        while self.players_alive:
            cur_player = choice(self.players_alive)

            hits = cur_player.get_hits()

            if hits < 3:
                cur_question_set = choice(self.easy_questions) 
                cur_level = 'Fácil'
            elif hits < 8:
                cur_question_set = choice(self.medium_questions)
                cur_level = 'Médio'
            else:
                cur_question_set = choice(self.hard_questions)
                cur_level = 'Difícil'
            
            alternatives = cur_question_set['Alternativas']
            question = cur_question_set['Pergunta']
            self.show_question(cur_player=cur_player, cur_question=question, alternatives=alternatives, cur_level=cur_level)
            
            start_time = time.perf_counter()

            ans = self.get_users_answer()
            alternatives_letters = ['A', 'B', 'C', 'D']
            player_index = self.players_alive.index(cur_player)
 
            end_time = time.perf_counter()

            time_to_answer = end_time - start_time
            
            cur_player.add_time_played(time_to_answer=time_to_answer)
            # Remover a questão que foi feita
            if hits < 3:
                self.easy_questions.remove(cur_question_set)
            elif hits < 8:
                self.medium_questions.remove(cur_question_set)
            else:
                self.hard_questions.remove(cur_question_set)
            
            if cur_question_set['Resposta'] == alternatives_letters.index(ans):
                cur_player.increment_hits()
                print("CERTA RESPOSTA")
            
            else:
                print("ERROU")
                self.players_alive.pop(player_index)
                continue            
            
            if self.players_alive[player_index].get_hits() == 10:
                print(f"Jogador já acertou todas as perguntas, removendo {self.players_alive[player_index].name}")
                self.players_alive.pop(player_index)

        self.sort_players()
        self.show_players()
            

if __name__ == '__main__':
    game = Game(names=['Vitor', 'Gabriel', 'Davi', 'Joao', 'Micael'], limit=10)

    game.run()