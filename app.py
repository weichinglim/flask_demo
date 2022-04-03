from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

friend_list = [{"name": "Mike Colbert"}]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Mike\'s Friends', friends = friend_list)

@app.route('/mike')
def mike():
    return render_template('mike.html', pageTitle='About Mike')

@app.route('/add_friend', methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST':
        form = request.form
        fname = form['fname']
        lname = form['lname']
        #print(fname)
        #print(lname)
        friend_dict = {"name": fname + " " + lname}
        #print(friend_dict)
        friend_list.append(friend_dict)
        #print(friend_list)
        return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
