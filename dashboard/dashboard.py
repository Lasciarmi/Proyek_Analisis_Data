import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from babel.numbers import format_currency

sns.set(style='dark')
def create_max_season_df(df):
  mappings = {
    1: "musim semi",
    2: "musim panas",
    3: "musim gugur",
    4: "musim dingin"
  }

  max_season_df = df.groupby("season").cnt.max().sort_values(ascending=False).reset_index()
  max_season_df["season"] = max_season_df["season"].map(mappings)
  return max_season_df.head()

# TITLE
st.title("Proyek Analisis Data")
# END OF TITLE

# HEADER
st.header("Bike Sharing Dataset")
# END HEADER

with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    

# LOADING DATA
day_df = pd.read_csv("../data/day.csv")
# END LOADING DATA
# SHOW DATA GROUP BY SEASON
st.markdown("Jumlah penyewaan sepeda yang dikelompokan oleh season")
max_season_df = create_max_season_df(day_df)
# END SHOW DATA GROUP BY SEASON

# SHOW BARCHART
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="cnt", y="season", data=max_season_df, palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Highest Bicycle Rental Demand Season", loc="center", fontsize=15)
ax.tick_params(axis ='y', labelsize=12)

st.pyplot(fig)
# END SHOW BARCHART

# LOADING DATA
hour_df = pd.read_csv("../data/hour.csv")
# END LOADING DATA

st.markdown("Perbandingan rata-rata jam peminjaman sepeda yang dilakukan di hari libur dan bukan hari libur")

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))

mean_hr_by_holiday = hour_df.groupby('holiday')['hr'].mean()

sns.barplot(x=mean_hr_by_holiday.index, y=mean_hr_by_holiday.values)

plt.xlabel('Hari Libur (0: Bukan Libur, 1: Libur)')
plt.ylabel('Rata-rata Jam')
plt.title('Perbandingan Rata-rata Jam pada Hari Libur dan Bukan Libur')

st.pyplot(fig)
# st.pyplot(fig)
