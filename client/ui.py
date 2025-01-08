import streamlit as st
import utils

st.set_page_config(layout='centered',page_title="Spam Mail Classification",page_icon=":email:")

st.markdown(
"""
<style> 
.stDeployButton {
    visibility: hidden;
}
#MainMenu {
    visibility: hidden;
}
div.row-widget.stButton{
    text-align: center
}
div.stMarkdown{
    text-align: center
}
</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<h1 style="text-align:center; color:blue">SPAM MAIL CLASSIFICATION</>
""", unsafe_allow_html=True)

st.write('---')

email = st.text_area(label=':blue[****Email****]',value=None,placeholder='Enter the mail here',height=230)

predict = st.button(label=':blue[****Predict****]')

st.write('---')

if predict:
    if email:
       pred,color = utils.predict(email)
       pred = pred.upper()
       st.header(f':{color}[{pred}]')
      