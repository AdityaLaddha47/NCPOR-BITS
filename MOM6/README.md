# MOM6 - Modular Ocean Model

## Overview
Ocean temperature and salinity simulations for Antarctic research stations
using NOAA-GFDL MOM6 (Modular Ocean Model version 6).

## Stations
- **Maitri Station**: 70.7°S, 11.7°E
- **Bharati Station**: 69.4°S, 76.2°E

## Configuration
- Model: MOM6 Single Column (EPBL mixing scheme)
- Forcing data: Weddell Sea (Southern Ocean proxy)
- Variables: Temperature, Salinity, Mixed Layer Depth

## Results
- `Weddell/results/weddell_results.csv` - 11-day surface T/S timeseries
- Temperature range: -0.816°C to 0.402°C (real Antarctic values!)
- Salinity range: 34.20 to 34.21 PSU

## How to Run
1. Install MOM6 following setup instructions
2. cd ocean_only/single_column/EPBL
3. mpirun -n 1 ~/demo/ocean_only/build/MOM6
