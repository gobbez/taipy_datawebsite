import pandas as pd
from taipy.gui import Gui
import taipy.gui.builder as tgb
from pytrends.request import TrendReq


def load_trends():
    def get_trends_data(keyword, timeframe):
        # Get data from Google Trends
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo='IT', gprop='')
        try:
            data = pytrends.interest_over_time()
            data = data.drop(columns=['isPartial'])
            data = data.rename(columns={f"{keyword}": 'search'})
            data = data.reset_index()
        except:
            data = pd.DataFrame({'date': [], 'search': []})
        return data


    def submit_search(state):
        """React to the button press action. """
        global data, keyword, time_select
        if state.time_select == '1 Month':
            state.time_select = 'today 1-m'
        elif state.time_select == '3 Months':
            state.time_select = 'today 3-m'
        elif state.time_select == '12 Months':
            state.time_select = 'today 12-m'
        state.data = get_trends_data(state.keyword, state.time_select)
        data = state.data


    # Initial values
    keyword = 'Vignate'
    time_select = '1 Month'
    time_selection = ['1 Month', '3 Months', '12 Months']
    description = (f"This page lets you see the trend-line of the term searched (es: Italy). "
                   f"It will show the graph and the datatable with filters and download. ")
    data = get_trends_data('Italy', 'today 1-m')


    """Page with Google Trends Analysis"""
    # Define the page layout
    with tgb.Page() as trends:
        tgb.text(value="# Trend Web", mode="md")
        with tgb.layout(columns="5 5 35 5"):
            tgb.input(label='Search something..', value="{keyword}")
            tgb.selector(label='Timeframe', value="{time_select}", lov="{time_selection}", dropdown=True, width="150px")
            tgb.button(label='Search', id='submit', on_action=submit_search)
            tgb.button(label='Informations', hover_text=description, class_name="secondary")

        # Show line plot
        with tgb.layout():
            tgb.chart(data="{data}", x="date", y="search")
            tgb.table(data="{data}", filter=True, downloadable=True, height="50vh")
    return trends

