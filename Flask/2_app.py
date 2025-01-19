from flask import Flask

'''
Creating an instance of Flask i.e WSGI (Web Server Gateway Interface)
'''
app = Flask(__name__)  # app is an instance of Flask class that works as WSGI application
                       # __name__ tells the Flask about where the application is located


# Creating Routes - routes are url that user go to.
@app.route('/home') # when you write this ("/home") after that default url i.e (http://127.0.0.1:5000/home), below function will be called
def home_page(): 
    return "You are in home page ☻, HEheheeh, testing the debugger"

@app.route('/about')
def about_page():
    return "You are in about page"    


# if __name__ == "__main__" : # Entry point of execution
#     app.run() # This executes the file
#     '''This block ensures that the application runs only if the script is executed directly (not imported as a module)'''

if __name__ == "__main__":
    app.run(debug=True)  
    '''
    debug = True 
    1. Enables Debugger 
        If an error occurs, instead of a plain error page,you'll see detailed error traceback
    2. Automatic Code Reloading (we do not have to run the code again after making changes)
    3. Enables Better Error Logging
    '''