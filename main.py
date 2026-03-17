import random
import re
import sys
import google.generativeai as genai
import json

# Sua Chave
GOOGLE_API_KEY = "COLE_AQUI_SUA_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

 # guarda os termos gerados para evitar trazer termos repetidos
historico_termos = []
score = 0


def obtem_termos():

    # Nota: Caso a versão 2.5 não esteja disponível na sua região/conta, 
    # altere para 'gemini-2.0-flash' ou 'gemini-1.5-flash'
    # Usando o modelo disponível
    model = genai.GenerativeModel('gemini-2.5-flash')

    
    # lista para tentar evitar que os termos venham repetidos a cada acesso à IA
    # por ser um codigo apenas para estudo e aprendizado, essa solucao é funcional
    categorias = ["DevOps", "Banco de Dados", "Frontend", "Backend","Cibersegurança", 
                  "Computação em Nuvem", "Inteligência Artificial", "Hardware"]
    categoria_da_vez = random.choice(categorias)
    
    
    # a ideia aqui é trazer uma qtd de termos por acesso, para que o usuário possa responder o quiz
    # sem fazer um novo acesso, evitando exceder a quota na api
    # altere a quantidade que desejar dos termos que serao retornados a cada acesso
    prompt = f"""
    Gere uma lista com EXATAMENTE 3 termos técnicos aleatórios, focando na área de {categoria_da_vez}
    Exclua os seguintes termos {historico_termos}.
    Retorne APENAS um JSON no seguinte formato:
    [
    {{"palavra": "Termo em Português", "traducao": "Termo em Inglês"}}
    ]
    Evite definições, foque na tradução direta.
    """
    
    try:
        response = model.generate_content(prompt)
        
        # Garante que pegamos apenas o JSON, mesmo que a IA retorne lixo
        # Extrai apenas o conteúdo entre colchetes [ ]
        json_match = re.search(r'\[.*\]', response.text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return None
    except Exception as e:
        if "Quota exceeded" in str(e):
            print("\n❌ Cota esgotada no google generativeai. Tente novamente mais tarde.")
        else:
            print(f"Erro na conexão: {e}")
        return None

def iniciar_quiz():
    global historico_termos
    global score

    print("\n--- 🤖 TECH TRANSLATION QUIZ ---\n")
    print("Buscando os termos...")
    
    termos = obtem_termos()
        
    if not termos:
        print("\n❌ Falha ao obter os termos\n")
        return
        
    total = 0
    
    for item in termos:
            
        # O que aparece para o usuário (em Portugues)
        palavra = item.get('palavra')
        # A resposta correta (em Ingles)
        traducao = item.get('traducao')
        
         # Só adiciona se NÃO existe
        if palavra not in historico_termos:
            historico_termos.append(palavra)
        
        total = len(historico_termos)

        print(f"\nComo se diz '{palavra}' em inglês?")
        answer = input("Resposta: ").strip().lower()
        
        if answer == traducao.lower():
            print("✨ EXATO! Você respondeu corretamente.")
            score += 1
        else:
            print(f"❌ Errado! O termo correto é: {traducao}")
    
    main_quiz(score, total)
    

def main_quiz(score, total):
    while True:
        encerrar = input("\nDigite C para continuar ou S para sair, e tecle ENTER: ").strip().upper()   
        if encerrar == "C":
            iniciar_quiz()  # continua o quiz
        elif encerrar == "S":
            # imprime o resumo
            print("\n" + "="*30)
            print(f"RESUMO DO QUIZ")
            print(f"Acertos: {score} de {total}")
            if total > 0:
                print(f"Desempenho: {(score/total)*100:.2f}%")
            else:
                print("Desempenho: N/A (nenhum termo respondido)")
            print("="*30)
            sys.exit()  # Sair do programa
        else:
            print("❌ Digite apenas C ou S")
    
        
if __name__ == "__main__":
    iniciar_quiz()
