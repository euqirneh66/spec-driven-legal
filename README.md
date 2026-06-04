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
📦 spec-driven-legal
 ┣ 📜 README.md                     <-- Você está aqui (O Manifesto)
 ┣ 📂 01-artigos                    <-- Artigos científicos e tutoriais
 ┃ ┗ 📂 o-que-e-sdl
 ┃   ┣ 📜 spec.md
 ┃   ┣ 📜 constraints.md
 ┃   ┗ 📜 artigo-final.md
 ┗ 📂 02-documentos-juridicos       <-- Modelos de documentos no padrão SDL
   ┗ 📂 nda-simplificado
     ┣ 📜 spec.md                   <-- Regras de negócio do NDA
     ┣ 📜 compliance.md             <-- Limites legais do NDA
     ┗ 📜 template.txt              <-- Prompt/Output final do NDA
