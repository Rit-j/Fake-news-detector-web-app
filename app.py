from flask import Flask, escape, request, render_template
import pickle

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction", methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)
        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("prediction.html", prediction_text="This news is - {}".format(predict))
        
    else:
        return render_template("prediction.html")


@app.route("/about")
def about():
    return render_template("about.html")        

if __name__ == '__main__':
    app.run()    