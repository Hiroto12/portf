import base64
import streamlit as st
import plotly.express as px
import os
df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image4.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://media.giphy.com/media/501qrEz3NAqyc/giphy.gif");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: local;
color: white; 
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

.st-h1, .st-h2, .st-h3, .st-h4, .st-h5, .st-h6, .st-figcaption, .st-caption, .st-imgtxt, .st-txt, .st-tt, .st-err, .st-em, .st-lg {{
    color: white;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='color: white;'>Descubra o poder além da planilha</h1>", unsafe_allow_html=True)

# Iniciando a Sidebar
st.sidebar.header("")

# Título de Contato
st.sidebar.markdown("<h2 style='color: white;'>Contato</h2>", unsafe_allow_html=True)

# Exibindo a imagem com dimensões reduzidas
image_path = "imagem5.jpeg"
if os.path.exists(image_path):
    st.sidebar.image(image_path, use_column_width='auto', width=200)  # Ajuste a largura conforme necessário
else:
    st.sidebar.warning(f"Imagem '{image_path}' não encontrada.")

# Texto sobre informações da equipe
st.sidebar.markdown("<p style='color: white;'>Informações da equipe:</p>", unsafe_allow_html=True)
texto = st.markdown("<p style='color: white;'>Informações da equipe:</p>", unsafe_allow_html=True)
# Selectbox com os nomes da equipe
equipe = st.sidebar.selectbox("Escolha um membro da equipe", ["Hiroto", "João Victor"])

# Mostrar a descrição correspondente ao membro da equipe selecionado
if equipe == "Hiroto":
    st.sidebar.markdown("""
    <p style='color: white;'>Formando em Engenharia de Computação pela Unifei - Campus Itabira, conheceu o mundo dos dados a mais de 3 anos em uma Iniciação Científica com o tema de Radar Meteorológico, sendo necessário analisar dados para previsão de chuva em uma base de mais 5TB de dados.</p>
    """, unsafe_allow_html=True)
elif equipe == "João Victor":
    st.sidebar.markdown("""
    <p style='color: white;'>Formando em Engenharia de Computação Pela Unifei- Campus Itabira, possui experiência como desenvolvedor full stack em uma empresa júnior da Universidade. Embora recente no mundo de dados, já virou um expert no desenvolvimento de dashboards, simplificandos dados em visualizações que contam histórias que vão além dos números da planilha.</p>
    """, unsafe_allow_html=True)
# Adicionando GIF e texto de marketing
col1, col2 = st.columns(2)

with col1:
    st.image("https://media.giphy.com/media/HEOQ8abOwAxbHmpmTR/giphy.gif")
with col2:
    st.write("Desenvolvemos dashboards e analisamos dados. Chega de planilhas complicadas e análises demoradas. Transforme seus dados em insights poderosos para sua empresa!")

with st.container():
    propaganda = """
        ### <span style="color:white">**Por que substituir planilhas por dashboards?**</span> 📊
        - **Eficiência Temporal**: De acordo com [Forbes](https://www.forbes.com/), funcionários gastam cerca de **2.5 horas por dia** buscando dados em planilhas. Dashboards centralizam e simplificam esse acesso.
        - **Tomada de Decisão Acelerada**: [Gartner](https://www.gartner.com/) aponta que empresas orientadas a dados tomam decisões **5 vezes mais rápido** do que seus concorrentes.
        - **Visualização Clara**: 65% das pessoas são aprendizes visuais, segundo [Social Science Research Network](https://www.ssrn.com/). Dashboards transformam dados brutos em representações visuais claras e compreensíveis.
        - **Automação de Processos**: Reduza erros manuais e processos redundantes automatizando a coleta e a apresentação dos dados.
        """

    st.markdown(propaganda, unsafe_allow_html=True)


with st.container():
    # Título com destaque
    titulo1 = """
                ### <span style="color:white">**Dashboard turbinados**</span> 
              """
    st.markdown(titulo1, unsafe_allow_html=True)

    # Texto descritivo sobre as capacidades dos dashboards
    st.write("""
        Os dashboards são ferramentas poderosas que transformam dados brutos em visuais impactantes e informações acionáveis.
        Com eles, você pode rapidamente identificar tendências, monitorar metas, e tomar decisões baseadas em dados.
        Ao invés de gastar horas analisando planilhas, um dashboard bem construído oferece insights em questão de segundos.
        """)

    col1, col2 = st.columns(2)
    with col1:
        st.image('imagem1.jpeg')
    with col2:
        st.image('imagem2.jpg')


with st.container():
    with st.container():
        # Título com destaque
        titulo1 = """
                    ### <span style="color:white">**Exemplo de Análise que realizamos**</span> 
                  """
        st.markdown(titulo1, unsafe_allow_html=True)

        # Texto descritivo sobre as capacidades dos dashboards
        st.write("""
            O estudo abaixo foi uma análise que realizamos para entender os dados da pandemia, com foco na relação dos óbitos distribuidos em um período. 
            A análise inclui: entender as regras de negócios que constitui o problema, realizar as devidas limpezas, geração de hipóteses e sua validação com base nos resultados dos dados.
            """)
    # Incorporando o Jupyter notebook usando nbviewer
    link = "https://nbviewer.jupyter.org/github/Hiroto12/S-rie-Temporal-COVID-19-Estudos-/blob/main/An%C3%A1lise%20de%20S%C3%A9rie%20Temporal%20-%20Covid%2019.ipynb"
    st.markdown(f'<iframe src="{link}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)