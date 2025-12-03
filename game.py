from typing import List, Dict, Any, Tuple
from copy import copy
from random import choice
import time

import streamlit as st

from player import Player
from data import EASY_QUESTIONS, MEDIUM_QUESTIONS, HARD_QUESTIONS


class Game:
    def __init__(self, names: List[str], limit: int):
        """
        -> Lista de jogadores
        -> Jogadores disponíveis
        -> Quantidade de jogadores
        -> Perguntas fáceis, médias e difíceis
        """
        self.players: List[Player] = self.initialize_players(names=names, limit=limit)
        self.players_alive: List[Player] = copy(self.players)
        self.num_players: int = len(self.players)
        # cada pergunta deve ser algo como:
        # {"Pergunta": str, "Alternativas": [str, str, str, str], "Resposta": int}
        self.easy_questions: List[Dict[str, Any]] = EASY_QUESTIONS.copy()
        self.medium_questions: List[Dict[str, Any]] = MEDIUM_QUESTIONS.copy()
        self.hard_questions: List[Dict[str, Any]] = HARD_QUESTIONS.copy()

    def initialize_players(self, names: List[str], limit: int) -> List[Player]:
        list_players = []
        for name in names:
            player = Player(name=name, limit=limit)
            list_players.append(player)
        return list_players

    def sort_players(self) -> None:
        # mesmo critério do seu código original:
        # ordenar por hits (desc) e, em seguida, pelo menor tempo total
        self.players.sort(key=lambda x: (x.hits, -x.time_played), reverse=True)

    def pick_question(self) -> Tuple[Player, Dict[str, Any], str]:
        """
        Escolhe um jogador vivo aleatório, define o nível da questão
        e devolve (jogador, question_set, nível).
        """
        if not self.players_alive:
            raise ValueError("No players alive")

        cur_player = choice(self.players_alive)
        hits = cur_player.get_hits()

        if hits < 3:
            cur_question_set = choice(self.easy_questions)
            cur_level = "Fácil"
        elif hits < 8:
            cur_question_set = choice(self.medium_questions)
            cur_level = "Médio"
        else:
            cur_question_set = choice(self.hard_questions)
            cur_level = "Difícil"

        return cur_player, cur_question_set, cur_level

    def answer_question(
        self,
        cur_player: Player,
        cur_question_set: Dict[str, Any],
        ans_letter: str,
        time_to_answer: float,
    ) -> Dict[str, Any]:
        """
        Processa a resposta do jogador e atualiza o estado do jogo.

        Retorna um dicionário com:
            - correct: bool
            - eliminated: bool
            - eliminated_name: Optional[str]
            - finished_for_player: bool  (atingiu 10 acertos)
            - game_over: bool (não há mais jogadores vivos)
            - player_hits: int (acertos atuais do jogador, se ainda vivo)
        """
        alternatives_letters = ["A", "B", "C", "D"]
        cur_player.add_time_played(time_to_answer=time_to_answer)

        hits_before = cur_player.get_hits()
        # Remover a questão que foi feita da lista adequada
        if hits_before < 3:
            if cur_question_set in self.easy_questions:
                self.easy_questions.remove(cur_question_set)
        elif hits_before < 8:
            if cur_question_set in self.medium_questions:
                self.medium_questions.remove(cur_question_set)
        else:
            if cur_question_set in self.hard_questions:
                self.hard_questions.remove(cur_question_set)

        player_index = self.players_alive.index(cur_player)
        answer_index = alternatives_letters.index(ans_letter)

        result: Dict[str, Any] = {
            "correct": False,
            "eliminated": False,
            "eliminated_name": None,
            "finished_for_player": False,
            "game_over": False,
            "player_hits": hits_before,
        }

        if cur_question_set["Resposta"] == answer_index:
            # certa resposta
            cur_player.increment_hits()
            result["correct"] = True
            result["player_hits"] = cur_player.get_hits()
        else:
            # errou -> remove da lista de vivos
            result["correct"] = False
            result["eliminated"] = True
            result["eliminated_name"] = cur_player.name
            self.players_alive.pop(player_index)

        # Checa se o jogador (ainda vivo) atingiu 10 acertos
        if result["correct"] and cur_player in self.players_alive and cur_player.get_hits() == 10:
            self.players_alive.remove(cur_player)
            result["finished_for_player"] = True

        # Verifica se o jogo acabou (ninguém vivo)
        if not self.players_alive:
            result["game_over"] = True

        return result


# ===================== STREAMLIT UI ===================== #


def reset_app_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]


def setup_page_config():
    st.set_page_config(
        page_title="QUIZITOS - Quiz Game of Software Requirements Specification",
        page_icon="🎲",
        layout="centered",
    )


def show_setup_screen():
    st.title("🎮 QUIZITOS - Quiz Game of Software Requirements Specification")
    st.markdown(
        """
    Bem-vindo!  
    Digite os nomes dos jogadores e o limite de acertos para começar.
    """
    )

    names_input = st.text_input(
        "Nomes dos jogadores (separados por vírgula)",
        value="Vitor, Gabriel, Davi, Joao, Micael",
    )

    limit = st.number_input(
        "Limite de acertos para cada jogador (mesmo valor que você usava no Player)",
        min_value=1,
        max_value=50,
        value=10,
        step=1,
    )

    if st.button("🚀 Começar o jogo"):
        names = [n.strip() for n in names_input.split(",") if n.strip()]
        if not names:
            st.warning("Por favor, informe pelo menos um jogador.")
            return

        st.session_state.game = Game(names=names, limit=limit)
        st.session_state.current_question = None  # question + metadata
        st.session_state.question_start_time = None
        st.session_state.last_result = None
        st.rerun()


def prepare_new_question():
    game: Game = st.session_state.game
    cur_player, cur_question_set, cur_level = game.pick_question()

    st.session_state.current_question = {
        "player_name": cur_player.name,
        "player_obj": cur_player,
        "question_set": cur_question_set,
        "level": cur_level,
    }
    st.session_state.question_start_time = time.perf_counter()


def show_game_screen():
    game: Game = st.session_state.game

    st.title("🎲 Quizitos Game")

    # Mostrar mensagem do último resultado, se houver
    last_result = st.session_state.get("last_result")
    if last_result:
        if last_result["correct"]:
            st.success(
                f"✅ {last_result['player_name']} acertou! "
                f"Total de acertos: {last_result['player_hits']}."
            )
        else:
            st.error(
                f"❌ {last_result['player_name']} errou e foi eliminado!"
            )
        if last_result.get("finished_for_player"):
            st.info(
                f"🏆 {last_result['player_name']} já acertou todas as perguntas (10) "
                "e foi removido da lista de jogadores vivos."
            )

        # Limpar para só aparecer uma vez
        st.session_state.last_result = None

    # Se não há mais jogadores vivos, mostrar ranking final
    if not game.players_alive:
        st.subheader("🏁 Fim de jogo!")
        game.sort_players()

        data = [
            {
                "Posição": i + 1,
                "Nome": player.name,
                "Acertos": player.hits,
                "Tempo total (s)": round(player.time_played, 2),
            }
            for i, player in enumerate(game.players)
        ]
        st.table(data)

        if st.button("🔁 Jogar novamente"):
            reset_app_state()
            st.rerun()
        return

    # Se ainda não temos questão atual, sorteia uma
    if st.session_state.current_question is None:
        prepare_new_question()

    cq = st.session_state.current_question
    cur_player_name = cq["player_name"]
    cur_player_obj: Player = cq["player_obj"]
    cur_question_set = cq["question_set"]
    cur_level = cq["level"]

    st.markdown(f"### 👤 Jogador: **{cur_player_name}**")
    st.markdown(f"**Nível da questão:** {cur_level}")

    st.markdown(f"#### ❓ Pergunta")
    st.write(cur_question_set["Pergunta"])

    alternatives = cur_question_set["Alternativas"]
    alternatives_letters = ["A", "B", "C", "D"]
    options = [
        f"{letter}) {text}" for letter, text in zip(alternatives_letters, alternatives)
    ]

    with st.form("answer_form", clear_on_submit=False):
        choice_label = st.radio("Escolha sua resposta:", options, index=0)
        submitted = st.form_submit_button("Responder")

        if submitted:
            # extrai apenas a letra (A, B, C ou D)
            ans_letter = choice_label.split(")")[0].strip()
            end_time = time.perf_counter()
            start_time = st.session_state.question_start_time or end_time
            time_to_answer = end_time - start_time

            result = game.answer_question(
                cur_player=cur_player_obj,
                cur_question_set=cur_question_set,
                ans_letter=ans_letter,
                time_to_answer=time_to_answer,
            )

            st.session_state.last_result = {
                "correct": result["correct"],
                "player_name": cur_player_name,
                "player_hits": result["player_hits"],
                "finished_for_player": result["finished_for_player"],
            }

            # Limpa a questão atual para sortear uma nova no próximo rerun
            st.session_state.current_question = None
            st.session_state.question_start_time = None

            # Recarrega para mostrar feedback e, depois, a próxima questão
            st.rerun()


def main():
    setup_page_config()

    if "game" not in st.session_state:
        show_setup_screen()
    else:
        show_game_screen()


if __name__ == "__main__":
    main()
