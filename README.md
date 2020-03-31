# SIR spatial simulation

This program simulates epidemiology of the COVID-19 virus using [SIR Models](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model). For given regional segmentation and commuter data it simulates how infections spread over time. It plots the SIR data over time and generates an animated map to visualize the infection and recovery ratio.


# Simulation Model
Each regional area, which can be a city, district or any other type of division, has its own SIR model instance. We model social exchange between those area using commuter data. For simplification, we assume that during daytime, commuters are at there working place, interacting with everyone in the same area. At night, everyone is at home, possibly infecting everyone else with the same home area.

We use these SIR differential equantions:
```
dS/dt = -beta * I/N * S
dI/dt = beta * I/N * S - I * gamma
dR/dt = I * gamma
```


# Run
```
git clone https://github.com/fl4p/sirmodel
cd sirmodel/simulator
pip install -r requirements.txt
python3 Simulation.py
```

After the simulation has finished, open `web/animation.html` with your browser to view the animated map.



# Configuartion

## SIR Parameters
You can edit the `beta` and `gamma` for the SIR differential equations in `simulator/SIRModel.py`:
```
    beta = 1.1
    gamma = 1 / 14
```

## Initial Infections
Edit the file `simulator/pendlerData/start.csv`, defaults are:
```
id,inf,rec
09188,1000,0
05370,1000,0
08117,1000,0
```

Columns:
`id` is the area ID (for Germany you can find the real values inside `BewohnerProLandkreis.csv`)
`inf` is the inital count of infected individuals
`rec` is the inital cound of recovered individuals




# Further Improvements
* Use Monte Carlo simulation for infection distribution between commuting groups
* Add random commuting "noise"


