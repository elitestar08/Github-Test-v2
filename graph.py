import pandas as pd
import plotly.express as px

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22]}

df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(df, x='Name', y='Age', title='Age of People')
fig.show()
