import dash
from dash import dcc, html, dash_table, Input, Output
import plotly.express as px
import pandas as pd

# Sample data for the graph and table
df = px.data.iris()

# Create a Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    # Printable content - Graph
    html.Div(
        dcc.Graph(
            id="example-graph",
            figure=px.scatter(df, x="sepal_width", y="sepal_length", color="species")
        ),
        className="printable"
    ),

    # Printable content - DataTable
    html.Div(
        dash_table.DataTable(
            id="example-table",
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
            page_size=10,
            style_table={"overflowX": "auto"},
        ),
        className="printable"
    ),

    # Non-printable button
    html.Div([
        html.Button("Save as PDF", id="print-button", n_clicks=0),
    ], className="non-printable"),  # Button will not appear in the printed document
    html.Link(href="/assets/styles.css", rel="stylesheet")
])

# Client-side callback to trigger printing
app.clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks > 0) {
            window.print(); // Trigger browser's print dialog
        }
        return null;
    }
    """,
    Output("print-button", "n_clicks"),  # Dummy output to satisfy callback
    Input("print-button", "n_clicks")
)

if __name__ == '__main__':
    app.run_server(debug=True)