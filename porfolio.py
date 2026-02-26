import streamlit as st
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mon CV", page_icon="📍", layout="wide")

# Sidebar pour Contacts et Logiciels
st.sidebar.header("📞 **Contacts**")
st.sidebar.markdown("""
**Adresse**  
Mbour Sérère Kao



**Email**  
[dioufbirane@gmail.com]""")

st.sidebar.header("💻 **Logiciels maîtrisés**")
logiciels = [
    "QGIS / ArcGIS",
    "AutoCAD", 
    "Python",
    "Pix4D",
    "Excel",
    "PowerPoint",
    "Erdas"
]
for logiciel in logiciels:
    st.sidebar.markdown(f"• **{logiciel}**")

st.sidebar.markdown("---")
st.sidebar.markdown("*Géomaticien - L2 en cours*")

# Main content
st.title("📋 **Curriculum Vitae**")
st.markdown("**Birane Diouf** - Géomaticien")

## Compétences
st.header("🎯 **Compétences**")
competences = [
    "Maîtrise des techniques de levés topographiques",
    "Conception et mise en page de cartes thématiques de qualité professionnelle",
    "Utilisation des instruments : Niveau, Station totale, Drone, GPS différenciel",
    "Géo-référencement",
    "Mettre en place une base de données",
    "Traitement d'image avec Agisoft et PIX4DMapper"
    
]

for comp in competences:
    st.markdown(f"• **{comp}**")

## Expériences Professionnelles
st.header("💼 **Expériences Professionnelles**")

st.subheader("**Juin - Septembre 2025**")
st.markdown("**Levée topographique**")
st.markdown("- Traitement de données spatiale")


## Formation
st.header("🎓 **Formation**")

st.markdown("""
**2024 - 2025**  
**Centre d'entrepreneuriat et de développement technique (CEDT) le G15**  
*Licence 1 en Géomatique *

**2025 - 2026**  
**Centre d'entrepreneuriat et de développement technique (CEDT) le G15**  
*Licence 2 en Géomatique(Formation en cours)*

**2023 - 2024**  
 *Baccalauréat*
""")







