"""
This module implements a Flask application to detect emotions
in user-provided text input via an API.
"""

from flask import Flask, jsonify, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def home():
    """
    Renders the home page of the application.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detect():
    """
    Detects the emotion of the provided text input.

    Returns:
        Response: JSON response containing the detected emotion or an error message.
    """
    statement = request.args.get("textToAnalyze", "").strip()

    if not statement:
        response = {"error": "Invalid text! Please try again!"}
        return jsonify(response), 400

    try:
        response = emotion_detector(statement)
        dominant_response = response.get("emotion")

        if dominant_response is None:
            response = {"error": "Invalid text! Please try again!"}
            return jsonify(response), 400

        return jsonify(response)

    except ValueError as error:
        return jsonify({"error": f"Failed to detect emotion: {error}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    