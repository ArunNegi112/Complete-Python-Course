## Integrating HTML template

from flask import Flask, render_template
# render_template is a function provided by flask framework, to render the HTML templates using jinja 2 template engine
# rendering a template means taking a static html template and combining it with dynamic data provided from flask routes

main = Flask(__name__)

@main.route('/home')
def home_page():
    return render_template('home_page.html')

@main.route('/about')
def about_page():
    return render_template('about_page.html')


# note: keeping these html file in a 'templates' folder is necessary cuz the render_template func looks for 'templates' folder by default
if __name__=="__main__":
    main.run(debug=True)
    