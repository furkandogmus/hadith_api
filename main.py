from flask import Flask,jsonify
import random
import json
app = Flask(__name__)
with open("hadith.json","r",encoding="utf-8") as file:
    data = json.load(file)

@app.route('/')
def random_hadith():
    # Select a random hadith from the JSON data
    _, hadith = random.choice(list(data.items()))
    hadith = json.dumps(hadith, ensure_ascii=True)
    return jsonify(hadith), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)