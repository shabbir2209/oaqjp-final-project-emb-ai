from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector 

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detect():
    statement = request.args.get("textToAnalyze")
    print(f'statement {statement}')
    if not statement:
        return jsonify({"error": "Missing 'statement' parameter in the request"}), 400

    try:
        response = emotion_detector(statement)
        
    except Exception as e:
        print(e)
        return jsonify({"error": f"Failed to detect emotion: {str(e)}"}), 500

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
