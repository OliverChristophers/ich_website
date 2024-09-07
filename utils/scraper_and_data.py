import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

def scraper_and_data():
    current_dir = os.path.dirname(os.path.abspath(__name__))
    df = pd.read_pickle(os.path.join(current_dir, 'data.pkl'))
    st.markdown("### Scraper and Data")
    i = st.slider('Data Game',1,len(df)+1,step=1,value=1) - 1
    st.write(f'{i+1}')
    l = st.selectbox('Line',sorted([float(i[2:]) for i in df.columns]),index=2)
    fig = plt.figure()
    ax = fig.add_subplot()
    try:
        u = df.loc[i,'3_'+str(l)+'0']['under']
        o = df.loc[i,'3_'+str(l)+'0']['over']
        ax.scatter([50],[1],label=f'Data Game: {i+1}',color='1',s=0.1)
        ax.scatter([50],[1],label=f'Line: {l}',color='1',s=0.1)
        ax.scatter(range(len(o)),o,label='Over',color='0')
        ax.scatter(range(len(u)),u,label='Under',color='0.5')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlabel('i')
        ax.set_ylabel('o_i')
        plt.legend(loc='upper left')
    except:
        plt.cla()
        ax.text(0.5,0.5,'No Data',ha='center',va='center')
        ax.set_xticks([])
        ax.set_yticks([])
    st.pyplot(fig)

    st.markdown("""As our name suggests, we require data that not only covers a vast range of events and markets, but that also covers a vast range of time, across those events and markets, as our strategy requires placing bets on the same event intertemporally. Our hands-on solution to this data issue has been to construct a scraper which can collect all the data we need. This provides us with the freedom to collect as much data as we desire, and the flexibility to collect whatever types of data we desire.

Oddschecker.com is a truly wonderful platform, collecting odds from the most respected bookmakers in the industry and conveniently comparing these, displaying for all markets the most favourable price and the supplying bookmaker. It does not only show the best price, however, but additionally shows all prices from all active bookmakers, meaning a bettor can gain an enhanced understanding of the distribution of prices, and hence the distribution of probability estimates on the market outcome. It also shows price trends, whether odds are moving inwards or outwards, which could in theory be useful for momentum strategies. Oddschecker, thus, has all the information that we could possibly need.

What our scraper does occurs in multiple stages. For an event where we desire data, it first gathers pre-match prices, just as the event begins, from the markets which we have requested. These prices are closing odds at which we place our initial bets. The scraper subsequently regathers odds for the same markets regularly throughout the event, with prespecified frequency. After the event has been completed, the data is structured conveniently in our database, from where we can access it freely. We can thus, across multiple events, analyse how prices move, identify trends and hence specify our trading strategies.

In the sandbox above you can interact with our data. It shows odds $o_i$ for the over and under line on the Total Goals Over/Under market for the $i$ timestamps throughout the selected game. Discontinuities occur when goals are scored, as the probability of scoring over/under a certain number of goals then obviously changes. When goals are not scored, the trend is continuous and monotonic.
""")