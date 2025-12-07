import sys
import os

# Resolve ROOT_DIR correctly even when Streamlit changes working dir
CURRENT_FILE = os.path.abspath(__file__)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(CURRENT_FILE), ".."))

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

#print("ROOT_DIR:", ROOT_DIR)
#print("sys.path:", sys.path)


import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Anime Recommender",layout='wide')

# storing recommendation pipeline in cache
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences eg: Light hearted anime with school settings")
if query :
    with st.spinner("Fetching Recommendations for you...."):
        response=pipeline.recommend(query)
        st.markdown("### Recommendations #####")
        st.write(response)
