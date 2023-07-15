import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

# Define sample categories and values 
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 20, 15, 25]

# Matplotlib - Bar chart with customized style
plt.figure(figsize=(10, 6))
colors = sns.color_palette('pastel')
plt.bar(categories, values, color=colors)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()


# Seaborn - Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='x_values', y='y_values', data=data, scatter_kws={'s': 80}, line_kws={'color': 'red', 'linewidth': 2})
plt.xlabel('X Values', fontsize=12)
plt.ylabel('Y Values', fontsize=12)
plt.title('Scatter Plot with Regression Line', fontsize=16, fontweight='bold')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# Plotly - Interactive Line chart with enhanced layout
fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines', line=dict(color='blue')))
fig.update_layout(
    title='Line Chart',
    xaxis=dict(title='X Values', tickfont=dict(size=10)),
    yaxis=dict(title='Y Values', tickfont=dict(size=10)),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=12)
)
fig.show()

# Plotly - Interactive Choropleth Map with customized color scale
fig = px.choropleth(
    locations=locations,
    locationmode='country names',
    z=values,
    color_continuous_scale='viridis',
    range_color=(0, max(values)),
    labels={'z': 'Values'},
    title='Choropleth Map',
    hover_name='Country',
    projection='natural earth'
)
fig.update_layout(
    coloraxis_colorbar=dict(
        title='Scale',
        ticks='outside',
        tickvals=[0, 0.5 * max(values), max(values)],
        ticktext=['Low', 'Medium', 'High'],
        len=0.5,
        thickness=15,
        yanchor='middle'
    ),
    font=dict(size=12)
)
fig.show()
