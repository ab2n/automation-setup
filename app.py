import streamlit as st
import json

st.set_page_config(page_title="Préparateur Claude → Slack", layout="wide")
st.title("Préparateur d'automatisation Claude API → Slack")

st.markdown("""
Remplis les champs ci-dessous pour générer ton flux complet.
""")

# --- Section Claude API ---
st.header("Claude API")
claude_model = st.selectbox("Choisir le modèle Claude", ["claude-1", "claude-2", "claude-instant"])
claude_api_key = st.text_input("API Key Claude", placeholder="sk-123abc456def")
claude_endpoint = st.text_input("Endpoint URL Claude", value="https://api.claude.ai/v1/generate")
claude_prompt = st.text_area("Prompt à envoyer à Claude", placeholder="Résumé du rapport...")

# --- Section Slack ---
st.header("Slack")
slack_token = st.text_input("Token OAuth Slack", placeholder="xoxb-9876543210-abcdef")
slack_channel = st.text_input("Channel ID Slack", placeholder="C0123456789")
slack_format = st.selectbox("Format du message Slack", ["Texte simple", "Blocks (JSON)"])

# --- Section Mapping / Connecteur des connecteurs ---
st.header("Connecteur des connecteurs (C)")
mapping_example = st.text_input(
    "Mapping Claude → Slack",
    placeholder='text → blocks[0].text'
)
enable_logs = st.checkbox("Activer logs / suivi erreurs", value=True)

# --- Générer la configuration ---
if st.button("Générer flux JSON"):
    flux_config = {
        "Claude_API": {
            "model": claude_model,
            "api_key": claude_api_key,
            "endpoint": claude_endpoint,
            "prompt": claude_prompt
        },
        "Slack": {
            "token": slack_token,
            "channel_id": slack_channel,
            "format": slack_format
        },
        "Connecteur_C": {
            "mapping": mapping_example,
            "logs_enabled": enable_logs
        }
    }
    
    st.subheader("Configuration JSON générée")
    st.code(json.dumps(flux_config, indent=4))

    st.success("Flux prêt à utiliser ou à intégrer dans ton pipeline d'automatisation !")
