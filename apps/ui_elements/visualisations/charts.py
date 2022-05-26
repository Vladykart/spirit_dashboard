import altair as alt


def get_chart(data, title=None, x_axis=None, y_axis=None):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title=title)
        .mark_bar()
        .encode(
            x='monthdate(date):T',
            y='uniqueEvents:Q',
            color='name',
            strokeDash='name',
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x='monthdate(date):T',
            y='uniqueEvents:Q',
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip('date', title=x_axis),
                alt.Tooltip('uniqueEvents', title=y_axis),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()
