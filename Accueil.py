import streamlit as st
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(page_title="Portfolio | Ibrahima Sory DIALLO", page_icon="🚀", layout="wide")

st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

st.logo("assets\img\logo.png", size="large")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #99ffaf , #10c532); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["About", "Experience", "Education", "Skills", "Projects", "Certifications", "Contact"],
        icons=["person", "briefcase", "mortarboard", "tools", "code-slash", "patch-check", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# --- SECTION : ABOUT ---
if selected == "About":
    st.header("Qui suis-je ? 🤔", divider="rainbow")
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.image("assets/img/profile_photo.jpg", width=280)
    
    with col2:
        st.subheader("Ibrahima Sory DIALLO")
        st.markdown(f"""
        🚀 **Data Scientist & AI Project Manager**
        
        Passionné par l'impact business de l'IA, j'ambitionne d'accompagner les entreprises dans le cadrage stratégique et le déploiement technique de solutions GenAI à forte valeur ajoutée.  
        Mon approche combine une expertise technique et une rigueur méthodologique pour assurer le lien critique entre vos besoins métiers et la mise en production.  
        Ce que j'apporte à vos projets :      

        🏗️ 𝐂𝐨𝐧𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐝'𝐚𝐠𝐞𝐧𝐭𝐬 IA: Orchestration de workflows via LangGraph pour une gestion fine de la mémoire et des flux décisionnels.  

        📚 𝐒𝐲𝐬𝐭𝐞̀𝐦𝐞𝐬 𝐑𝐀𝐆 𝐀𝐯𝐚𝐧𝐜és: Mise en place d'architectures de récupération précises pour valoriser vos documents internes.  

        🛡️ 𝐅𝐢𝐚𝐛𝐢𝐥𝐢𝐭é & 𝐄́𝐯𝐚𝐥𝐮𝐚𝐭𝐢𝐨𝐧 : Monitoring via LangSmith et tests rigoureux avec DeepEval pour garantir des systèmes sûrs et performants.  

        📊 𝐏𝐢𝐥𝐨𝐭𝐚𝐠𝐞 & 𝐎𝐩𝐭𝐢𝐦𝐢𝐬𝐚𝐭𝐢𝐨𝐧 : Analyse de faisabilité, gestion du ROI et amélioration continue des processus data.  

        𝐒𝐭𝐚𝐜𝐤 𝐓𝐞𝐜𝐡𝐧𝐢𝐪𝐮𝐞 : Python (Scikit-Learn, Pandas, Seaborn, Numpy, Matplotlib, etc...) | SQL  LangChain/LangGraph | LangSmith & DeepEval | Streamlit. \n
        💡 **Mon ambition :** Allier rigueur technique et leadership pour mener des projets de transformation digitale innovants.
        """)
        st.info("📍 Basé à Lyon | Disponible pour stage(4-5 mois) dès le 27 Avril 2026 | Mobilité: Lyon et périphérie")

# --- SECTION : EXPERIENCE ---
elif selected == "Experience":
    st.header("Expériences Professionnelles 💼", divider="violet")
    
    st.subheader("Ingénieur Data & Cloud (Alternance) | Groupe APICIL")
    st.caption("2023 - 2025 | Lyon")
    st.markdown("""
    - **Monitoring Cloud :** Mise en place d'un système de supervision automatisée des *AWS Step Functions*.
    - **Développement IHM :** Création d'une interface **Streamlit** pour la gouvernance des tables dans **Snowflake**.
    - **Qualité de Données :** Déploiement de contrôles automatisés via *AWS Lambda*.
    """)

# --- SECTION : EDUCATION ---
elif selected == "Education":
    st.header("Parcours Académique & Compétences 🎓", divider="red")
    
    # --- EPSI LYON ---
    st.subheader("Bachelor 3 Intelligence Artificielle")
    st.markdown("**EPSI Lyon** | 2025 - 2026")
    
    col_epsi1, col_epsi2 = st.columns(2)
    with col_epsi1:
        st.markdown("""
        **Axes de formation :**
        - 🤖 **IA & Deep Learning** : NLP, Computer Vision.
        - 📊 **Valorisation de données** : Insights & modèles.
        - 🗄️ **Architecture Data** : SQL & Python.
        """)
    with col_epsi2:
        st.markdown("""
        **Vision Projet :**
        - 🚀 **Agilité & IA** : Pilotage de projets Data.
        - 📜 **Certifications** : AWS, Azure DP-900, Python PCED.
        - 🌍 **Transversales** : Soft Skills & English.
        """)
    
    with st.expander("Détails des objectifs EPSI"):
        st.write("""
        - Développer et déployer des applications basées sur l’IA.
        - Concevoir et optimiser des bases de données pour l’IA.
        - Piloter des projets IA dans un environnement agile.
        """)

    st.write("---") 

    # --- ESGI LYON ---
    st.subheader("Bachelor Architecture des Logiciels")
    st.markdown("**ESGI Lyon** | 2022 - 2025")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Backend & Algo**")
        st.code("Java (POO, Streams)\nAlgorithmique\nNodeJS", language="text")
    with c2:
        st.markdown("**DevOps & Infra**")
        st.code("Docker\nLinux\nMongoDB\nJunit5", language="text")
    with c3:
        st.markdown("**Front & Soft**")
        st.code("React\nDesign Thinking\nAgile/Scrum", language="text")

    st.markdown("##### 🎯 Compétences développées (ESGI)")
    st.info("""
    - **Définir et concevoir** des solutions logicielles et applicatives.
    - **Conduire** un projet informatique responsable.
    - **Optimiser** des solutions existantes (Performance & Sécurité).
    """)

    st.write("---")

    # --- UNIVERSITÉ GAMAL ABDEL NASSER ---
    st.subheader("Licence 1 Informatique")
    st.markdown("**Université Gamal Abdel Nasser (Guinée)** | 2021 - 2022")
    st.write("Fondamentaux : Algorithmique, Mathématiques discrètes, Architecture des ordinateurs.")

# --- SECTION : SKILLS ---
elif selected == "Skills":
    st.header("Expertises & Compétences 🛠️", divider="orange")

    # Top Bar : Tes 3 piliers de Soft Skills (comme demandé dans tes instructions)
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric("Soft Skill", "Leadership", "Gestion d'équipe")
    col_s2.metric("Soft Skill", "Adaptation", "Proactivité")
    col_s3.metric("Soft Skill", "Autonomie", "Rigueur")

    st.write("---")

    # Organisation par Onglets pour une lecture fluide
    tab_ia, tab_cloud, tab_mgmt, tab_dev = st.tabs([
        "🤖 IA & RAG Expert", 
        "☁️ Cloud & Infrastructure", 
        "📊 Management & Stratégie", 
        "💻 Engineering & Data"
    ])

    with tab_ia:
        st.subheader("RAG & Agents IA")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Frameworks & Écosystème :**")
            st.write("- LangChain, LangGraph, LangSmith")
            st.write("- Hugging Face, LLaMA, Ollama, Groq")
            st.write("- Tavily, Pydantic, Protocole MCP")
        with c2:
            st.markdown("**Spécialisations :**")
            st.write("- Retrieval-Augmented Generation (RAG)")
            st.write("- Agentic AI & Prompt Engineering")
            st.write("- Apprentissage Automatique (ML) & Data Science")
        

    with tab_cloud:
        st.subheader("Cloud, DevOps & Data Platforms")
        c3, c4 = st.columns(2)
        with c3:
            st.markdown("**Fournisseurs & Outils :**")
            st.write("- **AWS Expert** (S3, Lambda, Step Functions)")
            st.write("- **Snowflake** (Cloud Data Platform)")
            st.write("- Terraform (Infrastructure as Code)")
            st.write("- Microsoft Azure & Google Cloud Platform")
        with c4:
            st.markdown("**DevOps & Industrialisation :**")
            st.write("- GitLab CI/CD, Git")
            st.write("- Docker, Linux, Ingénierie des réseaux")
            st.write("- MuleSoft Anypoint Platform, Salesforce")
        

    with tab_mgmt:
        st.subheader("Pilotage de Projets IA & Excellence Opérationnelle")
        c5, c6 = st.columns(2)
        with c5:
            st.markdown("**Méthodologies :**")
            st.write("- Lean Six Sigma (Expertise Process)")
            st.write("- Gestion de projets IA & Stratégie IT")
            st.write("- Agilité & Scrum")
        with c6:
            st.markdown("**Business Intelligence :**")
            st.write("- Planification, budgétisation et prévision")
            st.write("- Prise de décision & Analyse analytique")
            st.write("- Supports de formation & Résolution de problèmes")

    with tab_dev:
        st.subheader("Développement & Manipulation de Données")
        c7, c8 = st.columns(2)
        with c7:
            st.markdown("**Langages :**")
            st.write("- **Python** (Expertise Data/IA)")
            st.write("- SQL, PostgreSQL")
            st.write("- Java (POO), JavaScript")
        with c8:
            st.markdown("**Data Engineering :**")
            st.write("- Extract, Transform, Load (ETL)")
            st.write("- Big Data & MongoDB")
            st.write("- Analyse des données & Qualité")

# --- SECTION : PROJECTS ---
elif selected == "Projects":
    st.header("Quelques projets 🚀", divider="blue")

    st.link_button("Voir mon GitHub", "https://github.com/ibrahimasorydiallo1", type='primary')
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.write("### Smart Bakery Intelligence")
        st.write("Système multi-agent pour l'optimisation d'une boulangerie (Forecasting & Stock).")
        st.link_button("Voir la publication", "https://app.readytensor.ai/publications/smart-bakery-intelligence-system-multi-agent-bakery-USJByhsoBYdF")

    with col_p2:
        st.write("### RAG-Based AI Assistant")
        st.write("Assistant intelligent utilisant la génération augmentée par récupération.")
        st.link_button("Voir la publication", "https://app.readytensor.ai/publications/rag-based-ai-assistant-v45MzYqthSxM")

    col_q1, col_q2 = st.columns(2)

    with col_q1:
        st.write("### Housing price prediction")
        st.write("Système de prédiction des prix de l'immobilier.")
        st.link_button("Voir les détails", "https://github.com/ibrahimasorydiallo1/housing-price-predictor")

    with col_q2:
        st.write("### Autre portfolio personnel")
        st.write("Un projet de portfolio personnel développé en HTML, CSS et JavaScript pour présenter mes compétences et expériences.")
        st.link_button("Voir la publication", "https://isd.ydiallo.com/")

# --- SECTION : CERTIFICATIONS ---
elif selected == "Certifications":
    st.header("Certifications & Distinctions 🏆", divider="green")
    
    # Création de 3 catégories pour mieux structurer
    tab1, tab2, tab3 = st.tabs(["🤖 Intelligence Artificielle", "☁️ Cloud & Data", "📈 Gestion & Langues"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Expertises IA")
            st.success("**RAG Systems Expert**")
            st.success("**Agentic AI Builder**")
            st.warning("**AWS Certified AI Practitioner**")
        with col2:
            st.image("assets/fichiers/15449.jpg", use_container_width=True)
            st.image("assets/fichiers/master_agentic.png", caption="Certification Agentic AI", width=250)
            
    with tab2:
        col3, col4 = st.columns(2)
        with col3:
            st.markdown("##### Cloud & Infrastructure")
            st.info("**AWS Cloud Quest: Cloud Practitioner**")
            st.warning("**Google Cloud Digital Leader**")
            st.warning("**Azure Data Fundamentals (DP-900)**")
            st.warning("**Certified Entry-Level Data Analyst with Python**")
        with col4:
            # On regroupe les images dans un expander pour ne pas encombrer
            with st.expander("Voir les certificats Cloud", expanded=True):
                st.image("assets/fichiers/aws_certif.png", use_container_width=True)

    with tab3:
        col5, col6 = st.columns(2)
        with col5:
            st.markdown("##### Management & Langues")
            st.success("**TOEIC : 845/990** (Niveau Courant)")
            st.success("**CPMAI** - Project Management Institute")
            st.success("**Lean and Six Sigma**")
        with col6:
            with st.expander("Voir TOEIC & Management", expanded=True):
                st.image("assets/fichiers/toeic.png", use_container_width=True)
                st.image("assets/fichiers/gestionIA.png", use_container_width=True)
                st.image("assets/fichiers/certif.png", use_container_width=True)

# --- SECTION : CONTACT ---
elif selected == "Contact":
    st.header("Me contacter 📫", divider="gray")
    
    st.write("N'hésitez pas à me solliciter pour discuter de projets Data, Cloud ou IA !")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📧 Email")
        st.write("isddiallopro@gmail.com")
        st.link_button("Envoyer un mail", "mailto:isddiallopro@gmail.com")
        
    with col2:
        st.markdown("#### 🔗 LinkedIn")
        st.write("Retrouvez-moi sur mon réseau professionnel.")
        st.link_button("Voir mon profil", "https://www.linkedin.com/in/ibrahima-sory-diallo-isd/")