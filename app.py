from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/social")
def social():
    return render_template('social.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['username']
        message = request.form['message']
    else:
        name = request.args.get('username')
        message = request.args.get('message')

    return f"""
    <h2>Thanks, {name}!</h2>
    <p>Your message: {message}</p>
    """

if __name__ == "__main__":
    app.run(debug=True,port=5001)