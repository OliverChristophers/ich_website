import streamlit as st
import os

def who_are_we():
    current_dir = os.path.dirname(os.path.abspath(__name__))
    sl, left_co, sm, right_co,sr = st.columns([1, 8, 4, 8, 1])
    with left_co:
        st.image(os.path.join(current_dir, "elliot.jpg"),width=194)
        st.markdown('### Elliot Christophers\n- Co-founder, CFO\n- MSc Finance, Stockholm School of Economics\n- Responsible for risk-management\n- [LinkedIn](https://www.linkedin.com/in/elliot-christophers/)\n- elliotchristophers@gmail.com')
        
    with right_co:
        st.image(os.path.join(current_dir, "oliver.jpg"),width=200)
        st.markdown('### Oliver Christophers\n- Co-founder, CTO\n- BSc Computer Science, Uppsala University\n- Responsible for automation\n- [LinkedIn](https://www.linkedin.com/in/oliver-christophers-544738309/)\n- oliverchristophers@gmail.com')

    st.markdown("""We are two brothers who have grown up in Uppsala, Sweden. We share common passions in sport, technology, economics and mathematical modelling, and operate at their intersection with Intertemporal Crystal Hedging. We are quite different personality-wise, which allows us to create a strong complementary working relationship. Although we have the above primary responsibilities, we coordinate and cooperate extensively.""")