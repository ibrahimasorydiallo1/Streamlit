import streamlit as st
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(page_title="Portfolio | Ibrahima Sory DIALLO", page_icon="🚀", layout="wide")

st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

st.logo("assets/img/logo.png", size="large")

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
        
        Passionné par l'impact business de l'IA, j'accompagne les entreprises dans la mutation vers la GenAI : du cadrage stratégique au déploiement technique de solutions à forte valeur ajoutée.

        Mon approche repose sur un équilibre critique : l'excellence technique au service de la rigueur métier. Je ne construis pas seulement des modèles, je bâtis les ponts qui permettent leur mise en production industrielle.

        Ce que j'apporte à vos projets :

        🔹🏗️ Orchestration d'Agents IA : Conception de workflows complexes via LangGraph, permettant une gestion fine de la mémoire et des cycles décisionnels pour des agents véritablement autonomes.

        🔹📚 Architectures RAG Avancées : Mise en place de systèmes de récupération haute précision (Advanced RAG) pour transformer vos données non structurées en un actif stratégique exploitable.

        🔹🛡️ Fiabilité & Observabilité : Monitoring temps réel via LangSmith et évaluation rigoureuse avec DeepEval pour garantir des réponses sûres, précises et sans hallucinations.

        🔹📊 Pilotage & ROI : Analyse de faisabilité technique et optimisation des processus data pour assurer une transformation digitale mesurable et durable.

        Stack Technique : 

        🔹 Langages & Data : Python (Pandas, Scikit-Learn, Seaborn, Matplotlib), SQL.

        🔹 GenAI & LLMops : LangChain, LangGraph, LangSmith, DeepEval.

        🔹 Déploiement : Streamlit, AWS, Snowflake.
        """)
        st.info("📍 Basé à Lyon | Disponible pour stage(4-5 mois) dès le 27 Avril 2026 | Mobilité: Auvergne Rhône-Alpes - Ile de France")

# --- SECTION : EXPERIENCE ---
elif selected == "Experience":
    st.header("Parcours Professionnel 💼", divider="violet")
    
    st.subheader("Ingénieur Data & Cloud (Alternance) | Groupe APICIL")
    st.caption("2023 - 2025 | Lyon | Équipe : 2 personnes (Binôme Ingénieur/Expert)")

    # PROJET 1
    with st.expander("☁️ Projet 1 : Système de Monitoring automatisé des AWS Step Functions", expanded=True):
        st.write("**Rôle :** Lead Développeur Cloud & Supervision")
        st.write("**Technologies :** AWS (Step Functions, Lambda, EventBridge), Python, Terraform, VS Code")
        
        st.markdown("""
        **Étapes du projet :**
        1. **Analyse du besoin** : Identifier les points de rupture des flux de données critiques.
        2. **Conception** : Architecture d'un système de capture d'erreurs via EventBridge.
        3. **Déploiement IaC** : Automatisation de l'infrastructure avec Terraform.
        4. **Validation** : Tests de résilience et tableaux de bord de supervision.
        
        **Ce que j'ai appris :** J'ai renforcé ma capacité à anticiper les pannes dans des architectures distribuées. Ce projet m'a appris l'importance cruciale de l'observabilité pour garantir la continuité de service.
        """)

    # PROJET 2
    with st.expander("❄️ Projet 2 : IHM Streamlit pour la Gouvernance Snowflake"):
        st.write("**Rôle :** Développeur Fullstack Data")
        st.write("**Technologies :** Snowflake, Streamlit, Python, SQL, VS Code")
        
        st.markdown("""
        **Étapes du projet :**
        1. **Audit Data** : Analyse de la structure des tables Snowflake existantes.
        2. **Développement Backend** : Requêtage SQL optimisé via Python.
        3. **Interface Utilisateur** : Création d'une IHM intuitive pour les utilisateurs métiers.
        4. **Sécurisation** : Mise en place de contrôles d'accès et de logs de modification.
        
        **Ce que j'ai appris :** J'ai développé une vision produit en transformant un besoin technique complexe en un outil simple pour le métier. Mon adaptation aux spécificités de Snowflake a été un facteur clé.
        """)

    # PROJET 3
    with st.expander("🛡️ Projet 3 : Qualité de Données & Contrôles AWS Lambda"):
        st.write("**Rôle :** Ingénieur Qualité Data & Automatisation")
        st.write("**Technologies :** AWS Lambda, Python, SQL, Gitlab CI/CD")
        
        st.markdown("""
        **Étapes du projet :**
        1. **Définition des règles** : Établir les seuils de qualité avec les Data Owners.
        2. **Code & Serverless** : Développement de Lambdas Python pour le nettoyage automatique.
        3. **Industrialisation** : Intégration dans la pipeline CI/CD pour des contrôles à chaque déploiement.
        
        **Ce que j'ai appris :** Ce projet a forgé ma rigueur technique. J'ai compris que la donnée n'a de valeur que si elle est fiable, et que l'automatisation est le seul moyen de maintenir cette fiabilité à grande échelle.
        """)
    
    # PROJET 4
    with st.expander("🔐 Projet 4 : Automatisation de la Gouvernance & Masking Policies Snowflake"):
        st.write("**Rôle :** Ingénieur Sécurité Data")
        st.write("**Technologies :** Snowflake, SQL, Python (Snowpark), VS Code")
        
        st.markdown("""
        **Étapes du projet :**
        1. **Audit de confidentialité** : Identification des données sensibles (PII) au sein des tables de production.
        2. **Définition des politiques** : Création de règles de masquage dynamique basées sur les rôles (RBAC).
        3. **Développement de la procédure** : Écriture d'une procédure stockée hybride (SQL/Python) pour automatiser l'application des politiques sur de nouveaux schémas.
        4. **Audit & Log** : Mise en place d'un suivi pour vérifier l'accès aux données masquées.
        
        **Ce que j'ai appris :** J'ai acquis une expertise sur la sécurité granulaire des données. Ce projet m'a appris à concilier les besoins d'analyse des utilisateurs avec les contraintes strictes de confidentialité des données de santé/prévoyance.
        """)

# --- SECTION : EDUCATION ---
elif selected == "Education":
    st.header("Parcours Académique 🎓", divider="red")

    # --- EPSI LYON ---
    with st.container():
        st.subheader("Bachelor 3 Intelligence Artificielle")
        st.markdown("**EPSI Lyon** | 2025 - 2026")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("##### 🎯 Compétences développées")
            st.write("- **Déployer des apps IA** : Intégration ML, NLP et Computer Vision.")
            st.write("- **Valorisation Data** : Extraction d'insights pour modèles performants.")
            st.write("- **Architecture Data** : Optimisation SQL et bases de données pour l'IA.")
        with c2:
            st.markdown("##### 🚀 Vision Projet")
            st.write("- **Pilotage Agile** : Gestion de projets IA en environnement complexe.")
            st.write("- **Certification Focus** : Préparation AWS, Azure DP-900 et Python.")
            st.write("- **Soft Skills** : Communication technique et anglais professionnel.")

    st.write("---")

    # --- ESGI LYON ---
    with st.container():
        st.subheader("Bachelor Architecture des Logiciels")
        st.markdown("**ESGI Lyon** | 2022 - 2025")
        
        c3, c4 = st.columns(2)
        with c3:
            st.markdown("##### 🎯 Compétences développées")
            st.write("- **Conception Logicielle** : Définition de solutions applicatives Java/Node.")
            st.write("- **Développement & Optimisation** : Code responsable et performant.")
            st.write("- **DevOps** : Conteneurisation Docker et administration Linux.")
        with c4:
            st.markdown("##### 🚀 Vision Projet")
            st.write("- **Méthodologie** : Design Thinking et Agilité/Scrum.")
            st.write("- **Qualité Logicielle** : Automatisation des tests via Junit5.")
            st.write("- **Architecture** : Maîtrise des flux de données et stockage MongoDB.")

    st.write("---")

    # --- UNIVERSITÉ GAMAL ABDEL NASSER ---
    with st.container():
        st.subheader("Licence 1 Informatique")
        st.markdown("**Université Gamal Abdel Nasser (Guinée)** | 2021 - 2022")
        
        c5, c6 = st.columns(2)
        with c5:
            st.markdown("##### 🎯 Compétences développées")
            st.write("- **Algorithmique** : Listes, tris et logique de programmation.")
            st.write("- **Bases Théoriques** : Mathématiques discrètes et probabilités.")
            st.write("- **Architecture** : Compréhension du fonctionnement matériel.")
        with c6:
            st.markdown("##### 🚀 Vision Projet")
            st.write("- **Fondations** : Rigueur dans la résolution de problèmes complexes.")
            st.write("- **Adaptation** : Capacité à assimiler des concepts abstraits rapidement.")

# --- SECTION : SKILLS ---
elif selected == "Skills":
    st.header("Expertises & Compétences", divider="orange")

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