try:
    from subprocess import call
    from Classes import Employee, Event
    from flask import Flask, render_template
except:
    pips = ['pip install ', 'pip3 install ']
    packages = ['flask']
    pythons = ['python ', 'py ', 'python3 ', 'py3 ']

    for pip in pips:
        for package in packages:
            try:
                call(pip + package, shell=True)
            except:
                print(pip + package + ' is not the proper install command')

            for python in pythons:
                try:
                    call(python + pip + package, shell=True)
                except:
                    print(python + pip + package +
                          ' is not the proper install command')
    
    from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")

def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)