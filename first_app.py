import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import constants
from io import StringIO


table_option = st.selectbox(
    'Choose a table',
    constants.TABLES)

table_link = {
    'f_food_metrics': 'https://alation-ha.data-engineering.myteksi.net/table/417640/',
    'agg_passenger_bookings_d':'https://alation-ha.data-engineering.myteksi.net/table/420177/',
}

st.write('Alation: ['+table_option+']('+table_link[table_option]+')')


categories_selected = st.multiselect(
    'Choose categories', constants.CATEGORY_COLUMNS[table_option])

metrics_selected = st.multiselect(
    'Choose metrics', constants.METRIC_COLUMNS[table_option])


# col1, col2, col3 = st.beta_columns(3)
# with col1:
#     filter_options = [k for k,_ in constants.FILTER_OPTIONS.items()]
#     filters_selected = st.multiselect('Choose filters', filter_options)
# with col2:
#     st.selectbox('Choose a table',constants.TEST_COLUMNS)
filter_options = [k for k,_ in constants.FILTER_OPTIONS.items()]
filters_selected = st.multiselect('Choose filters', filter_options)



def get_structure(categories_selected,metrics_selected):
    status_map={}
    if len(categories_selected) > 0 and len(metrics_selected) > 0:
        status_map['first_column'] = 'basic'
    elif len(categories_selected) > 0: # it overlaps with above, but doing this for clarity
        status_map['first_column'] = 'basic'
    elif len(metrics_selected) > 0:
        status_map['first_column'] = 'agg'
    else:
        status_map['first_column'] = 'not_found'

    if len(filters_selected) > 0:
        status_map['has_filters'] = True
    else:
        status_map['has_filters'] = False
    
    return status_map

def write_basic_columns(s,status_map):
    result = ''
    if status_map['first_column'] == 'basic':
        result += '\t'+s[0]
        s = s[1:]

    if s is not None:
        for i in s:
            result += '\n\t, ' + i + ''
    return result
\

def write_agg_columns(s,status_map):
    result = ''
    if s is not None:
        for i in s:
            result += '\n\t, SUM(' + i + ') AS '+i
    return result




def write_filters(s,status_map):
    result = ''
    if status_map['has_filters']:
        result = 'WHERE '
        result += '\n\t'+constants.FILTER_OPTIONS[s[0]]
        s = s[1:]
    if s is not None:
        for i in s:
            result += '\n\tAND ' + constants.FILTER_OPTIONS[i] + ''
    return result

def group_by(n):
    s=''
    for i in range(1, n+1):
        s = s + str(i) + ','
    return 'GROUP BY ' + s[:-1]

status_map = get_structure(categories_selected,metrics_selected)

if len(categories_selected) == 0 and len(metrics_selected) == 0:
    script_text = 'Pick some columns!'
else:
    script_text = "SELECT TOP 10 " \
    + '\n' + write_basic_columns(categories_selected,status_map) \
    + '\n' + write_agg_columns(metrics_selected,status_map) \
    + '\n' + 'FROM ' + table_option \
    + '\n' + write_filters(filters_selected,status_map) \
    + '\n' + group_by(len(categories_selected))


st.code(script_text)


'''
### Tips
Copy the script to the clipboard by hovering over the code. A clipboard icon will appear.

Understand the common tables and columns we use. Check out our [question bank](http://google.com)!

ADW is queried using T-SQL. Main differences between other common SQL syntax:
- Use TOP instead of LIMIT
- Use *GROUP BY column1, column 2, etc...* instead of *GROUP BY 1, 2, 3*
- When grouping, you'll need to specify the full transformation and not the alias. 
For example, when you have something like *CONCAT('aaa', 'bbb', 'ccc') AS concat_string*, then
instead of *GROUP BY concat_string*, you'll have to specify the transformation: *GROUP BY CONCAT('aaa', 'bbb', 'ccc')* 

'''


# copy_button = st.button(label="Get Clipboard Data")


# result = streamlit_bokeh_events(
#     copy_button,
#     events="GET_TEXT",
#     key="get_text",
#     refresh_on_update=False,
#     override_height=75,
#     debounce_time=0)

# if result:
#     if "GET_TEXT" in result:
#         df = pd.read_csv(StringIO(result.get("GET_TEXT")))
#         st.table(df)


# category_3 = st.selectbox(
#     'Choose columns',
#      constants.COLUMNS[table_option])

# category_4 = st.selectbox(
#     'Choose columns',
#      constants.COLUMNS[table_option])

# metric_1 = st.selectbox(
#     'Choose columns',
#      constants.COLUMNS[table_option])

# metric_2 = st.selectbox(
#     'Choose columns',
#      constants.COLUMNS[table_option])

# metric_3 = st.selectbox(
#     'Choose columns',
#      constants.COLUMNS[table_option])

# metric_4 = st.selectbox(
#     'Choose columns',
#      constants.COLUMNS[table_option])


# st.title('My first app')


# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })


# left_column, right_column = st.beta_columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     right_column.write("Woohoo!")

# expander = st.beta_expander("FAQ")
# expander.write("Here you could put in some really, really long explanations...")


# sentence = st.text_input('Input your sentence here:')

# if sentence:
#     st.write(sentence)
