from flask import Flask, request
from caesar import rotate_string
app=Flask (__name__)
app.config['DEBUG']=True

form="""

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="POST">
            <label>
                <input name="rot" type="text" /> 
            </label>

            <p><textarea name="source" id="" cols="30" rows="10"></textarea></p>
            <input type="submit" />

        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    text=request.form['source']
    rot=int(request.form['rot'])
    result=rotate_string(text, rot)
    return result

@app.route("/")
def index():
    return form

app.run()