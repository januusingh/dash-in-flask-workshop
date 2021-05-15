# Dash-in-Flask Workshop

### Purpose
[Dash](https://dash.plotly.com/) is an open-source framework for building analytical applications, with no Javascript required, and it is tightly integrated with the [Plotly](https://plotly.com/python/) graphing library ([example](https://dash-gallery.plotly.host/dash-oil-and-gas/ )). We can use Dash to create detailed data-visualizations to generate insight into large datasets in Python and display it in an existing [Flask](https://flask.palletsprojects.com/en/1.1.x/) application which may server other purposes in a website. 

Flask is a very popular backend framework for web applications. We will use Flask to handle all the incoming requests from our clients and serve them the necessary HTML content, including the Dash dashboard that you create. This will allow you to create multiple custom dashboards and/or visualizations in your web server.

This workshop was inspired and adapted by concepts and methods introduced in other public tutorials [[1](https://hackersandslackers.com/plotly-dash-with-flask/), [2](https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b)].

### Setup
Follow the steps to get your environments set up for this workshop:
1. Download [Anaconda for Python](https://docs.anaconda.com/anaconda/install/) and create a new virtual enviornment called dashapp by running the following command: `conda create --name dashapp`.
2. Activate your virtual environment by running `conda activate dashapp` in your terminal.
3. Download Flask: `pip install Flask`
4. Download Dash: `pip install dash`
5. Download Pandas: `pip install pandas`

### Tools and Resources
1. [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html) (data manipulation) 
2. [Plotly Express](https://plotly.com/python/plotly-express/) (building custom visualizations) 
3. [Dash](https://dash.plotly.com/layout) (displaying visualizations on a custom Dashboard)
4. [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) (building web applications for any use or purpose) 
5. [Jupyter](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) (visualization for fun to explore)
6. [Stackoverflow](https://stackoverflow.com/) (general questions)
