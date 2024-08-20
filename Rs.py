from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

flowers = {
    "love": [{"name": "Rose", "meaning": "Love and Passion"},
             {"name": "Tulip", "meaning": "Perfect Love"}],
    "friendship": [{"name": "Yellow Rose", "meaning": "Friendship and Joy"},
                   {"name": "Sunflower", "meaning": "Loyalty and Adoration"}],
    "sympathy": [{"name": "Lily", "meaning": "Sympathy and Purity"},
                 {"name": "Chrysanthemum", "meaning": "Support and Encouragement"}],
    "gratitude": [{"name": "Pink Carnation", "meaning": "Thankfulness and Gratitude"},
                  {"name": "Hydrangea", "meaning": "Heartfelt Gratitude"}],
    "new beginnings": [{"name": "Daffodil", "meaning": "New Beginnings and Rebirth"},
                       {"name": "Iris", "meaning": "Hope and Faith"}],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])

def recommend():
    data = request.json
    sentiment = data.get('sentiment', '').lower()
    recommendations = flowers.get(sentiment, [{"name": "No recommendation found", "meaning": "Try another sentiment"}])
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
