from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mission = "Technology Engineering Operations"
    clouds = ["GCP", "Azure"]
    return render_template('basic.html', mission = mission, mycloud = clouds)

if __name__ == '__main__':
    app.run(debug=True)    
