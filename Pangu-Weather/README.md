# Pangu-Weather Local Inference & Antarctic Validation

This module handles the local execution of Huawei's Pangu-Weather (3DEST) model using the ECMWF `ai-models` wrapper, specifically optimized for Apple Silicon (ONNX Runtime) 


To bypass GitHub file-size limits, the 3GB `.onnx` weights are not stored in this repository. 

Before running the inference scripts, you must fetch the pre-trained weights directly from the ECMWF storage bucket by running:
`ai-models --download-assets panguweather`

## Data Pipeline Pipeline (CDS)
This pipeline utilizes the Copernicus Climate Data Store (CDS) for ERA5 initialization grids. 
1. Ensure your `~/.cdsapirc` file is configured with your API token.
2. The primary execution command to fetch data and run inference is:
`ai-models --input cds --date YYYYMMDD --time 0000 --lead-time 24 panguweather`

