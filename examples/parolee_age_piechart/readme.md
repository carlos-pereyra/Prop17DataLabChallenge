# 1. Install Dependencies
One of the easiest package installers to use is [Miniconda](https://docs.conda.io/en/latest/miniconda.html). I'd recommend using it
to install the dependencies that are mentioned below.
````
conda install -c plotly plotly=4.10.0
conda install numpy
conda install pyshp
conda install pandas
conda install -c plotly plotly-geo
conda install geopandas
````

next create an environment called 'sandbox'
```
conda create -n myenv sandbox
```

start environment
```
conda activate sandbox
```

Benefits of plotly
* scatter mapbox plots
* choropeth maps

# 2. Execute example
How to run this example. This example uses python and all the dependencies above.

````
python ParoleAge.py
````

# 3. Output
There will be a new .html file that plots the mapped out distribution of parolees in California counties.
Additionally plotly will automatically forward you to the visual on your web-browser.

The new html file for usage on websites can be found the directory below:
```
/docs/html/parole_age.html
```

