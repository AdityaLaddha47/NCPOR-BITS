import xarray as xr
import matplotlib.pyplot as plt


ds = xr.open_dataset(
    "panguweather.grib",
    engine="cfgrib"
)


temp = ds.t.sel(
    isobaricInhPa=850
).isel(step=4)

india = temp.sel(

    latitude=slice(35, 5),

    longitude=slice(65, 95)

)

# Plot

india.plot()

plt.show()