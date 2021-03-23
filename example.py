from flask import Flask

app = Flask(__name__)

with open("word.txt", "w") as f:
    f.write("OpenDevUFCG é show!")

@app.route('/')
def read():
    with open("word.txt", "r") as f:
        word = f.read()
    return word

@app.route('/<word>')
def write(word):
    with open("word.txt", "w") as f:
        f.write(word)
    return "Mudado :)"
    
app.run()