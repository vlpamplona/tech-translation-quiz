# 🤖 Tech Translation Quiz (Gemini AI)

Um quiz interativo em Python que utiliza a Inteligência Artificial do Google (Gemini) para gerar desafios de tradução de termos técnicos de TI.

## 🚀 Diferenciais Técnicos

*   **Otimização de Chamadas:** O sistema solicita múltiplos termos numa única requisição à API, reduzindo o consumo da cota gratuita e tornando o treino mais fluido.
*   **Tratamento de Erros:** Tratamento de exceções para erros de cota (`Quota exceeded`), garantindo que o programa informe ao usuário.
*   **Flexibilidade de Conteúdo:** O prompt foi estruturado para garantir que a IA retorne apenas dados estruturados (JSON), validados via Expressões Regulares (Regex).

## 🛠️ Tecnologias Utilizadas

*   **Python 3.9+**
*   **Google Generative AI** (`google-generativeai`)
*   **Modelo:** `gemini-2.5-flash` (Utilizando as capacidades mais recentes e experimentais da API do Google para maior velocidade e precisão).
*   **Regex & JSON:** Para parsing e limpeza de dados da IA.

## 📋 Configuração e Uso

### 1. Obter Chave de API (Gratuita)

Para rodar o projeto, é necessário uma chave própria:

1.  Link [Google AI Studio](https://aistudio.google.com).
2.  Criar sua chave em **"Create API key"**.
3.  Copie e cole a API KEY no código python (main.py)

### 2. Como Funciona
O script faz uma chamada ao modelo gemini-2.5-flash para obter a lista de termos. Se a cota gratuita do Google estiver esgotada no momento, o código captura o erro e avisa ao usuário.

### 3. Instalação Google Generative AI

```bash
pip install google-generativeai
