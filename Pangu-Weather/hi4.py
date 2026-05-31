import xarray as xr

print("Opening")
ds = xr.open_dataset("panguweather.grib", engine="cfgrib")


stations = {
    "Maitri Station": {"lat": -70.76, "lon": 11.73},
    "Bharati Station": {"lat": -69.40, "lon": 76.18}
}

print("\nEXTRACTION ")
for name, coords in stations.items():
   
    local_data = ds.sel(latitude=coords["lat"], longitude=coords["lon"], method="nearest")
    
  
    surface_level = local_data.sel(isobaricInhPa=1000)
    
 
    temp_kelvin = surface_level["t"].values
    if temp_kelvin.ndim > 0:
        temp_kelvin = temp_kelvin[-1]
        
    temp_c = temp_kelvin - 273.15
    
    print(f"{name} ({coords['lat']}°S, {coords['lon']}°E):")
    print(f"  Predicted Surface-Level Temp: {temp_c:.2f} °C")
    print("-" * 50)