from flask import Flask, render_template

app=Flask(_name_)

@aap.route('/')
def home():
    return render_template("home.html")


@aap.route('/about/')
def home():
    return "about content goes here!"

if _name_=="_main_":
    app.run(debug=True)


