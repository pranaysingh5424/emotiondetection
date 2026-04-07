"""
Flask server for Emotion Detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests.
    """
    text = request.args.get('textToAnalyze')

    if not text or text.strip() == "":
        return "Error: No text provided"

    result = emotion_detector(text)

    if result is None:
        return "Invalid input! Try again."

    return (
        f"Anger: {result['anger']}<br>"
        f"Disgust: {result['disgust']}<br>"
        f"Fear: {result['fear']}<br>"
        f"Joy: {result['joy']}<br>"
        f"Sadness: {result['sadness']}<br>"
        f"Dominant Emotion: {result['dominant_emotion']}"
    )


if __name__ == "__main__":
    app.run(debug=True)