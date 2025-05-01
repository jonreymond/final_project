from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    Retrieve the text to analyze, and return the corresponding emotions and scores
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    output = "For the given statement, the system response is "
    dominant_emotion = response.pop("dominant_emotion")

    for key, value in response.items():
        output += "'" + key +"': " + str(value) + ", "
    output = output[:-2] + ". The dominant emotion is "
    output += '<b>' + dominant_emotion + '</b>' + "."
    return output

@app.route("/")
def render_index_page():
    '''
    Render html file
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
