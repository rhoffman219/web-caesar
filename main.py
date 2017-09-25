from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>

            form {{
                background-color: #eee;
                padding: 20px;
                magin: 0 auto;
                width: 540px;
                font: 16 px sans-serif;
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
        <form method= 'POST'>

            <label for='rot'>Rotate by:</label>
                <input name="rot" type="text" value="0" />
            
                <textarea name="text" type="text">{m}</textarea>           
            

            
            <input type="submit" value="Submit Query" />
        </form>


    </body>



</html>
"""


@app.route("/")
def index():
    return form.format(m='')

@app.route("/", methods=['POST'])
def encrypt():
    message = ''
    rotate_by = request.form['rot']
    text = request.form['text']
    for char in text:
        if char.isalpha():
            message += rotate_character(char, rotate_by)
        else:
            message += char
       
    return form.format(m=message)

app.run()