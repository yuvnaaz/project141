from flask import Flask,jsonify,request
import csv

allarticles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]
liked_articles = []
not_liked_articles = []

app = Flask(_name_)
@app.route('/get-article')
def get-article():
    return jsonify({
    'data': allarticles[0]:
    'status': 'success'
    }
)
@app.route('/liked-articles', methods = ['POST'])
def articles():
    article = allarticles[0]
    allarticles = allarticles[1:]
    liked_articles.append(arcticles)
    return jsonify({
        'status': 'success', 
    }),201
@app.route('/not-liked-articles', methods = ['POST'])
def not_liked_articles():
    articles = allarticles[0]
    allarticles = allarticles[1:]
    not_liked_articles.append(articles)
    return jsonify({
        'status': 'success', 
    }),201

if __name__ == "__main__":
    app.run()