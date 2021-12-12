import flask
from text_conversion.SentimentAnalyzer import SentimentAnalyzer
from text_conversion.ConversionManager import create_song
from util.AnalysisUtil import print_object
from flask import request, jsonify, abort, make_response
import json

print("Creating app")
app = flask.Flask(__name__)
print("Initializing sentiment analyzer")
sentiment_analyzer = SentimentAnalyzer()


@app.route('/test', methods={'GET'})
def test_endpoint():
    print("TEST ENDPOINT CALLED")
    return "TEST"


@app.route('/convert-text-to-music', methods={'POST', 'OPTIONS'})
def convert():
    print("Received request")
    if request.method == "OPTIONS":  # CORS preflight
        print("Received preflight call")
        return build_cors_preflight_response()
    request_json = json.loads(request.data)
    text = request_json["text"]
    print("Text received: " + text)
    song = create_song(text, sentiment_analyzer)
    json_response = jsonify(song.to_dict())
    print("Response: " + str(json_response))
    return corsify_actual_response(json_response), 201


def build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "GET,POST")
    return response


def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def main():
    print("Running app")
    app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == '__main__':
    main()
