import streamlit as st
import pandas as pd
from components.header import main_header
from components.configuration_toggle import get_selection, filter_selection

main_header("DataFrame")


@st.cache_data
def load_data():
    return pd.DataFrame({
        'gender': [
            'Female', 'Male', 'Male', 'Female', 'Male',
            'Female', 'Male', 'Female', 'Male', 'Female'
        ],
        'city': [
            'New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles',
            'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York'
        ],
        'job': [
            'Engineer', 'Teacher', 'Doctor', 'Engineer', 'Teacher',
            'Doctor', 'Engineer', 'Teacher', 'Doctor', 'Engineer'
        ],
        'education': [
            'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master',
            'PhD', 'Bachelor', 'Master', 'PhD', 'Bachelor'
        ]
    })


og_df = load_data()

selections = get_selection(og_df, ["job", "education"])
filtered_df = filter_selection(og_df, selections)
st.dataframe(filtered_df, use_container_width=True)


def print_bar_chart():
    st.subheader("Genre distribution by city")
    gender_city_counts = (
        filtered_df
        .groupby(['city', 'gender'])
        .size()
        .unstack()
    )
    st.bar_chart(gender_city_counts)


def print_error_name():
    st.subheader("Add a error name if there is one")

    df = pd.DataFrame({
        'event_name': ['Ev1', 'Ev2', 'Ev3', 'Ev4', 'Ev5', None],
        'validation_A': [True, False, False, None, True, None],
        'validation_B': [False, True, False, None, True, None],
        'validation_C': [True, True, True, None, True, None]
    })

    df['error_name'] = df.apply(
        (
            lambda row: row['event_name']
            if not (
                row['validation_A'] and
                row['validation_B'] and
                row['validation_C']
            )
            else None
        ),
        axis=1
    )

    st.dataframe(df)


print_bar_chart()
print_error_name()
