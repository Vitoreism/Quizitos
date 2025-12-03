# 🎮 Quizitos - Quiz Game

## Descrição

**Quizitos** é um jogo de quiz interativo e competitivo desenvolvido para fins educacionais, focado na disciplina de **Especificação e Requisitos de Software**, ministrada pela Profa. Dra. **Danielle Rousy Dias Ricarte** do Centro de Informática da UFPB.

O jogo funciona como uma competição entre até 5 jogadores, onde cada participante deve responder a **10 perguntas** de forma aleatória, divididas em três níveis de dificuldade:

- 🟢 **Fácil** (0-2 acertos)
- 🟡 **Médio** (3-7 acertos)
- 🔴 **Difícil** (8+ acertos)

### Mecânica do Jogo

- **Sem ordem fixa**: Os jogadores são selecionados aleatoriamente para responder às perguntas
- **Eliminação instantânea**: Um erro resulta na eliminação automática do jogador
- **Ranking dinâmico**: O jogo termina quando:
  - Apenas um jogador permanece (vencedor automático), ou
  - Todos os jogadores completam 10 acertos (vencedor é quem levou menos tempo)

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** - Linguagem base
- **Streamlit** - Framework para interface web interativa
- **Typing** - Type hints para melhor qualidade de código

## 📋 Requisitos

- Python 3.10 ou superior
- Streamlit

## 🚀 Como Instalar

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/quiz_game.git
cd quiz_game/Quizitos
```

### 2. Instale as Dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install streamlit
```

## 🎮 Como Jogar

### Iniciando o Jogo

1. Execute o aplicativo com:

   ```bash
   streamlit run game.py
   ```

2. Seu navegador abrirá automaticamente na URL `http://localhost:8501`

### Tela de Configuração

1. Digite os **nomes dos jogadores** (separados por vírgula)
   - Padrão: "Vitor, Gabriel, Davi, Joao, Micael"
2. Defina o **limite de acertos** (padrão: 10)
3. Clique em **"🚀 Começar o jogo"**

### Durante o Jogo

1. Um jogador é selecionado aleatoriamente
2. Leia a pergunta e escolha uma alternativa (A, B, C ou D)
3. Clique em **"Responder"**
4. O resultado aparece imediatamente:
   - ✅ Acerto: continue jogando
   - ❌ Erro: você é eliminado
5. O próximo jogador é sorteado automaticamente

### Fim do Jogo

Quando o jogo terminar, você verá um **ranking final** com:

- Posição
- Nome do jogador
- Total de acertos
- Tempo total gasto

## 📁 Estrutura do Projeto

```
Quizitos/
├── game.py          # Lógica principal do jogo e interface Streamlit
├── player.py        # Classe Player (gerencia dados do jogador)
├── data.py          # Banco de perguntas (fácil, médio, difícil)
├── README.md        # Este arquivo
└── requirements.txt # Dependências do projeto
```

## 📚 Banco de Perguntas

O arquivo `data.py` contém:

- **15 perguntas fáceis**
- **25 perguntas médias**
- **10 perguntas difíceis**

Todas relacionadas a Especificação e Requisitos de Software.

## 📖 Como Contribuir

Contribuições são bem-vindas! Para adicionar novas perguntas ou melhorias:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/novas-perguntas`)
3. Commit suas mudanças (`git commit -m 'Add novas perguntas'`)
4. Push para a branch (`git push origin feature/novas-perguntas`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é fornecido como material educacional para a disciplina de Especificação e Requisitos de Software.

## 👨‍💻 Autores

- Vitor Reis, Micael Gomes, João Vitor Sampaio, Gabriel Ribeiro e Davi Alves - Desenvolvimento do Quizitos

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Desenvolvido com ❤️ para fins educacionais na UFPB**
