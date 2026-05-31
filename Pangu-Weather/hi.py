import xarray as xr

ds = xr.open_dataset(
    "panguweather.grib",
    engine="cfgrib"
)

print(ds)