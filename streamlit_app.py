import pandas as pd
import streamlit as st
from neuralprophet import NeuralProphet


df = pd.read_csv('/examples/air_passengers.csv')

m = NeuralProphet()

metrics = m.fit(df, freq="D")

forecast = m.predict(df)
