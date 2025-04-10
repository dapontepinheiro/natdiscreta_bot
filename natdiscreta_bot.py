import telebot
from collections import defaultdict
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
save_quiz = defaultdict(dict)

questoes = [
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
        "Pergunta": "Seja f:R→R dada por f(x)=x^2. Qual é o contradomínio dessa função?",
        "Itens": {
            "A": "R",
            "B": "R + (os números reais não negativos)",
            "C": "R - (os números reais negativos)",
            "D": "R ∗(os números reais, exceto 0)"
        },
        "Resposta": "A",
        "Valor": 1000
    },
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
]
ajudas = [...]

def verificarResposta(mensagem):
    if len(save_quiz) > 0:
        return True
    return False

texto = """     Bem vindo ao ===Show do Milhão===
O jogo inclui questões sobre conjuntos, relações, funções, 
e sequências numéricas, se prepare para forrar!!
Selecione /iniciar para iniciar o jogo"""
@bot.message_handler(commands=['start'])
def menu(mensagem):
    chat_id = mensagem.chat.id

    bot.send_message(chat_id, texto)


@bot.message_handler(commands=['iniciar'])
def iniciar(mensagem):
    chat_id = mensagem.chat.id
    save_quiz[chat_id] = {
        "Num Questao": 0,
        "Valor Ganho": 0
    }
    
    quiz(save_quiz, chat_id)

def quiz(save_quiz, chat_id):
    num_questao = save_quiz[chat_id]['Num Questao']
    questao_atual = questoes[num_questao]

    msg = f"""{num_questao+1}ª pergunta valendo R${questao_atual['Valor']}!
{questao_atual['Pergunta']}
    A. {questao_atual['Itens']['A']}
    B. {questao_atual['Itens']['B']}
    C. {questao_atual['Itens']['C']}
    D. {questao_atual['Itens']['D']}"""

    bot.send_message(chat_id, msg)

@bot.message_handler(func=verificarResposta)
def receberResposta(mensagem):
    chat_id = mensagem.chat.id
    save_atual = save_quiz[chat_id]
    num_questao = save_atual['Num Questao']

    try:
        resposta = mensagem.text.upper()
        if resposta not in ["A","B","C","D"]:
            bot.send_message(chat_id, "Resposta inválida, tente novamente.")
            return
        
        correta = questoes[num_questao]['Resposta']
        if correta == resposta:
            bot.send_message(chat_id, f"Resposta correta, você ganhou R${questoes[num_questao]['Valor']}")

            save_atual['Num Questao'] += 1
            save_atual['Valor Ganho'] += questoes[num_questao]['Valor']

            quiz(save_quiz, chat_id)
        else:
            bot.send_message(chat_id, f"Você perdeu com R${save_atual['Valor Ganho']}! Use /iniciar para tentar novamente.")

    except Exception as e:
        print(e)

bot.polling()