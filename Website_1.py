from flask import Flask, render_template

# Made by Christina Williams October 15, 2020.

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("Main.html")


# Remember that the actual website for each project has to be published and linked.

@app.route('/movies')
def movies():
    return render_template("movies.html")


# look up how to link videos, if my method doesn't work

@app.route('/catalog')
def catalog():
    return render_template("catalog.html")


# maybe listing my own supplies in SQLite can show my SQLite Skills

@app.route('/map')
def map():
    return render_template("map.html")


# Google map API needed and will look at cool spots in San Francisco. Maybe consider San Francisco Natives opinion
# more of a thought than a comment. But, I think this is going to be my favorite project.

@app.route('/resume')
def resume():
   return render_template("resume.html")


# Consider doing resume website after we create resume in class?

if __name__ == '__main__':
    app.route(debug=True)
