from flask import Flask, render_template

app = Flask(__name__)


# Add the option to run this directly 

# Make a homepage
@app.route('/')
def homepage():
    contentList = ["Hello my name is Nav!  This is my first site ever."]
    return render_template('homepage.html', aboutMe = contentList)


@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Yoyo", "Yenifer"]
    return render_template('name.html', Sname = name, nameList = listOfNames)



@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)




if __name__ == "__main__":
    app.run(debug = True)

