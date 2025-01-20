# Understanding HTTPS verbs : get, post
from flask import Flask,render_template,request
'''
POST: Used to submit data (e.g., form submissions).
GET: Used to retrieve data (e.g., accessing the form).
'''
app = Flask(__name__)

@app.route('/',methods = ['GET'])  #for home page
def home_page():
    return render_template('home_page.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.form.get('username')  # Ensure this matches the 'name' attribute in the form
        password = request.form.get('password')
        return f"Form submitted! Your name is {name} and your password is {password}."
    return render_template('form.html')  # Render the form for GET requests


if __name__ == "__main__":
    app.run(debug=True)

