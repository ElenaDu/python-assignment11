#Task 3: Interactive Visualizations with Plotly
import plotly.express as px
import plotly.data as pldata
#Load the Plotly wind dataset
df = pldata.wind(return_type='pandas')

#Print the first and last 10 lines of the DataFrame
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

#Clean the data. Convert the 'strength' column to a float. Use of str.replace() with regex is one way to do this, followed by type conversion.
df['strength'] = df['strength'].astype(str).str.replace(r'[^0-9.]', '', regex=True).astype(float)

#Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
)

#Save and load the HTML file, as wind.html
fig.write_html('wind.html', auto_open = True)