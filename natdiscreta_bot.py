import telebot, random
from collections import defaultdict
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
save_quiz = defaultdict(dict)

# Questões

cont_questoes = int(0)

questoes = [
    [
        {
            "Pergunta": "O que é um conjunto?",
            "Itens": {
                "A": "Uma lista ordenada de números.",
                "B": "Um agrupamento de elementos que têm uma característica em comum.",
                "C": "Um número específico dentro de uma sequência.",
                "D": "Uma operação matemática que une dois números."
            },
            "Resposta": "B",
            "Valor": 100
        },
        {
            "Pergunta": "O que representa o símbolo ∈ em conjuntos?",
            "Itens": {
                "A": "É o símbolo de união de conjuntos",
                "B": "Indica que um elemento pertence a um conjunto",
                "C": "Representa a interseção entre dois conjuntos",
                "D": "Mostra a diferença entre conjuntos"
            },
            "Resposta": "B",
            "Valor": 100
        },
        {
            "Pergunta": "Qual é o conjunto dos números naturais?",
            "Itens": {
                "A": "Todos os números inteiros, positivos e negativos",
                "B": "Os números positivos, inteiros e sem frações",
                "C": "Apenas os números pares",
                "D": "Todos os números racionais"
            },
            "Resposta": "B",
            "Valor": 100
        }        
    ],
    [
        {
            "Pergunta": "Sejam A={1,2,3} e 𝐵={3,4,5}. Qual é a interseção dos conjuntos A e B?",
            "Itens": {
                "A": "{1,2}",
                "B": "{3}",
                "C": "{1,2,3}",
                "D": "{4,5}"
            },
            "Resposta": "B",
            "Valor": 200
        },
        {
            "Pergunta": "Se A = {2, 4, 6} e B = {1, 2, 3, 4}, qual é A ∩ B?",
            "Itens": {
                "A": "{2, 4}",
                "B": "{6}",
                "C": "{1, 3}",
                "D": "{2, 4, 6}"
            },
            "Resposta": "A",
            "Valor": 200
        },
        {
            "Pergunta": "Se A = {a, b, c} e B = {b, c, d}, qual é A ∪ B?",
            "Itens": {
                "A": "{a, d}",
                "B": "{b, c}",
                "C": "{a, b, c, d}",
                "D": "{a, b, c}"
            },
            "Resposta": "C",
            "Valor": 200
        },    
    ],
    [
        {
            "Pergunta": "Seja a relação R sobre o conjunto A={1,2,3} definida por R={(1,2),(2,3)}. A relação é reflexiva?",
            "Itens": {
                "A": "Sim, pois todo elemento está relacionado consigo mesmo.",
                "B": "Não, pois não existe nenhum par do tipo (x,x) para os elementos de A.",
                "C": "Sim, pois ela é simétrica.",
                "D": "Não, porque a relação é apenas uma sequência de pares ordenados."
            },
            "Resposta": "B",
            "Valor": 500
        },
        {
            "Pergunta": "Se R = {(1,1), (2,2), (3,3)} em A = {1,2,3}, então R é:",
            "Itens": {
                "A": "Simétrica",
                "B": "Transitiva",
                "C": "Reflexiva",
                "D": "Inexistente"
            },
            "Resposta": "C",
            "Valor": 500
        },
        {
            "Pergunta": "Uma relação R é simétrica quando:",
            "Itens": {
                "A": "Para todo (a,b) em R, (b,a) também está em R",
                "B": "Existe ao menos um (a,a) em R",
                "C": "Para todo (a,b), b é maior que a",
                "D": "A soma dos pares é sempre igual"
            },
            "Resposta": "A",
            "Valor": 500
        },
    ],
    [
        {
            "Pergunta": "Seja f:R→R dada por f(x)=x^2. Qual é o contradomínio dessa função?",
            "Itens": {
                "A": "R",
                "B": "R + (os números reais não negativos)",
                "C": "R - (os números reais negativos)",
                "D": "R ∗(os números reais, exceto 0)"
            },
            "Resposta": "B",
            "Valor": 1000
        },
        {
            "Pergunta": "Seja f(x) = √x com domínio x ≥ 0. Qual é seu contradomínio?",
            "Itens": {
                "A": "Números negativos",
                "B": "Apenas inteiros positivos",
                "C": "Números reais não negativos",
                "D": "Todos os reais"
            },
            "Resposta": "C",
            "Valor": 1000
        },
        {
            "Pergunta": "Se f(x) = -x², então a imagem da função é:",
            "Itens": {
                "A": "Todos os reais",
                "B": "Apenas positivos",
                "C": "Números reais não positivos",
                "D": " Inteiros positivos"
            },
            "Resposta": "C",
            "Valor": 1000
        },
    ],
    [
        {
            "Pergunta": "Qual é o valor de f^-1 (4) se f(x)=2x+1?",
            "Itens": {
                "A": "2",
                "B": "3",
                "C": "4",
                "D": "5"
            },
            "Resposta": "A",
            "Valor": 2000
        },
        {
            "Pergunta": "Se f(x) = 3x - 2, qual é f⁻¹(7)?",
            "Itens": {
                "A": "3",
                "B": "2",
                "C": "5",
                "D": "1"
            },
            "Resposta": "A",
            "Valor": 2000
        },
        {
            "Pergunta": "Se f(x) = x/2 + 1, o valor de f⁻¹(5) é:",
            "Itens": {
                "A": "10",
                "B": "8",
                "C": "6",
                "D": "4"
            },
            "Resposta": "A",
            "Valor": 2000
        }
    ],
    [
        {
            "Pergunta": "Seja An =3n+2 a fórmula geral de uma sequência. Qual é o valor de A5?",
            "Itens": {
                "A": "13",
                "B": "15",
                "C": "17",
                "D": "20"
            },
            "Resposta": "C",
            "Valor": 5000
        },
        {
            "Pergunta": "Se An = n² + n, então A3 é:",
            "Itens": {
                "A": "6",
                "B": "9",
                "C": "12",
                "D": "15"
            },
            "Resposta": "C",
            "Valor": 5000
        },
        {
            "Pergunta": "Se a sequência é An = 5n - 1, então A4 vale:",
            "Itens": {
                "A": "20",
                "B": "21",
                "C": "19",
                "D": "16"
            },
            "Resposta": "B",
            "Valor": 5000
        }
    ],
    [
        {
            "Pergunta": "Dada a sequência an =2 ^n, qual é o valor de a6?",
            "Itens": {
                "A": "32",
                "B": "64",
                "C": "128",
                "D": "256"
            },
            "Resposta": "B",
            "Valor": 10000
        },
        {
            "Pergunta": "Na sequência aₙ = 3ⁿ, qual é o valor de a₄?",
            "Itens": {
                "A": "27",
                "B": "81",
                "C": "64",
                "D": "16"
            },
            "Resposta": "B",
            "Valor": 10000
        },
        {
            "Pergunta": "Se aₙ = (-1)ⁿ, qual é o valor de a₅?",
            "Itens": {
                "A": "-1",
                "B": "1",
                "C": "0",
                "D": "5"
            },
            "Resposta": "A",
            "Valor": 10000
        },
    ],
    [
        {
            "Pergunta": "Seja f(x)=x ^3 −4x + 2. Qual é a imagem de f(2)? ou",
            "Itens": {
                "A": "2",
                "B": "6",
                "C": "4",
                "D": "8"
            },
            "Resposta": "A",
            "Valor": 25000
        },
        {
            "Pergunta": "Se f(x) = 2x² - x, qual é o valor de f(3)?",
            "Itens": {
                "A": "15",
                "B": "12",
                "C": "18",
                "D": "19"
            },
            "Resposta": "C",
            "Valor": 25000
        },
        {
            "Pergunta": "Se f(x) = x² - 2x + 1, qual é f(4)?",
            "Itens": {
                "A": "1",
                "B": "4",
                "C": "9",
                "D": "3"
            },
            "Resposta": "C",
            "Valor": 25000
        }
    ],
    [
        {
            "Pergunta": "Seja A={1,2,3,4} e B={3,4,5,6}, e considere a relação R em A x B tal que (a,b) ∈ R se a + b=7. Qual é o conjunto dos pares ordenados de R?",
            "Itens": {
                "A": "{(1,6),(2,5),(3,4),(4,3)}",
                "B": "{(1,5),(2,4),(3,3),(4,2)}",
                "C": "{(1,6),(3,4)}",
                "D": "{(2,5),(4,3)}"
            },
            "Resposta": "A",
            "Valor": 50000
        },
        {
            "Pergunta": "Seja A = {1,2}, B = {3,4}, e R ⊆ A×B tal que a·b é par. Quais pares estão em R?",
            "Itens": {
                "A": "{(1,3), (1,4)}",
                "B": "{(2,3), (2,4)}",
                "C": "{(1,4), (2,4)}",
                "D": "{(2,4)}"
            },
            "Resposta": "C",
            "Valor": 50000
        },
        {
            "Pergunta": "Seja R em A×B com A={1,2,3}, B={4,5}, tal que a + b = número ímpar. Quais os pares de R?",
            "Itens": {
                "A": "{(1,4), (2,5)}",
                "B": "{(1,4), (3,4), (2,5)}",
                "C": "{(2,4), (3,5)}",
                "D": "{(1,5), (3,5)}"
            },
            "Resposta": "A",
            "Valor": 50000
        }
    ],
    [
        {
            "Pergunta": "A sequência de Fibonacci é dada por F0 = 0, F1 = 1, e Fn = Fn−1 + F n−2 para n≥2. Qual é o valor de F7?",
            "Itens": {
                "A": "13",
                "B": "21",
                "C": "34",
                "D": "55"
            },
            "Resposta": "A",
            "Valor": 100000
        },
        {
            "Pergunta": "Na sequência de Fibonacci, qual é o valor de F9?",
            "Itens": {
                "A": "21",
                "B": "34",
                "C": "55",
                "D": "36"
            },
            "Resposta": "C",
            "Valor": 100000
        },
        {
            "Pergunta": "A sequência de Fibonacci é dada por F₀ = 0, F₁ = 1. Qual é a soma dos 6 primeiros termos?",
            "Itens": {
                "A": "20",
                "B": "8",
                "C": "12",
                "D": "7"
            },
            "Resposta": "A",
            "Valor": 100000
        }
    ],
]

# Ajudas

lista_ajudas = [
    {
        'Ajuda': 'Cartas',
        'Disponíveis': 2
    },
    {
        'Ajuda': 'Trocar',
        'Disponíveis': 2
    },
    {
        'Ajuda': 'Pular',
        'Disponíveis': 1
    }
]
ajudas_usadas = []

def exibir_ajudas():
    texto = ""
    for ajuda in lista_ajudas:
        if ajuda['Disponíveis'] > 0:
            texto += f"{ajuda["Disponíveis"]}x {ajuda['Ajuda']} "
    return texto


# Início

texto = """=========💸Bem vindo ao Show do Milhão💸=========
O jogo inclui questões sobre conjuntos, relações, funções, 
        e sequências numéricas, se prepare para forrar!!
                Selecione /iniciar para iniciar o jogo"""
@bot.message_handler(commands=['start'])
def menu(mensagem):
    chat_id = mensagem.chat.id

    bot.send_message(chat_id, texto)


@bot.message_handler(commands=['iniciar'])
def iniciar(mensagem):
    lista_ajudas[0]['Disponíveis'],lista_ajudas[1]['Disponíveis'],lista_ajudas[2]['Disponíveis'] = 2,2,1
    chat_id = mensagem.chat.id
    save_quiz[chat_id] = {
        "Fase": 0,
        "Valor Ganho": 0
    }
    
    quiz(chat_id)


# Quiz

def quiz(chat_id):
    try:
        num_questao = save_quiz[chat_id]['Fase']
        questao_atual = questoes[num_questao][cont_questoes]

        msg = f"""{num_questao+1}ª pergunta valendo R${questao_atual['Valor']}!
    {questao_atual['Pergunta']}
        A. {questao_atual['Itens']['A']}
        B. {questao_atual['Itens']['B']}
        C. {questao_atual['Itens']['C']}
        D. {questao_atual['Itens']['D']}
        
        Ajudas:  {exibir_ajudas()}"""

        bot.send_message(chat_id, msg)
    except IndexError:
        bot.send_message(chat_id,"💸Você venceu o show do milhão!💸")


# Verificando resposta

def verificarResposta(mensagem):
    return len(save_quiz) > 0 and mensagem.text.upper() in ['A','B','C','D']

@bot.message_handler(func=verificarResposta)
def receberResposta(mensagem):
    chat_id = mensagem.chat.id
    save_atual = save_quiz[chat_id]
    num_questao = save_atual['Fase']
    questao_atual = questoes[num_questao][cont_questoes]

    try:
        resposta = mensagem.text.upper()
        if resposta not in ["A","B","C","D"]:
            bot.send_message(chat_id, "Resposta inválida, tente novamente.")
            return
        
        correta = questao_atual['Resposta']
        if correta == resposta:
            bot.send_message(chat_id, f"Resposta correta, você ganhou R${questao_atual['Valor']}")

            save_atual['Fase'] += 1
            save_atual['Valor Ganho'] += questao_atual['Valor']

            quiz(chat_id)
        else:
            bot.send_message(chat_id, f"Você perdeu com R${save_atual['Valor Ganho']}!❌\n Use /iniciar para tentar novamente.")

    except Exception as e:
        print(e)


# Verificando ajudas

def verificar_ajuda(mensagem):
    return mensagem.text.capitalize() in ["Cartas", "Trocar", "Pular"]
    
@bot.message_handler(func=verificar_ajuda)
def usar_ajudas(mensagem):
    global cont_questoes
    chat_id = mensagem.chat.id
    ajuda = mensagem.text.capitalize()
    
    save_atual = save_quiz[chat_id]
    num_questao = save_atual['Fase']
    questao_atual = questoes[num_questao][cont_questoes]
    if ajuda == "Cartas":
        if lista_ajudas[0]['Disponíveis'] > 0:
            lista_ajudas[0]['Disponíveis'] -= 1
            
            resposta = questao_atual['Resposta']
            
            opcoes = ""
            for op in questao_atual['Itens'].keys():
                if op != resposta:
                    opcoes += op
            
            qtd_remover = random.randint(0, 3)
            remover = random.sample(opcoes, qtd_remover)
            
            msg = f"🃏 Cartas usadas! {qtd_remover} alternativa(s) foram removidas:\n\n"
            msg += f"{questao_atual['Pergunta']}\n"
            
            for op, texto in questao_atual['Itens'].items():
                if op not in remover:
                    msg += f"    {op}. {texto}\n"

            bot.send_message(chat_id, msg)

        else:
            bot.send_message(chat_id, "Ajuda indisponível.")
            return

    elif ajuda == "Trocar":
        if lista_ajudas[1]['Disponíveis'] > 0:
            lista_ajudas[1]['Disponíveis'] -= 1
            cont_questoes += 1
            quiz(chat_id)
        else:
            bot.send_message(chat_id, "Ajuda indisponível.")
            return

    elif ajuda == "Pular":
        if lista_ajudas[2]['Disponíveis'] > 0:
            lista_ajudas[2]['Disponíveis'] -= 1
            save_atual['Fase'] += 1
            save_atual['Valor Ganho'] += questao_atual['Valor']
            quiz(chat_id)
        else:
            bot.send_message(chat_id, "Ajuda indisponível.")
            return




bot.polling()