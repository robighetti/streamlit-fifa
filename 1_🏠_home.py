import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
  df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
  df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
  df_data = df_data[df_data["Value(£)"] > 0]
  df_data = df_data.sort_values(by="Overall", ascending=False)
  st.session_state["data"] = df_data

st.markdown("## Fifa 2025 OFFICIAL DATASET! ⚽️")
st.sidebar.markdown("Desenvolvido por [Rodrigo Bighetti](https://stack2u.net)")

btn = st.button("Acessar os dados da Kaggle")

if btn:
  webbrowser.open_new_tab("https://www.kaggle.com/datasets/joebeachcapital/fifa-players")
  
st.markdown(
  """
  The datasets provided include the players data for the Career Mode from FIFA 15 to FIFA 23.

  The data allows multiple comparisons for the same players across the last 8 version of the videogame.

  Some ideas of possible analysis:

  Historical comparison between Messi and Ronaldo (what skill attributes changed the most during time – compared to real-life stats);
  Ideal budget to create a competitive team (at the level of top n teams in Europe) and at which point the budget does not allow to buy significantly better players for the 11-men lineup. An extra is the same comparison with the Potential attribute for the lineup instead of the Overall attribute;
  Sample analysis of top n% players (e.g. top 5% of the player) to see if some important attributes as Agility or BallControl or Strength have been popular or not acroos the FIFA versions. An example would be seeing that the top 5% players of FIFA 20 are faster (higher Acceleration and Agility) compared to FIFA 15. The trend of attributes is also an important indication of how some attributes are necessary for players to win games (a version with more top 5% players with high BallControl stats would indicate that the game is more focused on the technique rather than the physicial aspect).
  """
)

