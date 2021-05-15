## Dash

Dash is an open-source framework for building analytical applications, with no Javascript required, and it is tightly integrated with the Plotly graphing library. While Plotly is the graphing library, Dash is a library that powers Plotly (in different languages, but this workshop focuses on Python).

### Download the Dataset

This workshop uses the Gamestop Historical Stock data for its analysis. 
1. Click [here](https://www.nasdaq.com/market-activity/stocks/gme/historical) and download the Gamestop stock data as a csv file.
2. Create a new folder inside the `code_next` folder called `data`. Move the newly downloaded data file to the `data` folder.

### Read and Clean the Dataset
1. Import the data using `pd.read_csv()` and use pandas to "clean" or modify the data. This is to ensure that Dash can read and interpret the data correctly, in the way that is useful for our analysis.
2. If you want an advanced figure with custom visuals like time bars, etc. visit the [Time-series in Python](https://plotly.com/python/time-series/) tutorial.

### Build your dashboard
Link your Plotly graphs together using Dash to build a comprehensive dashboard. The Dash dashboard creates its own Flask instance and wraps all the custom HTML/ styling that would normally need to be coded using Javascript + CSS into its own high-level libraries.
