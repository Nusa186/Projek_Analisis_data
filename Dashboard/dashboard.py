import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bike Sharing Analysis Dashboard",
    page_icon=":bike:",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title('Analisis Data Peminjam Sepeda')

url = 'https://raw.githubusercontent.com/Nusa186/Projek_Analisis_data/main/Dashboard/day.csv'

df = pd.read_csv(url)
df['dteday'] = pd.to_datetime(df['dteday'])

tabs = st.tabs(["Tren Peminjaman Musim Semi 2011", "Tren Peminjaman Pengguna Terdaftar Q1 2012", "Tren Peminjaman Penguna Casual dan Terdaftar"])


with tabs[0]:

    df_spring_2011 = df[(df['yr'] == 0) & (df['mnth'].isin([3, 4, 5]))]

    st.subheader("Tren Peminjaman Sepeda Selama Musim Semi 2011")

    st.line_chart(df_spring_2011.set_index('dteday')['cnt'])

    st.write('''- Peminjaman sepeda pada musim semi 2011 tetap meningkat 
             sampai akhir musim. Meskipun terdapat penurunan di beberapa titik.''')
    st.write('''- Musim semi 2011 terjadi peningkatan jumlah peminjaman sepeda 
             yang signifikan, terutama seiring dengan berakhirnya musim. Tren peningkatan 
             bisa jadi disebabkan oleh cuaca yang lebih hangat dan stabil. Selain itu, mungkin 
             karena biasanya pada musim semi terdapat berbagai festival daerah dan libur panjang.''')
    

with tabs[1]: 

    q1_2012 = df[(df['yr'] == 1) & (df['mnth'].isin([1, 2, 3]))]

    st.subheader("Tren Peminjaman Sepeda oleh Pengguna Terdaftar pada Q1 2012")

    st.line_chart(q1_2012.set_index('dteday')['registered'], color='#FF0000')

    st.write('''- Untuk peminjaman sepeda oleh peminjam yang terdaftar 
             pada kuartal 1, hasil yang didapatkan kurang stabil, banyak titik yang 
             fluktuatif. Penurunan ini mungkin disebabkan oleh musim yang kurang bersahabat.''')
    st.write('''- Kuartal 1 2012 ini memperlihatkan hasil yang fluktuatif.Hal ini kemunkinan 
             disebabkan oleh cuaca buruk dan perpindahan musim dari musim dingin ke musim semi.''')
    
with tabs[2]:
    df_2011 = df[(df['yr'] == 0)]
    casual = df_2011.groupby('dteday')['casual'].sum()
    registered = df_2011.groupby('dteday')['registered'].sum()
    peminjaman = pd.DataFrame({'Casual': casual, 'Registered': registered})
    st.line_chart(peminjaman)

    st.write('''- Sepanjang tahun 2011 peminjam yang terdaftar meningkat, pada puncaknya yaitu pertengahan tahun.''')
    st.write('''- Sedangkan untuk peminjam casual hampir memiliki pola yang sama dengan terdaftar, 
             tapi tidak memiliki peningkatan yang signifikan''')
    st.write('''- Terdapat Perbedaan yang signifikan antara peminjam casual dan terdaftar. 
             Dimana peminjam terdaftar memiliki jumlah hampir 5 kali lipat dari peminjam casual''')