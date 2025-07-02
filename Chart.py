
import plotly.express as px
import pandas as pd

# Load the analysis data from the sheet
df = q.cells("Dask_Analysis")

# Create a pie chart for the sum of B
fig = px.pie(df, values='B', names='C', 
             title='Proportion of Sum of B by Category C',
             hole=0.3)

# Update the text formatting
fig.update_traces(textinfo='percent+label')

# Show the chart
fig.show()
