from flask import Flask, render_template, redirect, url_for

from plotlydash.dashboard import init_dashboard

app = Flask(__name__)
with app.app_context():
    app = init_dashboard(app)

@app.route("/")
def index():
    return "Hello Team Edge!"

@app.route("/python")
def hello_python():
    return "Custom Python placeholder page"

@app.route('/code-next')
def code_next_page():
    return render_template("codenext.html")

@app.route('/dashapp-intro')
def dashapp_intro():
    return redirect(url_for("/dashapp/"))

if __name__ == '__main__':
    app.run(debug=True)
