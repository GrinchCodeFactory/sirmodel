# Spatial SIR model simulation

This program simulates epidemiology of the COVID-19 virus using [SIR Models](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model). For given regional segmentation and commuter data it simulates how infections spread over time. It plots the SIR data over time and generates an animated map to visualize the infection and recovery ratio.

# Simulation Model
Each regional area, which can be a city, district or any other type of division, has its own SIR model instance. We model social exchange between those area using commuter data. For simplification, we assume that during daytime, commuters are at there working place, interacting with everyone in the same area. At night, everyone is at home, possibly infecting everyone else with the same home area.


We use [SIR models](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model)

Simulator for 
