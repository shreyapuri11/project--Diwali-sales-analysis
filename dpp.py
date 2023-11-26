import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

st.set_page_config(
    page_icon="💸",
    page_title="Diwali sales analysis ",
    layout="wide")


df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')


st.title('Diwali Sales Analysis 🪔')

st.write('## Data Summary')
st.write('Shape of the dataset:', df.shape)
st.write(df)


st.write('## Visualizations 📈')


st.write('Select an option from the dropdown below to view the corresponding graph:')


option = st.selectbox('Select an option:', [
    'State-wise Orders','Gender Distribution',
    'Age Group Distribution',
    'State-wise Total Sales/Amount',
    'Marital Status Distribution',
    'Marital Status vs. Amount with Gender Hue',
    'Occupation Distribution',
    'Top 10 Most Sold Products'
])

if option == 'Gender Distribution':
    st.subheader('Gender Distribution')
    st.write('This graph shows the distribution of gender among buyers.')
    plt.figure(figsize=(15, 5)) 
    gender_countplot = sb.countplot(x='Gender', data=df)
    st.pyplot(gender_countplot.get_figure())
    

    st.write('### Conclusion for Gender Distribution')
    st.write(' Female Dominance: The data indicates a higher representation of female buyers compared to males.')
    st.write(' This suggests a significant female presence in the customer base during the Diwali sales period.')

elif option == 'Age Group Distribution':
    st.subheader('Age Group Distribution')
    st.write('This graph shows the distribution of age groups among buyers, with gender as a hue.')
    plt.figure(figsize=(15, 5)) 
    age_group_countplot = sb.countplot(data=df, x='Age Group', hue='Gender')
    st.pyplot(age_group_countplot.get_figure())
    
    st.write('### Conclusion for Age Group Distribution')
    st.write('The majority of buyers belong to the 26-35 age group, particularly females.')
    st.write('This age group is the most active in terms of making purchases.')

elif option == 'State-wise Orders':
    st.subheader('State-wise Orders')
    st.write('This graph displays the total number of orders for each state.')
    state_orders = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False)
    st.bar_chart(state_orders.set_index('State')['Orders'])
    
    
    st.write('### Conclusion for State-wise Orders')
    st.write('Uttar Pradesh, Maharashtra, and Karnataka are the top states in terms of both order quantity and total sales.')
    st.write('These states have a higher market share and contribute significantly to overall sales.')

elif option == 'State-wise Total Sales/Amount':
    st.subheader('State-wise Total Sales/Amount')
    st.write('This graph shows the total sales amount for each state.')
    plt.figure(figsize=(15, 5)) 
    state_sales = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    st.bar_chart(state_sales.set_index('State')['Amount'])
    
    
    st.write('### Conclusion for State-wise Total Sales/Amount')
    st.write('Uttar Pradesh, Maharashtra, and Karnataka are the top states in terms of total sales amount as well.')
    st.write('These states are key contributors to the overall revenue.')

elif option == 'Marital Status Distribution':
    st.subheader('Marital Status Distribution')
    st.write('This graph shows the distribution of marital status among buyers.')
    plt.figure(figsize=(15, 5)) 
    marital_status_countplot = sb.countplot(data=df, x='Marital_Status')
    st.pyplot(marital_status_countplot.get_figure())
    
    
    st.write('### Conclusion for Marital Status Distribution')
    st.write('Most buyers are married, especially women.')
    st.write('Married buyers, particularly married women, make up a substantial portion of the customer base.')

elif option == 'Marital Status vs. Amount with Gender Hue':
    st.subheader('Marital Status vs. Amount with Gender Hue')
    st.write('This graph displays the relationship between marital status, total amount spent, and gender.')
    plt.figure(figsize=(15, 5)) 
    marital_status_vs_amount = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    st.bar_chart(marital_status_vs_amount.set_index('Marital_Status')['Amount'])
    
    
    st.write('### Conclusion for Marital Status vs. Amount with Gender Hue')
    st.write('Married individuals, especially women, tend to spend more on purchases.')

elif option == 'Occupation Distribution':
    st.subheader('Occupation Distribution')
    st.write('This graph shows the distribution of occupations among buyers.')
    plt.figure(figsize=(19, 5))
    occupation_countplot = sb.countplot(data=df, x='Occupation')
    st.pyplot(occupation_countplot.get_figure())
    
  
    st.write('### Conclusion for Occupation Distribution')
    st.write('The top occupations of buyers are in IT, Healthcare, and Aviation sectors.')
    st.write('These sectors have a higher number of buyers, possibly due to higher disposable income.')

elif option == 'Top 10 Most Sold Products':
    st.subheader('Top 10 Most Sold Products')
    st.write('This graph displays the top 10 most sold products.')
    plt.figure(figsize=(15, 5)) 
    top_10_products = df.groupby(['Product_Category'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    st.bar_chart(top_10_products.set_index('Product_Category')['Orders'])
    
    
    st.write('### Conclusion for Top 10 Most Sold Products')
    st.write('The top-selling products have higher order quantities.')
    st.write('Identifying these products can help in optimizing inventory and marketing efforts.')


st.write('---')
st.write('### KEY INSIGHTS 🔑🔍')
conclusion = """
The Diwali sales analysis highlights several key insights:

- Female buyers play a pivotal role, with a notable presence in the customer base.
- The 26-35 age group is the most active, especially among females.
- States like Uttar Pradesh, Maharashtra, and Karnataka are crucial for sales.
- Married individuals, particularly women, form a substantial part of our customer base.
- Top occupations include IT, Healthcare, and Aviation sectors.
- Identifying and prioritizing top-selling products can optimize inventory and marketing efforts.

These findings underscore the importance of tailoring marketing strategies and product offerings to cater to the preferences of female buyers and the dominant age group. 
Focusing on key states, marital status segments, and top occupations can lead to sustained growth and success in future Diwali sales campaigns.
"""


st.write(conclusion)
st.write('------')
st.markdown('### Created by Shreya Puri')