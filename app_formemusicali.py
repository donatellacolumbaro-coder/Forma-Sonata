import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="Guida Interattiva alle Forme Musicali",
    page_icon="🎼",
    layout="centered"
)

# Stile CSS personalizzato per un look moderno
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        font-weight: bold;
    }
    .diagram-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 20px 0;
    }
    .diagram-box {
        padding: 15px 25px;
        border-radius: 12px;
        color: white;
        font-weight: 800;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar per la navigazione
st.sidebar.title("📚 Menu Forme")
scelta = st.sidebar.radio(
    "Scegli la forma da esplorare:",
    ["Forma Sonata", "Forma Bipartita", "Forma Tripartita", "Rondò"]
)

st.sidebar.divider()
st.sidebar.markdown("""
**Istruzioni:**
1. Seleziona una forma.
2. Esplora le sezioni tramite i tab o i pulsanti.
3. Osserva lo schema visivo in fondo.
""")

# --- CONTENUTI ---

if scelta == "Forma Sonata":
    st.title("🎵 La Forma Sonata")
    st.markdown("*L'architettura del dramma musicale classico.*")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Intro", "▶️ Esposizione", "⚡ Sviluppo", "🔄 Ripresa"])
    
    with tab1:
        st.info("### La struttura più evoluta")
        st.write("Nata nel XVIII secolo, è la base di sinfonie e concerti. Si fonda sul contrasto tra due temi e sulla tensione tra diverse tonalità.")
        st.markdown("""
        - **Dinamismo**: La musica non è statica, ma evolve come un racconto.
        - **Dialettica**: Il tema 'maschile' (ritmico) incontra quello 'femminile' (melodico).
        """)

    with tab2:
        st.subheader("1. Esposizione")
        st.write("Vengono presentati i protagonisti del brano.")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Tema 1 (T1)**")
            st.caption("Tonalità di Tonica (I). Spesso ritmico e deciso.")
        with col2:
            st.markdown("**Tema 2 (T2)**")
            st.caption("Tonalità di Dominante (V). Più dolce e cantabile.")
        st.markdown("---")
        st.write("**Ponte Modulante**: Il corridoio musicale che ci porta da T1 a T2 cambiando tonalità.")

    with tab3:
        st.subheader("2. Sviluppo")
        st.warning("Qui il compositore 'gioca' con i temi precedenti.")
        st.write("I frammenti dei temi vengono mescolati, portati in tonalità lontane e trasformati. È il momento di massima tensione emotiva.")

    with tab4:
        st.subheader("3. Ripresa")
        st.success("Il ritorno alla stabilità.")
        st.write("Si riascoltano T1 e T2, ma con una grande differenza: ora **entrambi sono nella tonalità di Tonica**. Il conflitto è risolto.")

    # Schema Sonata
    st.markdown("""
    <div class="diagram-container">
        <div class="diagram-box" style="background-color: #3b82f6;">ESPOSIZIONE</div>
        <div class="diagram-box" style="background-color: #a855f7;">SVILUPPO</div>
        <div class="diagram-box" style="background-color: #10b981;">RIPRESA</div>
    </div>
    """, unsafe_allow_html=True)

elif scelta == "Forma Bipartita":
    st.title("🌓 Forma Bipartita")
    st.markdown("*Struttura binaria tipica del Barocco (A - B).*")
    
    st.write("Comune nelle danze (Allemanda, Corrente, ecc.). Entrambe le sezioni vengono solitamente ripetute.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Parte A")
        st.write("Inizia in Tonica e finisce in Dominante.")
    with c2:
        st.markdown("### Parte B")
        st.write("Inizia in Dominante e torna alla Tonica.")
    
    st.markdown("""
    <div class="diagram-container">
        <div class="diagram-box" style="background-color: #60a5fa; border: 2px solid #2563eb;">A</div>
        <div class="diagram-box" style="background-color: #f87171; border: 2px solid #dc2626;">B</div>
    </div>
    """, unsafe_allow_html=True)

elif scelta == "Forma Tripartita":
    st.title("🥪 Forma Tripartita")
    st.markdown("*La forma a contrasto (A - B - A).*")
    
    st.write("Molto usata nelle Arie dell'opera e nei Minuetti. La sezione centrale (B) offre un contrasto netto rispetto ad A.")
    
    st.markdown("""
    - **A**: Esposizione dell'idea principale.
    - **B**: Episodio centrale (spesso in una tonalità diversa o con carattere opposto).
    - **A**: Ripetizione (a volte variata) della prima parte.
    """)

    st.markdown("""
    <div class="diagram-container">
        <div class="diagram-box" style="background-color: #fbbf24; color: black;">A</div>
        <div class="diagram-box" style="background-color: #f472b6; color: black;">B</div>
        <div class="diagram-box" style="background-color: #fbbf24; color: black;">A</div>
    </div>
    """, unsafe_allow_html=True)

elif scelta == "Rondò":
    st.title("🎡 Il Rondò")
    st.markdown("*Il tema circolare (A - B - A - C - A).*")
    
    st.write("Si basa su un tema principale (Ritorno o Refrain) che si alterna a vari episodi contrastanti.")
    
    st.markdown("### Caratteristiche:")
    st.markdown("- **Refrain (A)**: Orecchiabile, allegro e torna sempre uguale.")
    st.markdown("- **Episodi (B, C, ...)**: Divagazioni musicali che rendono il brano vario.")

    st.markdown("""
    <div class="diagram-container">
        <div class="diagram-box" style="background-color: #ef4444;">A</div>
        <div class="diagram-box" style="background-color: #94a3b8;">B</div>
        <div class="diagram-box" style="background-color: #ef4444;">A</div>
        <div class="diagram-box" style="background-color: #94a3b8;">C</div>
        <div class="diagram-box" style="background-color: #ef4444;">A</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Guida alle Forme Musicali | Creata con Streamlit")