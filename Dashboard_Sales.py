
import streamlit as st
import plotly.express as px
import pandas as pd

df =pd.read_csv("Sales_Store_Processed.csv")
df["Year"]=df["Year"].astype(str)
st.title("Sales_Store_Analysis")


c1,c2,c3= st.columns(3)

with c1:
    st.metric(label="Total Sales in M$", value=(df["Sales"].sum() / 1000000).round(3))
with c2:
    st.metric(label="Total Profit in M$", value=(df["Profit"].sum() / 1000).round(3))
with c3:
    st.metric(label="Avg Discount Percentage Per Year %", value=(15.5), delta="2%")

st.title("Total profit for each Category in each Region")
profit_category_region=pd.pivot_table(df,index="Category",columns="Region",values="Profit",aggfunc="sum")
profit_region=px.imshow(profit_category_region)

st.plotly_chart(profit_region)

st.title("Distribution and outliers of discount")
c1,c2 = st.columns([2,3])
with c1:
    discount_box=px.box(df,x="Discount")
    st.plotly_chart(discount_box)
with c2:
    discount_histo=px.histogram(df,x="Discount")
    st.plotly_chart(discount_histo)
    
st.title("the top 10 profited state")
profited_state=df.groupby("State").sum()["Profit"].sort_values(ascending=False).head(10).reset_index()
state_bar=px.bar(profited_state,x="State",y="Profit")
st.plotly_chart(state_bar)

st.title("Distribution of each category's Profit")
fig = px.pie(df, values='Profit', names='Category', title='Distribution of each category\'s Profit')
st.plotly_chart(fig)
