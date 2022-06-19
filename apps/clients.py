import datetime

import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
from data.get_data import get_unique_values_from_columns, get_data_from_collection
from data.prepare_data import prepare_date_columns, group_data, aggregate_data
from apps.ui_elements.agrid.agrid_video import get_table, set_ggrid_options
import plotly.express as px


def app():
    st.title('Clients')
    st.sidebar.subheader("St-AgGrid example options")

    query = {}
    df = get_data_from_collection('clients', query)
    df = df.reset_index()
    df = df[['_id', 'date_created', 'customer_group_id']]

    def parse_date_created(df):
        df['date_created'] = pd.to_datetime(df['date_created'])
        df['month_created'] = df['date_created'].dt.month
        df['year_created'] = df['date_created'].dt.year
        df['day_created'] = df['date_created'].dt.day
        df['weekday_created'] = df['date_created'].dt.weekday
        df['hour_created'] = df['date_created'].dt.hour
        df['day_of_year_created'] = df['date_created'].dt.dayofyear
        df['month_created_str'] = df['date_created'].dt.strftime("%b")

        df['date_created'] = df['date_created'].dt.date

        return df

    df = parse_date_created(df)

    def aggregate_date_created(df):
        df = df[['_id', 'date_created']].groupby(['date_created']).count()
        df = df.reset_index()
        df = df.rename(columns={'_id': 'count'})
        return df

    def aggregate_monthly(df):
        df = df[['_id', 'month_created']].groupby(['month_created']).count()
        df = df.reset_index()
        df = df.rename(columns={'_id': 'count'})
        return df

    def aggregate_yearly(df):
        df = df[['_id', 'year_created']].groupby(['year_created']).count()
        df = df.reset_index()
        df = df.rename(columns={'_id': 'count'})
        return df

    dayly_agg = aggregate_date_created(df)
    monthly_agg = aggregate_monthly(df)
    yearly_agg = aggregate_yearly(df)

    df1 = df[['date_created', 'month_created_str', 'day_created', '_id']].groupby(
        ['date_created', 'month_created_str', 'day_created']).count().reset_index().rename(columns={'_id': 'count'})

    df1 = df1[['month_created_str', 'day_created', 'count']].set_index('day_created')



    fig = px.area(df1, facet_col="month_created_str", facet_col_wrap=3,
                  color_discrete_sequence=px.colors.sequential.Plasma)
    # fig.show()

    st.plotly_chart(fig, use_container_width=True)

    # df = prepare_date_columns(df)
    gb = set_ggrid_options(df)

    gridOptions = gb.build()
    grid_response = get_table(df, gridOptions)



