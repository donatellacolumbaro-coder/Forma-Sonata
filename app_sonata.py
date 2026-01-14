import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="La Forma Sonata - Infografica",
    page_icon="🎵",
    layout="centered"
)

# Stile personalizzato per emulare il look moderno dell'infografica originale
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        font-weight: bold;
        border: 2px solid #e2e8f0;
    }
    .section-card {
        padding: 1.5rem;
        border-radius: 1rem;
        border-left: 5px solid #6366f1;
        background-color: white;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        margin-bottom: 2rem;
    }
    .detail-card {
        background-color: #f1f5f9;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Inizializzazione dello stato della sessione (per gestire i click dei bottoni)
if 'sezione_attiva' not in st.session_state:
    st.session_state.sezione_attiva = 'Introduzione'

# Header
st.title("🎵 La Forma Sonata")
st.markdown("*L'architettura del dramma musicale classico.*")
st.divider()

# Navigazione (Pulsanti)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Intro"):
        st.session_state.sezione_attiva = 'Introduzione'
with col2:
    if st.button("▶️ Esposizione"):
        st.session_state.sezione_attiva = 'Esposizione'
with col3:
    if st.button("⚡ Sviluppo"):
        st.session_state.sezione_attiva = 'Sviluppo'
with col4:
    if st.button("🔄 Ripresa"):
        st.session_state.sezione_attiva = 'Ripresa'

# Logica dei contenuti
if st.session_state.sezione_attiva == 'Introduzione':
    st.info("### Cos'è la Forma Sonata?")
    st.write("""
        La Forma Sonata è la struttura architettonica più importante della musica strumentale classica. 
        Si basa sulla dialettica tra due temi contrastanti e sul ritorno finale alla tonalità principale.
    """)
    st.markdown("- **Struttura Tripartita**: Esposizione, Sviluppo, Ripresa.")
    st.markdown("- **Dialettica Tonale**: Tensione tra tonica (casa) e dominante (tensione).")

elif st.session_state.sezione_attiva == 'Esposizione':
    st.subheader("1. Esposizione")
    st.write("In questa fase vengono presentati i due temi principali.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Primo Tema (T1)**")
        st.caption("Energico, definisce la tonalità principale.")
        st.markdown("**Ponte Modulante**")
        st.caption("Transizione che crea tensione e cambia tonalità.")
    with c2:
        st.markdown("**Secondo Tema (T2)**")
        st.caption("Più melodico e cantabile, in una nuova tonalità.")
        st.markdown("**Codetta**")
        st.caption("Conclude la sezione, spesso con un ritornello.")

elif st.session_state.sezione_attiva == 'Sviluppo':
    st.warning("### 2. Sviluppo")
    st.write("""
        È la sezione più libera e drammatica. Il compositore frammenta i temi, 
        li porta in tonalità lontane e crea instabilità emotiva.
    """)
    st.markdown("🎯 **Obiettivo**: Elaborazione creativa e massima tensione.")

elif st.session_state.sezione_attiva == 'Ripresa':
    st.success("### 3. Ripresa (e Coda)")
    st.write("""
        La tensione si risolve. Vengono riproposti i temi dell'esposizione, 
        ma questa volta anche il **Secondo Tema appare nella tonalità principale**.
    """)
    st.markdown("✅ **Risoluzione**: Il conflitto tonale è superato.")

# Schema Visivo Finale
st.divider()
st.markdown("### 📊 Schema Sintetico")
st.markdown("""
<div style="display: flex; gap: 10px; text-align: center;">
    <div style="flex: 1; background: #dbeafe; padding: 10px; border-radius: 8px; color: #1e40af;"><b>Esposizione</b><br><small>T1(I) → T2(V)</small></div>
    <div style="flex: 1; background: #f3e8ff; padding: 10px; border-radius: 8px; color: #6b21a8;"><b>Sviluppo</b><br><small>Modulazioni</small></div>
    <div style="flex: 1; background: #d1fae5; padding: 10px; border-radius: 8px; color: #065f46;"><b>Ripresa</b><br><small>T1(I) → T2(I)</small></div>
</div>
""", unsafe_allow_html=True)

st.caption("Guida Didattica Interattiva - Creata con Streamlit")