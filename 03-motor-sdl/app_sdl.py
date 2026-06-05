# ╔════════════════════════════════════════════════════════════════════════════╗
# ║ MOTOR DE ENGENHARIA JURÍDICA SDL (Spec-Driven Legal) v1.0                 ║
# ║ Pipeline Autônomo de Redação e Auditoria Contratual/Processual           ║
# ╚════════════════════════════════════════════════════════════════════════════╝

import os
import json
import time
from datetime import datetime
import gradio as gr
import google.generativeai as genai

# ==================== 1. CONFIGURAÇÃO DO AMBIENTE ====================

api_key = os.getenv("GOOGLE_API_KEY", "SUA_API_KEY_AQUI")
if api_key and api_key != "SUA_API_KEY_AQUI": 
    genai.configure(api_key=api_key)

# Modelos recomendados para otimização de custo/performance
model_flash = genai.GenerativeModel("gemini-2.0-flash-exp")  # Rápido e estruturado para lógica
model_pro = genai.GenerativeModel("gemini-1.5-pro-002")      # Profundo para auditoria e redação final

ARQUIVO_CONFIG = "protocolo_sdl_contratos.json"
MAX_ITERACOES = 3  # Limite de loops se a Spec falhar na auditoria legal

# ==================== 2. GERENCIAMENTO DO PROTOCOLO SDL ====================

def carregar_protocolo_sdl():
    """Carrega as diretrizes do pipeline do framework"""
    try:
        with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as f:
            conteudo = f.read()
            json.loads(conteudo)
            return conteudo
    except (FileNotFoundError, json.JSONDecodeError):
        return criar_protocolo_sdl_padrao()

def criar_protocolo_sdl_padrao():
    """Define as 10 fases nativas do Spec-Driven Legal"""
    protocolo_sdl = [
        {"fase": 0, "nome": "CAPTURA_FATOS", "modelo": "flash", "tipo_saida": "json", 
         "missao": "Extraia do input do cliente um JSON estruturado com: PARTES, OBJETO_PRINCIPAL, CONDICOES_FINANCEIRAS, PRAZOS, ANEXOS_CITADOS, GAPS_DE_INFORMAÇÃO."},

        {"fase": 1, "nome": "MAPEAMENTO_RISCOS", "modelo": "flash", "tipo_saida": "json",
         "missao": "Analise o caso e liste vulnerabilidades do negócio em JSON: RISCO_INADIMPLEMENTO, RISCO_RESCISAO, DIRETRIZES_DE_MUTA_E_PENALIDADES."},

        {"fase": 2, "nome": "INVENTARIO_LEGAL", "modelo": "flash", "tipo_saida": "json",
         "missao": "Identifique as restrições legislativas brasileiras aplicáveis. Retorne JSON: LEIS_IMPERATIVAS, JURISPRUDENCIA_STJ_STF, REQUISITOS_DE_VALIDADE."},

        {"fase": 3, "nome": "CONSTRUCAO_SPEC", "modelo": "flash", "tipo_saida": "texto",
         "missao": "Crie o arquivo 'spec.md' em Markdown puro. Escreva a matriz lógica do contrato (Se acontecer X, a consequência é Y). Proibido juridiquês, foque em regras estruturadas."},

        {"fase": 4, "nome": "CONSTRUCAO_COMPLIANCE", "modelo": "flash", "tipo_saida": "texto",
         "missao": "Crie o arquivo 'compliance.md' em Markdown puro. Liste os limites imperativos legais encontrados na fase 2 que este documento deve respeitar obrigatoriamente."},

        {"fase": 5, "nome": "ESTRESSE_CONTRATUAL", "modelo": "flash", "tipo_saida": "json",
         "missao": "Simule 3 cenários de falha jurídica (ex: falência, quebra de sigilo). Retorne JSON com cenários, impactos na spec e sugestões de blindagem contratual."},

        {"fase": 6, "nome": "REFINAMENTO_LOGICO", "modelo": "pro", "tipo_saida": "json",
         "missao": "Incorpore as melhorias dos cenários de estresse na lógica anterior. Retorne JSON indicando o mapa de alterações finais aplicadas na estrutura lógica."},

        {"fase": 7, "nome": "AUDITORIA_CRUCIALIDADE", "modelo": "pro", "tipo_saida": "json",
         "missao": "Submeta a Spec ao teste de legalidade contra o Compliance. Avalie (0.0-1.0): LEGALIDADE, AUSENCIA_DE_ABUSIVIDADE, CLAREZA, PROTECAO_CONTRA_RISCOS. Retorne JSON com: SCORE_SEGURANCA (média), LIMIAR_APROVACAO (0.75), PASSOU (bool), ACAO (PROSSEGUIR ou VOLTAR_FASE_3), AJUSTES_NECESSARIOS (array)."},

        {"fase": 8, "nome": "LOCK_SPEC", "modelo": "pro", "tipo_saida": "json",
         "missao": "Tranque a especificação. Retorne JSON consolidando as variáveis finais, confirmando que a lógica está blindada e pronta para compilação textual."},

        {"fase": 9, "nome": "DRAFT_COMPILATION", "modelo": "pro", "tipo_saida": "texto",
         "missao": "Atue como o Compilador SDL. Traduza a spec.md e compliance.md validados na timeline em um instrumento jurídico completo em Markdown. Use linguagem formal moderna, clara, sem prolixidade ou clichês jurídicos arcaicos."}
    ]

    protocolo_json = json.dumps(protocolo_sdl, ensure_ascii=False, indent=2)
    try:
        with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as f:
            f.write(protocolo_json)
    except Exception:
        pass
    return protocolo_json

def salvar_protocolo_sdl(conteudo):
    try:
        protocolo = json.loads(conteudo)
        if not isinstance(protocolo, list):
            return "❌ Erro: O protocolo precisa ser uma lista JSON."
        with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as f:
            f.write(conteudo)
        return f"✅ Protocolo SDL salvo com sucesso ({len(protocolo)} fases)."
    except Exception as e:
        return f"❌ Erro na validação do JSON: {str(e)}"

# ==================== 3. ENGINE DE EXECUÇÃO DO FRAMEWORK ====================

def executar_fase_sdl(timeline, config, fase_atual):
    modelo = model_pro if config.get("modelo") == "pro" else model_flash
    contexto = json.dumps(timeline, ensure_ascii=False, indent=2)

    prompt = f"""--- TIMELINE DE ENGENHARIA JURÍDICA ---
{contexto}

--- DIRETRIZ DE EXECUÇÃO ---
AGENTE_SDL: {config['nome']}
FASE DO PIPELINE: {fase_atual}/10
FORMATO_SAIDA: {config['tipo_saida']}

--- MISSÃO DO AGENTE ---
{config['missao']}

--- REGRAS RESTRITAS ---
1. Baseie-se estritamente na timeline de fatos. Não invente premissas.
2. {"Retorne EXCLUSIVAMENTE um JSON válido" if config['tipo_saida'] == 'json' else "Retorne o documento formatado em Markdown clássico."}
3. Evite juridiquês arcaico ou textos prolixos.
"""
    log = f"\n🔹 Fase {fase_atual}: {config['nome']}"
    try:
        inicio = time.time()
        resp = modelo.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2 if config['tipo_saida'] == 'json' else 0.6,
                "max_output_tokens": 8000
            }
        )
        output_raw = resp.text
        tempo = time.time() - inicio

        if config['tipo_saida'] == 'json':
            output_limpo = output_raw.strip().replace('```json', '').replace('```', '')
            content = json.loads(output_limpo)
        else:
            content = output_raw

        log += f" ✓ ({tempo:.1f}s)"
        return {"role": "assistant", "agent": config['nome'], "fase": config['fase'], "content": content}, log, True
    except Exception as e:
        log += f" ✗ FALHA: {str(e)[:50]}"
        return {"role": "system", "agent": config['nome'], "fase": config['fase'], "error": str(e)}, log, False

# ==================== 4. ORQUESTRADOR E LOOP DE REFINAMENTO ====================

def orquestrador_sdl(texto, arquivo, history, json_config):
    anexo_conteudo = ""
    if arquivo:
        try:
            with open(arquivo.name, "r", encoding="utf-8") as f:
                anexo_conteudo = f"\n\n--- DOCUMENTO ANEXO ---\n{f.read()}\n"
        except Exception as e:
            anexo_conteudo = f"\n[Falha ao ler o anexo: {e}]\n"

    input_completo = f"{texto}\n{anexo_conteudo}".strip()
    if not input_completo:
        yield history, {}, "⚠️ Por favor, insira os fatos do caso ou anexe um documento."
        return

    history = history + [[texto + (" 📎 (Anexo)" if arquivo else ""), None]]
    
    try:
        protocolo = json.loads(json_config)
    except Exception as e:
        history[-1][1] = f"❌ Erro na leitura das configurações JSON: {e}"
        yield history, {}, "Erro no JSON"
        return

    timeline = [{"role": "user", "content": input_completo, "timestamp": datetime.now().isoformat()}]
    logs = f"🚀 COMPILADOR AGENTE SDL INICIADO: {datetime.now().strftime('%H:%M:%S')}\n=======\n"
    
    history[-1][1] = "⏳ **Iniciando Engenharia Jurídica...**\n\nProcessando Fase 0: Captura de Fatos..."
    yield history, timeline, logs

    # Fases 0 a 6: Sequenciais estruturais
    fases_iniciais = [f for f in protocolo if f['fase'] < 7]
    for cfg in fases_iniciais:
        fase_num = cfg['fase']
        history[-1][1] = f"⚙️ **Fase {fase_num}/10: {cfg['nome']}**\nConstruindo matriz estrutural..."
        yield history, timeline, logs

        resultado, log_add, sucesso = executar_fase_sdl(timeline, cfg, fase_num)
        timeline.append(resultado)
        logs += log_add + "\n"

        if not sucesso:
            history[-1][1] = f"❌ Erro crítico na Fase {fase_num}. Verifique a aba de depuração."
            yield history, timeline, logs
            return
        yield history, timeline, logs

    # Loop Iterativo: Fase 7 (Auditoria) ↔ Fases 3-6 (Ajuste Lógico da Spec)
    iteracao = 0
    spec_aprovada = False
    cfg_fase7 = next((f for f in protocolo if f['fase'] == 7), None)

    while iteracao < MAX_ITERACOES and not spec_aprovada:
        iteracao += 1
        logs += f"\n🔄 LOOP DE AUDITORIA CONTRATUAL: TESTE {iteracao}/{MAX_ITERACOES}\n"

        if iteracao > 1:
            history[-1][1] = f"🔄 **Ajustando Spec (Tentativa {iteracao})**: Corrigindo vulnerabilidades contratuais..."
            yield history, timeline, logs
            
            fases_reajuste = [f for f in protocolo if 3 <= f['fase'] < 7]
            for cfg in fases_reajuste:
                resultado, log_add, sucesso = executar_fase_sdl(timeline, cfg, cfg['fase'])
                timeline.append(resultado)
                logs += log_add + "\n"
                if not sucesso: return
                yield history, timeline, logs

        history[-1][1] = f"🧪 **Fase 7/10: Auditoria Contratual**\nValidando cláusulas contra brechas e abusividades..."
        yield history, timeline, logs

        resultado, log_add, sucesso = executar_fase_sdl(timeline, cfg_fase7, 7)
        timeline.append(resultado)
        logs += log_add + "\n"

        if not sucesso: return

        dados_auditoria = resultado.get('content', {})
        spec_aprovada = dados_auditoria.get('PASSOU', False)
        score = dados_auditoria.get('SCORE_SEGURANCA', 0)

        if spec_aprovada:
            logs += f"✅ SPEC APROVADA NA AUDITORIA (Score: {score:.2f})\n"
        else:
            logs += f"⚠️ SPEC REPROVADA (Score: {score:.2f}). Reiniciando reajuste lógico.\n"
            vulnerabilidades = dados_auditoria.get('AJUSTES_NECESSARIOS', [])
            history[-1][1] = f"⚠️ **Spec Reprovada na Auditoria (Score: {score:.2f})**\n\nCorrigindo falhas mapeadas:\n" + "\n".join(f"- {v}" for v in vulnerabilidades[:4])
        yield history, timeline, logs

    # Fases Finais: 8 e 9 (Geração do Documento Final)
    fases_finais = [f for f in protocolo if f['fase'] >= 8]
    for cfg in fases_finais:
        fase_num = cfg['fase']
        history[-1][1] = f"📝 **Fase {fase_num}/10: {cfg['nome']}**\nCompilando documento final..."
        yield history, timeline, logs

        resultado, log_add, sucesso = executar_fase_sdl(timeline, cfg, fase_num)
        timeline.append(resultado)
        logs += log_add + "\n"

        if not sucesso: return

        if cfg['fase'] == 9:
            history[-1][1] = resultado.get('content', '# Erro na compilação do texto jurídico')
        yield history, timeline, logs

    logs += f"\n=======\n✅ CONCLUÍDO COM SUCESSO!\nIterações de auditoria realizadas: {iteracao}\n"
    yield history, timeline, logs

# ==================== 5. INTERFACE DO USUÁRIO (GRADIO UI) ====================

def build_app_sdl():
    config_padrao = carregar_protocolo_sdl()
    
    with gr.Blocks(title="⚖️ Motor de Engenharia Jurídica SDL", css="footer {display: none !important;}", theme=gr.themes.Soft()) as app:
        gr.Markdown("""
        # ⚖️ Motor de Engenharia Jurídica SDL (Spec-Driven Legal)
        ### Framework de Redação e Validação de Contratos e Peças Baseado em Especificações Lógicas
        """)

        with gr.Tabs():
            with gr.Tab("📝 Compilador Jurídico"):
                chatbot = gr.Chatbot(label="", show_label=False, height=600, show_copy_button=True, render_markdown=True, type="tuples")
                
                with gr.Row():
                    with gr.Column(scale=9):
                        txt_input = gr.Textbox(show_label=False, placeholder="Insira a narrativa do cliente, acordos preliminares ou os fatos brutos da petição...", lines=2, container=False)
                    with gr.Column(scale=1, min_width=50):
                        file_input = gr.UploadButton("📎", file_types=[".txt", ".md", ".json", ".pdf", ".docx"])
                    with gr.Column(scale=2, min_width=100):
                        btn_run = gr.Button("🚀 Compilar Draft", variant="primary")
                
                status_anexo = gr.Markdown("")
                file_input.upload(lambda f: f"📎 **Documento anexado:** {os.path.basename(f.name)}", file_input, status_anexo)

            with gr.Tab("🔍 Matriz de Depuração (Timeline)"):
                gr.Markdown("### Linha do Tempo das Fases (Variáveis e Lógica em JSON)")
                out_timeline = gr.JSON(label="Pipeline State")
                gr.Markdown("### Logs do Compilador")
                out_logs = gr.Textbox(label="Logs", lines=20, max_lines=40)

            with gr.Tab("⚙️ Configurar Pipeline (JSON)"):
                gr.Markdown("### Personalização das Missões das 10 Fases da IA")
                with gr.Row():
                    btn_save_config = gr.Button("💾 Salvar Configurações do Pipeline", variant="primary")
                    status_save = gr.Label(show_label=False)
                
                editor_codigo = gr.Code(value=config_padrao, language="json", lines=25)
                btn_save_config.click(salvar_protocolo_sdl, editor_codigo, status_save)

        # Eventos de gatilho
        inputs_list = [txt_input, file_input, chatbot, editor_codigo]
        outputs_list = [chatbot, out_timeline, out_logs]
        
        btn_run.click(orquestrador_sdl, inputs=inputs_list, outputs=outputs_list).then(lambda: (None, ""), outputs=[txt_input, status_anexo])
        txt_input.submit(orquestrador_sdl, inputs=inputs_list, outputs=outputs_list).then(lambda: (None, ""), outputs=[txt_input, status_anexo])

    return app

if __name__ == "__main__":
    app = build_app_sdl()
    app.launch(server_name="0.0.0.0", server_port=7860, show_error=True)
