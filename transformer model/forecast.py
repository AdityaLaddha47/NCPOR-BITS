import pandas as pd
import torch
from chronos import ChronosPipeline

# Load clean data
df = pd.read_csv("goa_temperature_clean.csv")
df["time"] = pd.to_datetime(df["time"])

# Prepare input — Chronos needs a torch tensor
context = torch.tensor(df["temperature"].values, dtype=torch.float32)

# Load pretrained Chronos model
pipeline = ChronosPipeline.from_pretrained(
    "amazon/chronos-t5-small",
    device_map="cpu",
    dtype=torch.float32
)

# Forecast next 24 hours
forecast = pipeline.predict(
    inputs=context,
    prediction_length=24
)

# forecast shape: (1, num_samples, 24) — gives probabilistic predictions
median_forecast = forecast[0].median(dim=0).values.numpy()

# Show results
future_times = pd.date_range(
    start=df["time"].iloc[-1] + pd.Timedelta(hours=1),
    periods=24,
    freq="h"
)

result = pd.DataFrame({
    "time": future_times,
    "predicted_temperature": median_forecast.round(2)
})

print(result)
result.to_csv("forecast_output.csv", index=False)
print("\nSaved to forecast_output.csv")
