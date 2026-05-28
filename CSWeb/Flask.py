"""
Flask School Survey
Student Name: Jackson Lieberman
Description:
Simple school review survey website
Sources: https://docs.python.org/3/library/datetime.html, https://flask.palletsprojects.com/en/stable/quickstart/, https://flask.palletsprojects.com/en/stable/tutorial/templates/
Version: 2.1
"""

from flask import Flask, render_template, request                           #imports
import csv                                                                  #for writing rows to a .csv file
import os                                                                   #to check whether the file already exists
from datetime import datetime                                               #to timestamp each submission

app = Flask(__name__)                                                       #Initialize the Flask application instance

CSV_FILE = "responses.csv"                                                  #name of the file all responses get saved to


def save_to_csv(fname, raw_scores, pct_scores):                             #helper: takes the name and both score dicts
    file_exists = os.path.isfile(CSV_FILE)                                  #True if responses.csv is already there

    header = ["timestamp", "fname"]                                         #start building the column names
    for philosophy in raw_scores:                                           #loop through each philosophy
        header.append(philosophy)                                           #raw score column
        header.append(philosophy + "_pct")                                  #percentage column

    row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), fname]             #first two cells: time and name
    for philosophy in raw_scores:                                           #loop in the same order as the header
        row.append(raw_scores[philosophy])                                  #add the raw score
        row.append(pct_scores[philosophy])                                  #add the percentage

    with open(CSV_FILE, "a", newline="") as f:                              #append mode so old rows stay
        writer = csv.writer(f)                                              #make a csv writer for this file
        if not file_exists:                                                 #only the very first time...
            writer.writerow(header)                                         #...write the column names
        writer.writerow(row)                                                #write this submission's data


@app.route('/')                                                             #bind ('/') to the main() function
def main():
    fname = request.args.get('fname')                                       #looks for parameter named 'fname'
    print(fname)                                                            #debug print to the server console
    return render_template("index.html")                                    #renders index.html to the browser


@app.route('/submit-data')                                                  #route for '/submit-data' 
def submitdata():

    fname = request.args.get('fname')                                       #first name from the form

    # Existentialism
    e1 = request.args.get('Q1_existentialism')                              #does the same get for every next question
    e2 = request.args.get('Q2_existentialism')
    e3 = request.args.get('Q3_existentialism')
    e4 = request.args.get('Q4_existentialism')
    e5 = request.args.get('Q5_existentialism')

    # Utilitarianism
    u1 = request.args.get('Q1_utilitarianism')
    u2 = request.args.get('Q2_utilitarianism')
    u3 = request.args.get('Q3_utilitarianism')
    u4 = request.args.get('Q4_utilitarianism')
    u5 = request.args.get('Q5_utilitarianism')

    # Taoism
    t1 = request.args.get('Q1_taoism')
    t2 = request.args.get('Q2_taoism')
    t3 = request.args.get('Q3_taoism')
    t4 = request.args.get('Q4_taoism')
    t5 = request.args.get('Q5_taoism')

    # Confucianism
    c1 = request.args.get('Q1_confucianism')
    c2 = request.args.get('Q2_confucianism')
    c3 = request.args.get('Q3_confucianism')
    c4 = request.args.get('Q4_confucianism')
    c5 = request.args.get('Q5_confucianism')

    # Nihilism
    n1 = request.args.get('Q1_nihilism')
    n2 = request.args.get('Q2_nihilism')
    n3 = request.args.get('Q3_nihilism')
    n4 = request.args.get('Q4_nihilism')
    n5 = request.args.get('Q5_nihilism')

    # Empiricism
    m1 = request.args.get('Q1_empiricism')
    m2 = request.args.get('Q2_empiricism')
    m3 = request.args.get('Q3_empiricism')
    m4 = request.args.get('Q4_empiricism')
    m5 = request.args.get('Q5_empiricism')

    # Stoicism
    s1 = request.args.get('Q1_stoicism')
    s2 = request.args.get('Q2_stoicism')
    s3 = request.args.get('Q3_stoicism')
    s4 = request.args.get('Q4_stoicism')
    s5 = request.args.get('Q5_stoicism')

    existentialism = int(e1) + int(e2) + int(e3) + int(e4) + int(e5)        #sum the 5 existentialism answers
    utilitarianism = int(u1) + int(u2) + int(u3) + int(u4) + int(u5)        #sum the 5 utilitarianism answers
    taoism = int(t1) + int(t2) + int(t3) + int(t4) + int(t5)                #sum the 5 taoism answers
    confucianism = int(c1) + int(c2) + int(c3) + int(c4) + int(c5)          #sum the 5 confucianism answers
    nihilism = int(n1) + int(n2) + int(n3) + int(n4) + int(n5)              #sum the 5 nihilism answers
    empiricism = int(m1) + int(m2) + int(m3) + int(m4) + int(m5)            #sum the 5 empiricism answers
    stoicism = int(s1) + int(s2) + int(s3) + int(s4) + int(s5)              #sum the 5 stoicism answers

    total = (existentialism + utilitarianism + taoism + confucianism        #grand total, used for the percentages
             + nihilism + empiricism + stoicism)

    existentialism_pct = round(existentialism / total * 100, 1)             #each score as a % of the total, 1 dp
    utilitarianism_pct = round(utilitarianism / total * 100, 1)
    taoism_pct = round(taoism / total * 100, 1)
    confucianism_pct = round(confucianism / total * 100, 1)
    nihilism_pct = round(nihilism / total * 100, 1)
    empiricism_pct = round(empiricism / total * 100, 1)
    stoicism_pct = round(stoicism / total * 100, 1)

    raw_scores = {                                                          #raw point totals
        "existentialism": existentialism,
        "utilitarianism": utilitarianism,
        "taoism": taoism,
        "confucianism": confucianism,
        "nihilism": nihilism,
        "empiricism": empiricism,
        "stoicism": stoicism,
    }

    pct_scores = {                                                          #matching percentages
        "existentialism": existentialism_pct,
        "utilitarianism": utilitarianism_pct,
        "taoism": taoism_pct,
        "confucianism": confucianism_pct,
        "nihilism": nihilism_pct,
        "empiricism": empiricism_pct,
        "stoicism": stoicism_pct,
    }

    save_to_csv(fname, raw_scores, pct_scores)                              #append this submission to responses.csv

    return render_template(                                                 #send the results to the results page
        "results.html",
        fname=fname,                                                        #template variables for results.html
        existentialism=existentialism_pct,
        utilitarianism=utilitarianism_pct,
        taoism=taoism_pct,
        confucianism=confucianism_pct,
        nihilism=nihilism_pct,
        empiricism=empiricism_pct,
        stoicism=stoicism_pct
    )


if __name__ == '__main__':
    app.run(debug=True)