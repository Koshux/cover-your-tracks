from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('front.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html', title="Privacy Policy")

if __name__ == "__main__":
    app.run()