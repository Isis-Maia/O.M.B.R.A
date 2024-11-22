from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def boi():
    inf_boi = [
        {"nome": "Boitatá" , "comprimento" : "8m" , "altura" : "4m" , "peso" : "260t" , "habitat" : "florestas"},
    ]
    return render_template('index.html' , inf_boi=inf_boi)

def curupira():
    inf_curupira = [
        {"nome" : "Curupira" , "Altura" : "1,64" , "habitat" : "florestas"},
    ]

if __name__ == '__main__':
    app.run(debug=True)

