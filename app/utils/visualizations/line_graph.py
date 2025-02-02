# Function to produce a json file for web to display a Plotly line graph that
# maps the history of a specific student's submission scores

# Imports
import plotly.graph_objects as go


def line_graph(score_history, name):
    """
    Function produces a line graph of a student's squad scores over time

        Input: A list containing the history of the students scores, in
        chronological order. And student's name.

        Output: Plotly JSON for web to display using plotly.js on the
        parent dashboard
    """

    # If no scores are inputted, should not pass through API, but just in case
    if len(score_history) == 0:
        return "No Submissions for This User"

    # If no name is inputted, should not pass through API, but just in case
    if name == "":
        return "No User Specified"

    # Check for edge case of default data entered
    if score_history == [1005, 1500, 9000, 789] and name == "Firstname":
        return "Default Data Entered"

    # Plotly line graph to show improvement over time
    fig = go.Figure(
        data=go.Scatter(
            x=[i + 1 for i in range(len(score_history))],
            y=score_history,
            line={
                'width': 7,
                'color': '#EB7E5B'
            },
            mode="lines+markers+text",
            marker={
                'size': 18,
                'color': '#FED23E',
                'symbol': 'star'
            }
        )
    )

    fig.update_layout(
        title={
            "text": f"{name}'s Squad Score Over Time",
            "y": 0.95,
            "x": 0.5,
            "font": {"size": 25, "family": "PT Sans Narrow"},
        },
        plot_bgcolor="#6CEAE6",
    )

    fig.update_traces(hoverinfo="none", hovertemplate=None)

    fig.update_xaxes(
        title_text="Week Number",
        title_font={"size": 20, "family": "PT Sans Narrow"},
        showgrid=False,
        zeroline=False,
        ticks="inside",
        tickvals=[i + 1 for i in range(len(score_history))],
    )

    fig.update_yaxes(
        title_text="Squad Score",
        title_font={"size": 20, "family": "PT Sans Narrow"},
        showticklabels=False,
        showgrid=False,
    )

    # If there is only 1 submission, it will only show a single data point
    # Adds a sentence to the parent to check back when more data is available
    if len(score_history) == 1:
        fig.update_layout(
            annotations=[
                dict(
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=1.15,
                    text="Your child only has one submission so far. Please check back next week to view their progress!",
                    showarrow=False,
                    font=dict(size=18, family="PT Sans Narrow"),
                )
            ]
        ),

    # Return as json for web to use in plotly.js
    return fig.to_json()
