## Flask

### Core Flask Logic
`app.py` is the file that creates most of the core logic of our Flask server. Decorators, or the code that starts with the @ symbol, in `app.py` is used by Flask to interpret commands as routes. This tells Flask that it wants to treat the code in the decorated function as a new web page, or route. [This link](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) has more information about complex routing.

`render_template()` is another core function which we will use to serve HTML content as a file name.

### Rendering Dash in an existing Flask app
Dash (which powers the powerful Plotly visualizations), is actually built on top of Flask. So the Dashboard that we created earlier internally creates its own Flask instance and wraps all the custom HTML/ styling that would normally need to be coded using Javascript + CSS into its own high-level libraries.

We can utilize a sample Flask server to power our Dashboard in a custom way. All you have to do to integrate them is to add complex graphs to plotlydash/dashboard.py You can add new `@app.route()` in `app.py` for as many different dashboards as you want.

### Deploying a local Flask application
Once you feel like your Flask server is ready, you can deploy your local Flask server to Heroku or Google App Engine. Below are some linked tutorials:

- [Deploy Flask to Heruoku](https://stackabuse.com/deploying-a-flask-application-to-heroku/)
- [Deploy Flask to App Engine](https://medium.com/@dmahugh_70618/deploying-a-flask-app-to-google-app-engine-faa883b5ffab)
