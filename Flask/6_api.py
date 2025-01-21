## Understanding HTTP verbs - DELETE and PUT
## Making a project - TODO list

from flask import Flask,jsonify,redirect,request,url_for
# Jus like we use 'render_template' to retrieve html data, we use jsonify for that of json data

app = Flask(__name__)

# Default tasks (This is a JSON format data)
Todo_list = [
    {'id':1,'task':'task1','description':'This is task 1'},
    {'id':2,'task':'task2','description':'This is task 2'}
]

# Creating Home page
@app.route('/')
def home():
    return "Welcom To This API example"

# Retreiving all data from json  (get request)
@app.route('/todo',methods=['GET'])           # We can use same url multiple times iff method is different
def all_tasks():
    return jsonify(Todo_list)

# Retreiving any one task (get request)
@app.route('/todo/<int:id>')
def get_task(id):
    '''Making using next() on a generator that iterates through [item,none], item is decided using list comprehension to get the task'''
    task = next((item for item in Todo_list if item['id']==id), (None))   
    if task==None:
        return jsonify({'error':'task does not found'})
    else:
        return jsonify(task)


# Adding new data (post request)
@app.route('/todo',methods = ['POST'])
def add_data():
    if not request.json or not 'task' in request.json or not 'description' in request.json:
        return jsonify({'error':'wrong post request'})
    new_item = {
        'id' : Todo_list[-1]['id']+1 if Todo_list else 1,    # It gives the task id to new task, 1 if no tasks prior exists
        'task' : request.json['task'],
        'description': request.json['description']           # req.json is like req.form, it access data given by the user in an http request
    }
    Todo_list.append(new_item)
    return jsonify(new_item)  


# Changing a data (put request) '''PUT is used for change the existing data'''
@app.route('/todo/<int:id>',methods = ['PUT'])
def change_task(id):
    task = next((item for item in Todo_list if item['id']==id ),None) 
    if task == None:  
        return jsonify({'error':'task does not found'})   # if 'id' not found, it gives error
    else:
        # update the task 
        task['task']=request.json.get('task',task['task'])  # we retreiving 'task' if user gives it, otherwise default will give orginal(previous)  values of 'task'
        task['description']=request.json.get('description',task['description'])
        return jsonify(Todo_list)  # Returning the original list this time with changed task
    


# deletion of task (DELETE request)
@app.route('/todo/<int:id>',methods = ['DELETE'])
def delete_task(id):
    global Todo_list       # by mention of this, we tell computer that, we are updating the globally defined "Todo_list" , not making a new one
    Todo_list =[item for item in Todo_list if item['id']!=id]   # keeping only those items that we want
    return jsonify(Todo_list)


if __name__=='__main__':
    app.run(debug = True)

'''
 Note :
    Test this code in 'postman' not in chrome using url, because chrome does not have option to put/delete. Even POST is throup html template only, 
    Browsers like Chrome primarily support GET and POST methods when accessing URLs directly. These are the standard methods used for retrieving and submitting data via forms or navigating pages.
    PUT and DELETE methods are part of the HTTP specification but are not natively supported for direct interaction through the browser's URL bar or standard HTML forms.

'''


## Also for post/put got to body-->raw-->then write the new task (eg; {"task":"pushups","description":"pusss"})