"""Steamlit to create a dummy webpage"""
import streamlit as st


hello_text = st.write("Hello, This is the first webpage I have created!!!")
#print("Hello Abhay")

st.title("This is App title")
st.markdown("This is the Markdown")
st.header("This is the App Header")
st.subheader("This is the App Subheader")
st.caption("This is the App Caption")
st.code("x=2021")
st.latex(r'''
a + a r^1 + a r^2 + a r^3 ''')

st.header("")
st.header("Buddha:")
st.video("/workspaces/-machine_learning/resource_folder/\
Buddha Purnima _ Gautam Buddha _ Gautam Buddha Status _ \
Buddha pournima _ Historic India _ #Shorts.mp4")

st.header("")
st.header("Abhay:")
st.image("/workspaces/-machine_learning/resource_folder/Abhay_60Kb.jpeg")


#st.header("Enjoying")

st.header("")
#st.markdown("Pick Your Options:")
st.write("Pick your options:")
option = st.radio("",["Enjoying","Not Enjoying"])

#st.write("Entered Option: " + option)

st.header("")
st.markdown("Select Preferred Food Options")
st.checkbox("Veg")
st.checkbox("Chienese Veg")

st.selectbox("Pick up relationship",["Partner","Friend"])
st.multiselect("Pick the day on which you would be visiting",["Sunday", "Saturday", "Friday"])


