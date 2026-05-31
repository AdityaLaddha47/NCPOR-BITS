# Pangu-Weather Local Inference & Antarctic Validation

This module handles the local execution of Huawei's Pangu-Weather (3DEST) model using the ECMWF `ai-models` wrapper, specifically optimized for Apple Silicon (ONNX Runtime) and Antarctic coastal validation (Maitri & Bharati stations).

## ⚠️ Important: Downloading Model Weights
To bypass GitHub file-size limits, the 3GB `.onnx` weights are not stored in this repository. 

Before running the inference scripts, you must fetch the pre-trained weights directly from the ECMWF storage bucket by running:
`ai-models --download-assets panguweather`

## Data Pipeline Pipeline (CDS)
This pipeline utilizes the Copernicus Climate Data Store (CDS) for ERA5 initialization grids. 
1. Ensure your `~/.cdsapirc` file is configured with your API token.
2. The primary execution command to fetch data and run inference is:
`ai-models --input cds --date YYYYMMDD --time 0000 --lead-time 24 panguweather`

## Validation Scripts
* `pangu_inference.py`: Executes the core ONNX runtime.
* `polar_check.py`: Extracts exact 1000hPa surface temperatures for Maitri and Bharati.
* `shoreline_analysis.py`: Generates a 3x3 spatial pixel gradient to diagnose coastal smoothing/land-sea mask boundary errors.
