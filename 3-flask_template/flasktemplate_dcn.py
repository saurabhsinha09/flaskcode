from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    mission = "Technology Engineering Operations"
    clouds = ["GCP", "Azure"]
    return render_template('about.html', mission = mission, mycloud = clouds)    

@app.route('/signup') 
def signup():
    return render_template("signup.html")   

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    company_check = verification(request.args.get('company'))
    return render_template("thankyou.html", first = first, last = last, name_check = company_check)    

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

def verification(company):

    checks = {}
    lower_letter = any(c.islower() for c in company)
    upper_letter = any(c.isupper() for c in company)
    num_end = company[-1].isdigit()
    report = lower_letter and upper_letter and num_end
    #print("ll: "+ str(lower_letter), "ul: "+ str(upper_letter), "ne: "+ str(num_end), "report: "+ str(report))

    checks = {'lower_letter' :lower_letter,
              'upper_letter' : upper_letter,
              'num_end' : num_end,
               'report' : report}

    return checks

if __name__ == '__main__':
    app.run(debug=True)    