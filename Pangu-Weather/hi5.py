import xarray as xr

print("Loading global tensor for coastal gradient analysis...")
ds = xr.open_dataset("panguweather.grib", engine="cfgrib")

# Using the working 1000 hPa temperature array
t_surface = ds["t"].sel(isobaricInhPa=1000)
if t_surface.ndim > 2:
    t_surface = t_surface[-1]  # Grab the forecast step

stations = {
    "Maitri Station": {"lat": -70.76, "lon": 11.73},
    "Bharati Station": {"lat": -69.40, "lon": 76.18}
}

print("\n==================================================")
print("       COASTAL PIXEL GRADIENT REPORT              ")
print("==================================================")

for name, coords in stations.items():
    # Get the coordinate values of the closest grid intersection
    matched_point = t_surface.sel(latitude=coords["lat"], longitude=coords["lon"], method="nearest")
    lat_idx = float(matched_point.latitude)
    lon_idx = float(matched_point.longitude)
    
    print(f"\nTarget: {name} (True: {coords['lat']}°S, {coords['lon']}°E)")
    print(f"Nearest Model Grid Center: {lat_idx:.2f}°S, {lon_idx:.2f}°E")
    
    # Extract a 3x3 pixel box around the station center to see the shift
    # Pangu grid spacing is 0.25 degrees
    print("  [Surrounding Temperature Gradient (Celsius)]:")
    
    for d_lat in [0.25, 0.0, -0.25]:
        row_str = "    "
        for d_lon in [-0.25, 0.0, 0.25]:
            p = t_surface.sel(latitude=lat_idx + d_lat, longitude=lon_idx + d_lon, method="nearest")
            val_c = float(p.values) - 273.15
            
            # Label the center pixel where the station is mapped
            if d_lat == 0.0 and d_lon == 0.0:
                row_str += f"| *{val_c:.1f}°C* | "
            else:
                row_str += f"  {val_c:.1f}°C   "
        print(row_str)
print("\n==================================================")