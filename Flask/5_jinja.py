## Understanding 
# Variable Rule, Building url dynamically, Jinja 2 template engine

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/form')
def form():
    return render_template('form2.html')

@app.route('/submit',methods = ['GET','POST'])
def submit():
    name = request.form.get('name')   
    return f"Hellow {name}!"

# Variable rule : It allows you to define dynamic parts of url, these parts can accept value and pass it to function
@app.route('/marks/<int:score>')  # we can define dtype (here dtype = int. default = str)
def marks(score):
    return f"Your marks is {score}"


# Now, we giving data from here, to html
@app.route('/percentage/<int:score>')  
def percent(score):
    per = str(score) + '%'
    return render_template('percentage.html',percentage = per) # dont forget to give that variable to html file

'''
Jinja2 Template engine
{{ expression }}  used for passing expression
{%...%} for conditional statements, loops
{#...#} for comments

'''
# Showing other ways
@app.route('/marksheet/<int:score>')  
def marksheet(score):
    per = str(score) + '%'
    if score>33:
        res = 'PASSED'
    else:
        res = 'FAILED'
    result = {'Percentage':per,'Result':res}   # making a dict, and calling this throup html template
    return render_template('marksheet.html',result = result)


# Using if condition
@app.route('/marksheetif/<int:score>')
def marksheetif(score):
    return render_template('marksheetif.html',scores = score)


# Building url dynamically 
@app.route('/fillmarks',methods=['GET','POST'])
def fillmarks():
    total_percentage=0
    if request.method=='POST':
        science = float(request.form.get('science'))     # we put key = 'id' given in html template
        maths = float(request.form.get('maths'))
        c = float(request.form.get('c'))
        datascience = float(request.form.get('datascience'))
        total_percentage=(science+maths+c+datascience)/4
        return redirect(url_for('marksheetif',score = total_percentage)) 
    else :
        return render_template('fillmarks.html')
     
    # redirecting the whole function to marksheetif function at the end, when user press submit button

if __name__=="__main__":
    app.run(debug = True)