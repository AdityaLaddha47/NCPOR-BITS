india = temp.sel(
    latitude=slice(35,5),
    longitude=slice(65,95)
)

india.plot()
plt.show()