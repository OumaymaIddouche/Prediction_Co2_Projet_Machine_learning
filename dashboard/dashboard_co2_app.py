import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Données mises à jour
df = pd.DataFrame({
    "Modèle": [
        "XGBoost",
        "Random Forest",
        "MLP",
        "Decision Tree"
    ],
    "RMSE Test": [
        4.521233,
        6.662166,
        7.477466,
        8.349105
    ],
    "R² Test": [
        0.990785,
        0.979991,
        0.974794,
        0.968575
    ]
})

# Initialisation de l'app
app = dash.Dash(__name__)

# Graphique RMSE
fig = px.bar(
    df,
    x="Modèle",
    y="RMSE Test",
    title="Comparaison des modèles (RMSE Test)",
    text="RMSE Test"
)

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

# Layout
app.layout = html.Div(children=[
    html.H1("Dashboard des Modèles CO₂"),

    dcc.Graph(figure=fig),

    html.H2("Tableau des performances"),

    html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(len(df))
        ])
    ])
])

# Lancement
if __name__ == '__main__':
    app.run(debug=True)
