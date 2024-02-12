from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sort_names():
    sorted_names = ""
    if request.method == 'POST':
        names = request.form.get('names')
        names_list = names.split('\n')
        random.shuffle(names_list)
        sorted_names = '\n'.join(names_list)
    return render_template('index.html', sorted_names=sorted_names)

if __name__ == '__main__':
    app.run(debug=True)