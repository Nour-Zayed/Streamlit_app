import streamlit as st
import time
st.header("shapes calculations")

st.sidebar.title('Configrations')
with st.sidebar:

     shape=st.selectbox("Choose shape:",{"Circle","Rectangle"})


if shape=='Circle':
    redius =st.number_input('Redius:',min_value=0,max_value=100,step=1)
    area=redius * redius * 3.14
    perimeter= 2 * 3.14*redius
    
if shape=='Rectangle': 
    width=st.number_input('width', 0., step=0.1)
    height=st.number_input('height', 0.,step=0.1)
    area=width *height
    perimeter = 2 * (width+height)   


compute_btn =st.button("Compute Area and Perimeter")
if compute_btn:
    with st.spinner('Computing.....'):
      time.sleep  (1)
      st.write ("Area=",area)
      st.write ("Perimeter = ",perimeter)