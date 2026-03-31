import streamlit as st
import json

st.set_page_config(page_title="Automatisation Claude → Slack", layout="wide")
st.title("Automatisation Claude API → Slack")

# --- PARTIE 1 : Visualisation / Modélisation ---
st.header("1️⃣ Visualisation du flux")

st.text("""
Flux simplifié :  

[ Workflow principal ]
          │
          ▼
[ Connecteur des connecteurs (C) ]
          │
 ┌────────┴─────────┐
 │                  │
▼                  ▼
Claude API        Slack

Blocs :  
- Claude API : génère ou récupère le contenu  
- Connecteur C : stocke clés, identifiants, prépare le mapping et les transformations  
- Slack : reçoit le contenu et le poste dans le canal ciblé
""")

# --- PARTIE 2 : Remplissage des paramètres ---
st.header("2️⃣ Remplissage des blocs / paramètres")

# Claude API
st.subheader("Claude API")
claude_model = st.selectbox("Modèle Claude", ["claude-1", "claude-2", "claude-instant"])
claude_api_key = st.text_input("API Key Claude", placeholder="sk-123abc456def")
claude_endpoint = st.text_input("Endpoint URL Claude", value="https://api.claude.ai/v1/generate")
claude_prompt = st.text_area("Prompt à envoyer à Claude", placeholder="Résumé du rapport...")

# Connecteur C
st.subheader("Connecteur des connecteurs (C)")
mapping_example = st.text_input("Mapping Claude → Slack", placeholder="text → blocks[0].text")
enable_logs = st.checkbox("Activer logs / suivi erreurs", value=True)

# Slack
st.subheader("Slack")
slack_token = st.text_input("Token OAuth Slack", placeholder="xoxb-9876543210-abcdef")
slack_channel = st.text_input("Channel ID Slack", placeholder="C0123456789")
slack_format = st.selectbox("Format du message Slack", ["Texte simple", "Blocks (JSON)"])

# --- Générer configuration JSON ---
if st.button("Générer flux JSON"):
    flux_config = {
        "Claude_API": {
            "model": claude_model,
            "api_key": claude_api_key,
            "endpoint": claude_endpoint,
            "prompt": claude_prompt
        },
        "Connecteur_C": {
            "mapping": mapping_example,
            "logs_enabled": enable_logs
        },
        "Slack": {
            "token": slack_token,
            "channel_id": slack_channel,
            "format": slack_format
        }
    }

    st.subheader("Configuration JSON générée")
    st.code(json.dumps(flux_config, indent=4))
    st.success("Flux prêt à utiliser ou à intégrer dans ton pipeline !")
