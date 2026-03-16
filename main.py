import re
import google.generativeai as genai
import json

# Sua Chave API criada no google AI
GOOGLE_API_KEY = "COLE_AQUI_SUA_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

def obtem_lista_perguntas():
    
    # Nota: Caso a versão 2.5 não esteja disponível na sua região/conta, 
    # altere para 'gemini-2.0-flash' ou 'gemini-1.5-flash'
    # Usando o modelo disponível
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Prompt para obter os termos, altere a quantidade (10) de termos que serao retornados
    # a cada acesso. 
    prompt = """
    Gere uma lista com 10 termos técnicos de TI. 
    Retorne APENAS um JSON no seguinte formato de lista:
    [
      {"palavra": "Termo em Português", "traducao": "Termo em Inglês"},
      ...
    ]
    Evite definições longas, foque na tradução direta do vocabulário técnico.
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

def quiz():
    print("\n--- 🤖 TECH TRANSLATION QUIZ ---\n")
    print("Sorteando palavra...")
    
    perguntas = obtem_lista_perguntas()
        
    if not perguntas:
        return
    
    score = 0
    total = len(perguntas)
    
    for item in perguntas:
        # O que aparece para o usuário (em Portugues)
        palavra = item.get('palavra')
        # A resposta correta (em Ingles)
        traducao = item.get('traducao')
        
        print(f"\nComo se diz '{palavra}' em inglês?")
        answer = input("Resposta: ").strip().lower()
        
        if answer == traducao.lower():
            print("✨ EXATO! Você está afiado.")
            score += 1
        else:
            print(f"❌ Errado! O termo correto é: {traducao}")
    
    
    print("\n" + "="*30)
    print(f"RESUMO DO QUIZ")
    print(f"Acertos: {score} de {total}")
    print(f"Desempenho: {(score/total)*100:.2f}%")
    print("="*30)
    
if __name__ == "__main__":
    quiz()
