# ⚖️ Spec-Driven Legal (SDL)

**Onde a lógica antecede a redação.** Um framework *open-source* para o desenvolvimento estruturado de documentos e estratégias jurídicas.

---

## 🚨 O Problema

A advocacia tradicional, especialmente para jovens advogados, sofre de dois grandes males na hora de redigir documentos:
1. **A Cultura do "Copia e Cola" (Modelões):** Remendar textos de modelos genéricos da internet gera brechas, contradições internas e insegurança jurídica.
2. **O "Vibe Coding" das IAs Generativas:** Pedir para o ChatGPT criar um contrato inteiro a partir de um prompt vago (*"faça um contrato de prestação de serviços"*) resulta em textos prolixos, genéricos e propensos a alucinações.

## 💡 A Solução: O que é o SDL?

Inspirado no *Spec-Driven Development* da Engenharia de Software, o **Spec-Driven Legal (SDL)** é uma metodologia que estabelece uma regra de ouro: **separe a Lógica Jurídica da Prosa Jurídica.**

No Direito, o texto final (o "juridiquês") não deve ser o ponto de partida. Ele é apenas a compilação de uma regra de negócio bem estruturada.

> *"O Direito não é feito de palavras, é feito de lógica. As palavras são apenas a interface."*

No ecossistema SDL, a **Especificação (Spec)** é a única fonte da verdade. Se o contrato precisar mudar, você não altera parágrafos longos no Word; você altera a matriz lógica e "recompila" o documento.

## ⚙️ Como funciona a Arquitetura SDL?

Todo documento ou tese dentro deste repositório é construído com base em 3 pilares estruturais (que refletem a nossa arquitetura de pastas):

1. 📄 **`spec.md` (A Lógica):** Descreve as regras de negócio de forma pura (Quem, o quê, quando, e consequências condicionais). Sem juridiquês. Focado nas regras e *edge cases* (casos extremos).
2. 📄 **`compliance.md` (As Restrições):** O limite legal. Normas imperativas, foro obrigatório, artigos de leis específicas que o documento deve respeitar (Ex: Código Civil, LGPD).
3. 📄 **`draft` ou `prompt` (A Compilação):** O resultado final. Pode ser o texto pronto em `.docx` gerado a partir da Spec, ou o *Prompt Mestre* validado para que uma IA gere o documento de forma determinística e sem alucinações.

---

## 📂 Estrutura deste Repositório

Nós usamos o próprio SDL para criar os conteúdos explicativos deste repositório.

```text
📂 spec-driven-legal
 ┣ 📜 README.md                     <-- Você está aqui (O Manifesto)
 ┣ 📂 01-artigos                    <-- Fundamentos teóricos e científicos do método
 ┃ ┗ 📂 o-que-e-sdl
 ┃   ┣ 📜 spec.md                   <-- Mapa lógico do artigo conceitual
 ┃   ┣ 📜 constraints.md            <-- Restrições de estilo e tamanho
 ┃   ┗ 📜 artigo-final.md           <-- O rascunho compilado final
 ┣ 📂 02-documentos-juridicos       <-- Modelos estáticos no padrão SDL (Prontos para IA)
 ┃ ┗ 📂 nda-simplificado
 ┃   ┣ 📜 spec.md                   <-- Variáveis e regras de negócio do NDA
 ┃   ┣ 📜 compliance.md             <-- Limites e restrições do Direito Brasileiro
 ┃   ┣ 📜 prompt-compilador.txt     <-- Instrução de colagem para chats comuns
 ┃   ┗ 📜 draft-exemplo.md          <-- O contrato final resultante
 ┗ 📂 03-motor-sdl                  <-- MOTOR AUTÔNOMO (Pipeline em Python)
   ┣ 📜 app_sdl.py                  <-- Aplicação com interface gráfica em Gradio
   ┣ 📜 protocolo_sdl_contratos.json <-- Arquivo de configuração das 10 fases da IA
   ┗ 📜 requirements.txt            <-- Dependências de instalação do sistema
```
---

## 🛠️ Como Utilizar o SDL?

Você pode adotar o framework em três níveis diferentes de profundidade, dependendo da sua estrutura tecnológica:

### Nível 1: Modo Agente (Claude Projects, Gemini Gems ou Custom GPTs)
A forma mais elegante de usar o SDL no dia a dia sem programar:
1. Crie uma IA dedicada (Gems, Projects ou GPTs) e chame-a de **Compilador SDL**.
2. Nas **Instruções de Sistema**, cole: 
   > *"Você é o Compilador SDL. Seu papel é receber arquivos de especificação (`spec.md`) com as regras de negócio de um cliente, cruzá-los com as diretrizes de lei (`compliance.md`) que estão no seu conhecimento base e gerar o texto jurídico final (Draft) em formato Markdown. Seja estritamente determinístico, sem inventar regras e sem usar termos prolixos."*
3. Faça o upload dos arquivos `compliance.md` deste repositório na base de conhecimento da IA.
4. No dia a dia, apenas envie a `spec.md` do seu novo cliente e digite: *"Compilar contrato"*.

### Nível 2: Modo Manual (Chat Comum do ChatGPT / Claude)
Caso queira usar o chat tradicional, acesse a pasta do documento desejado (ex: `02-documentos-juridicos/nda-simplificado`), abra o arquivo `prompt-compilador.txt`, copie a instrução mestre, cole a sua `spec` adaptada e envie para a IA.

### Nível 3: O Motor Autônomo (Pipeline de 10 Fases em Python)
Se você busca automação em escala e auditoria de risco com loops de feedback, utilize o nosso script em Python localizado em `03-motor-sdl`. 

O motor executa uma esteira de **10 fases sequenciais**, utilizando modelos rápidos (`gemini-2.0-flash`) para estruturação de dados e modelos profundos (`gemini-1.5-pro`) para escrita e julgamento crítico.

```
Fatos Brutos ➔ Extração ➔ Criação da Spec ➔ Teste de Abusividade (Fase 7)
                                ▲                   │
                                └───── [Se Reprovar]┘
                                        │ [Se Passar]
                                        ▼
                                 Draft Final (.md)
```

#### Como rodar o motor localmente:
```bash
# Entre na pasta do motor
cd 03-motor-sdl

# Instale as dependências
pip install -r requirements.txt

# Configure sua chave de API do Gemini
export GOOGLE_API_KEY="sua_chave_aqui"

# Execute a aplicação
python app_sdl.py
```

---

## 🚀 Como Começar? (Para Jovens Advogados)
Leia os textos na pasta 01-artigos para entender profundamente a mudança de mentalidade (de "redator de textos" para "arquiteto lógico").

Navegue pela pasta 02-documentos-juridicos antes de redigir seu próximo contrato ou petição.

Use nossas specs como guia para entrevistar seus clientes. As perguntas certas geram a especificação certa.

## 🤝 Contribua
O SDL é um projeto colaborativo e de código aberto. Se você mapeou a matriz lógica de um tipo de contrato específico ou de uma petição inicial, faça um pull request. Vamos padronizar o Direito juntos.

## 🚀 Como Usar o Framework na Prática?

O SDL foi desenhado para se adaptar ao ecossistema moderno de Inteligência Artificial. Você pode utilizá-lo de duas formas: o **Modo Agente** (automatizado e recomendado para o dia a dia) ou o **Modo Manual** (via chat comum).

---

### 🤖 Método Avançado: Criando seu "Compilador SDL" (Recomendado)

Em vez de copiar e colar prompts toda vez, você pode encapsular o framework criando uma IA dedicada dentro do **Claude Projects**, **Gemini Gems** ou **Custom GPTs (ChatGPT)**. 

#### 1. Configuração Inicial (Você só faz uma vez):
1. Crie um novo Projeto/Gem/GPT e batize de **"Compilador SDL"**.
2. No campo **Instruções de Sistema (System Instructions / Instructions)**, cole o seguinte comando mestre:

> "Você é o Compilador Oficial do framework Spec-Driven Legal (SDL). Seu único papel é atuar como um engenheiro jurídico determinístico. Você receberá do usuário um arquivo ou texto de especificação (`spec.md`) com as regras de negócio de um cliente. Sua tarefa é cruzar essas informações com as diretrizes de lei e estilo (`compliance.md`) que estão no seu conhecimento base e gerar o texto jurídico final (Draft). Nunca invente cláusulas que não foram parametrizadas na Spec. Escreva em português formal, moderno, limpo e sem prolixidade."

3. Na área de **Conhecimento Base (Knowledge / Files)** da ferramenta, faça o upload dos arquivos de `compliance.md` deste repositório (as regras jurídicas que nunca mudam).

#### 2. Fluxo de Trabalho Diário:
Agora sua IA está pronta. Para criar um documento perfeito para um cliente em segundos, basta abrir o chat do seu Agente e fazer isso:
* **Você:** Faz o upload ou digita a `spec.md` do caso e escreve: *"Compilar NDA"*.
* **A IA:** Lê a lógica do cliente, cruza com a lei que já está na memória dela e entrega o contrato pronto.

---

### 📝 Método Manual: Chat Tradicional (ChatGPT / Claude / Gemini comuns)

Se preferir usar o chat comum sem configurar um agente, você pode fazer a compilação manualmente a cada novo documento:

1. Acesse a pasta do documento desejado neste repositório (ex: `02-documentos-juridicos/nda-simplificado`).
2. Abra os arquivos `spec.md` (ajuste os dados para o seu cliente) e `compliance.md`.
3. Copie o prompt abaixo, preencha os campos e envie para a IA:

```text
Você é o Compilador do framework Spec-Driven Legal (SDL). Sua tarefa é ler a Especificação e as Restrições abaixo e gerar o texto jurídico finalizado (Draft), sem inventar regras ocultas e mantendo um tom moderno e direto.

[ESPECIFICAÇÃO (spec.md)]
(Cole aqui o conteúdo do arquivo spec.md do seu cliente)

[RESTRIÇÕES (compliance.md)]
(Cole aqui o conteúdo do arquivo compliance.md do repositório)

Gere o contrato/peça final:
