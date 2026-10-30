
import streamlit as st
import pandas as pd

st.title("Smart Traffic Light Controller")

signal = st.selectbox(
    "Choose Traffic Signal",
    ["Green", "Yellow", "Red"]
)

durations = {
    "Green": 5,  # TASK 2: Update to 7
    "Yellow": 2,
    "Red": 5
}

messages = {
    "Green": "GO",
    "Yellow": "SLOW DOWN",
    "Red": "STOP"
}

st.metric("Duration", f"{durations[signal]} seconds")
st.info(messages[signal])

data = pd.DataFrame({
    "Signal": list(durations.keys()),
    "Duration": list(durations.values())
})

st.dataframe(data)
st.bar_chart(data.set_index("Signal"))

