"""
Este arquivo conterá os dados para o jogo, no caso, terão as perguntas,
e essas perguntas estarão num formato de:

LISTA DE DICIONÁRIOS: List[Dict[str, List, int]]
"""


EASY_QUESTIONS = [
  {
    "Pergunta": "O que é um requisito de software?",
    "Alternativas": [
      "Um tipo de hardware.",
      "Uma linguagem de programação.",
      "Uma necessidade ou condição que o sistema deve atender.",
      "Um teste automatizado."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Requisitos funcionais descrevem:",
    "Alternativas": [
      "A cor da interface.",
      "O banco de dados utilizado.",
      "O formato do manual.",
      "O que o sistema deve fazer."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "Requisitos não funcionais descrevem:",
    "Alternativas": [
      "Funções do usuário.",
      "Atributos de qualidade e restrições.",
      "Telas do sistema.",
      "A lógica de programação."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Quem são os stakeholders?",
    "Alternativas": [
      "Apenas desenvolvedores.",
      "Só usuários finais.",
      "Pessoas interessadas no sistema.",
      "Apenas a gerência."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Qual é uma técnica comum de elicitação?",
    "Alternativas": [
      "Entrevistas.",
      "Compilação.",
      "Deploy.",
      "Refatoração."
    ],
    "Resposta": 0
  },
  {
    "Pergunta": "Requisitos de usuário são escritos para:",
    "Alternativas": [
      "Somente programadores.",
      "O suporte técnico.",
      "A área de marketing.",
      "Usuários e clientes."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "Requisitos completos devem:",
    "Alternativas": [
      "Ser escritos informalmente.",
      "Incluir todas as necessidades.",
      "Ser vagos.",
      "Evitar detalhes."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Um requisito deve ter um:",
    "Alternativas": [
      "Endereço IP.",
      "Nome de servidor.",
      "ID único.",
      "Formato HTML."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Requisitos ambíguos causam:",
    "Alternativas": [
      "Interpretações diferentes.",
      "Aumento da velocidade.",
      "Menos validações.",
      "Documentação desnecessária."
    ],
    "Resposta": 0
  },
  {
    "Pergunta": "O que é Engenharia de Requisitos?",
    "Alternativas": [
      "Codificar o sistema.",
      "Testar o software.",
      "Desenhar interfaces.",
      "O processo de descobrir, analisar e documentar requisitos."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "Regras de negócio são:",
    "Alternativas": [
      "Códigos-fonte do sistema.",
      "Políticas e normas do domínio.",
      "Documentos de design.",
      "Regras de UI."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Requisitos de desempenho tratam de:",
    "Alternativas": [
      "Layout da interface.",
      "Cores e estilos.",
      "Velocidade e resposta do sistema.",
      "Banco de dados escolhido."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "O modelo cascata é:",
    "Alternativas": [
      "Linear e sequencial.",
      "Totalmente flexível.",
      "Sem fases definidas.",
      "Baseado em adivinhação."
    ],
    "Resposta": 0
  },
  {
    "Pergunta": "Métodos ágeis são:",
    "Alternativas": [
      "Rígidos e lineares.",
      "Sem planejamento.",
      "Baseados em hardware.",
      "Adaptáveis e iterativos."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "A engenharia de requisitos começa quando:",
    "Alternativas": [
      "O código está pronto.",
      "Existe uma necessidade de negócio.",
      "As telas estão desenhadas.",
      "O hardware está comprado."
    ],
    "Resposta": 1
  }
]


MEDIUM_QUESTIONS = [
  {
    "Pergunta": "Requisitos de sistema servem para:",
    "Alternativas": [
      "Definir apenas regras burocráticas.",
      "Descrever em detalhe o que deve ser implementado.",
      "Organizar o banco de dados.",
      "Projetar a interface."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Por que requisitos não funcionais são importantes?",
    "Alternativas": [
      "Porque sempre são opcionais.",
      "Porque definem a interface gráfica.",
      "Porque podem tornar o sistema inutilizável se ignorados.",
      "Porque substituem requisitos funcionais."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Requisitos organizacionais incluem:",
    "Alternativas": [
      "Funções matemáticas.",
      "Padrões internos e políticas da empresa.",
      "Requisitos de domínio.",
      "Regras de usabilidade."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "O que causa problemas segundo o estudo 'Naming the Pain in RE'?",
    "Alternativas": [
      "Excesso de hardware.",
      "Metodologias ágeis.",
      "Requisitos incompletos ou não documentados.",
      "Arquiteturas pequenas."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Requisitos de domínio representam:",
    "Alternativas": [
      "O uso de UML.",
      "Regras específicas do contexto do negócio.",
      "O design visual.",
      "As técnicas de teste."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Uma característica de um requisito consistente é:",
    "Alternativas": [
      "Ser curto.",
      "Não entrar em conflito com outros requisitos.",
      "Ser difícil de implementar.",
      "Ser subjetivo."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "A perspectiva dos requisitos existe para:",
    "Alternativas": [
      "Definir a arquitetura.",
      "Reduzir documentação.",
      "Comunicar requisitos a diferentes tipos de stakeholders.",
      "Criar protótipos."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Um requisito verificável deve:",
    "Alternativas": [
      "Ser subjetivo.",
      "Não possuir métricas.",
      "Ter critérios claros de validação.",
      "Ser ambíguo."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Requisitos funcionais de usuário são:",
    "Alternativas": [
      "Arquiteturas completas.",
      "Linhas de código.",
      "Declarações de alto nível sobre o que o sistema deve fazer.",
      "Diagramas UML."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "O desenvolvimento iterativo permite:",
    "Alternativas": [
      "Processo rígido.",
      "Ajustes rápidos e ciclos curtos.",
      "Ausência de feedback.",
      "Uma única entrega."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Requisitos externos incluem:",
    "Alternativas": [
      "Aparência da interface.",
      "Velocidade de CPU.",
      "Leis, normas e fatores externos ao sistema.",
      "Funções internas do usuário."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Um exemplo de requisito não funcional é:",
    "Alternativas": [
      "O sistema deve cadastrar clientes.",
      "O sistema deve permitir login.",
      "O sistema deve emitir relatórios.",
      "O sistema deve responder em até 2 segundos."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "O principal risco de requisitos abstratos é:",
    "Alternativas": [
      "Interpretar de maneiras diferentes.",
      "Facilitar implementação.",
      "Eliminar testes.",
      "Reduzir retrabalho."
    ],
    "Resposta": 0
  },
  {
    "Pergunta": "Atributos de requisitos incluem:",
    "Alternativas": [
      "O sistema operacional.",
      "Fonte, estado, tipo e testes.",
      "O modelo de rede.",
      "A máquina do servidor."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Quando requisitos mudam constantemente:",
    "Alternativas": [
      "O projeto fica mais rápido.",
      "Os testes diminuem.",
      "A equipe trabalha menos.",
      "Há retrabalho e instabilidade no projeto."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "Por que requisitos precisam ser validados?",
    "Alternativas": [
      "Para substituir testes.",
      "Para reduzir a equipe.",
      "Para garantir que representam realmente as necessidades dos stakeholders.",
      "Para definir o banco de dados."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Requisitos incompletos geram:",
    "Alternativas": [
      "Arquitetura mais simples.",
      "Rework e falhas.",
      "Maior produtividade.",
      "Menos comunicação."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Requisitos de negócio são:",
    "Alternativas": [
      "Histórias de usuário.",
      "Detalhes técnicos.",
      "Regras de interface.",
      "Objetivos de alto nível da organização."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "Qual problema é frequente em requisitos de domínio?",
    "Alternativas": [
      "Especialistas deixam conhecimento implícito.",
      "Nunca há ambiguidade.",
      "Sempre existem métricas.",
      "A linguagem é sempre clara."
    ],
    "Resposta": 0
  },
  {
    "Pergunta": "Em métodos ágeis:",
    "Alternativas": [
      "A especificação é proibida.",
      "A especificação ainda existe, mas é evolutiva.",
      "Nunca há requisitos.",
      "O backlog substitui o sistema."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Requisitos de produto incluem:",
    "Alternativas": [
      "O layout das telas.",
      "Confiabilidade, desempenho e portabilidade.",
      "O salário da equipe.",
      "O idioma do time."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Uma boa especificação deve ser:",
    "Alternativas": [
      "Repleta de jargões.",
      "Clara, precisa e compreensível.",
      "Sem detalhes.",
      "Ambígua."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "A engenharia de requisitos envolve:",
    "Alternativas": [
      "Somente testes.",
      "Elicitação, análise, documentação e validação.",
      "Apenas modelagem de dados.",
      "Apenas codificação."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Exemplo de erro comum em requisitos:",
    "Alternativas": [
      "Seguir padrões.",
      "Confundir requisitos com soluções.",
      "Usar linguagem clara.",
      "Deixar tudo explícito."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Um requisito rastreável permite:",
    "Alternativas": [
      "Aumentar ambiguidade.",
      "Eliminar revisão.",
      "Reduzir testes.",
      "Acompanhar mudanças e impactos."
    ],
    "Resposta": 3
  }
]


HARD_QUESTIONS = [
  {
    "Pergunta": "Por que requisitos mal documentados geram retrabalho?",
    "Alternativas": [
      "Porque reduzem testes.",
      "Porque aceleram o projeto.",
      "Porque levam a interpretações diferentes e soluções incorretas.",
      "Porque exigem menos validações."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Requisitos não funcionais podem ser mais críticos porque:",
    "Alternativas": [
      "Tornam o sistema mais bonito.",
      "Sempre são opcionais.",
      "Substituem requisitos funcionais.",
      "Um sistema pode se tornar inutilizável sem eles."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "Quando a confiança entre cliente e equipe é baixa, a especificação deve ser:",
    "Alternativas": [
      "Menos detalhada.",
      "Mais formal e detalhada.",
      "Inexistente.",
      "Substituída por protótipos."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "O que diferencia um requisito funcional de sistema de um de usuário?",
    "Alternativas": [
      "Não há diferença.",
      "Usuário sempre é mais técnico.",
      "Sistema descreve detalhes; usuário descreve visão geral.",
      "Sistema sempre é abstrato."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "Um problema grave citado nos slides é:",
    "Alternativas": [
      "Documentação organizada.",
      "Falhas de comunicação entre time e clientes.",
      "Uso de diagramas.",
      "Excesso de revisões."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Por que requisitos devem ser verificáveis?",
    "Alternativas": [
      "Para remover métricas.",
      "Para aumentar subjetividade.",
      "Para reduzir detalhes.",
      "Para permitir testes objetivos."
    ],
    "Resposta": 3
  },
  {
    "Pergunta": "Um requisito inconsistente causa:",
    "Alternativas": [
      "Maior produtividade.",
      "Conflitos que impedem implementação correta.",
      "Interfaces melhores.",
      "Menos reuniões."
    ],
    "Resposta": 1
  },
  {
    "Pergunta": "Requisitos de domínio mal especificados podem:",
    "Alternativas": [
      "Facilitar testes.",
      "Reduzir documentação.",
      "Comprometer o funcionamento do sistema.",
      "Melhorar velocidade."
    ],
    "Resposta": 2
  },
  {
    "Pergunta": "O processo de ER deve garantir que requisitos sejam:",
    "Alternativas": [
      "Corretos, completos, consistentes e verificáveis.",
      "Minimizados.",
      "Subjetivos.",
      "Curtos e vagos."
    ],
    "Resposta": 0
  },
  {
    "Pergunta": "Requisitos abstratos demais causam:",
    "Alternativas": [
      "Arquitetura fixa.",
      "Menos testes.",
      "Documentação melhor.",
      "Ambiguidade e erros de interpretação."
    ],
    "Resposta": 3
  }
]