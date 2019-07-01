from flask import Flask, request
from caesar import rotate_string
app=Flask (__name__)
app.config['DEBUG']=True

# When we use a single open and close curly brace in our HTML, the string.format function is going to think that's a placeholder. 
# For that reason, in the STYLE section, we need to use double curly braces. 
# Of course, in a proper setup, we would not have this problem, because we wouldn't use an inline style sheet, but link to a separate CSS file

form="""

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST">
            <label>
                <input name="rot" type="text" /> 
            </label>

            <p><textarea name="source" id="" cols="30" rows="10">{0}</textarea></p>
            <input type="submit" />

        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
# This tells the app that, when a POST call is made to just the base path (for instance, localhost:5000/), this is the code to be executed. 
def encrypt():
    text=request.form['source']
    rot=int(request.form['rot'])
    result=rotate_string(text, rot)
    return form.format(result)

@app.route("/")
# This tells the app that, when a GET call is made to just the base path (for instance, localhost:5000/), this is the code to be executed. 
# Remember that, if a method is not specified, GET will be the default. 
def index():
    return form.format("")

app.run()