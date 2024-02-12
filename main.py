from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sort_names():
    names = ""
    sorted_names = ""
    if request.method == 'POST':
        names = request.form.get('names')
        names_list = names.split('\n')
        random.shuffle(names_list)
        sorted_names = '\n\n'.join(['\n'.join(names_list[i:i+2]) for i in range(0, len(names_list), 2)])
    return render_template('index.html', names=names, sorted_names=sorted_names)

if __name__ == '__main__':
    app.run(debug=True)
