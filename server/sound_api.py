from flask import Flask, request, jsonify

from read_sound import read_sound

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    audio_file = request.files["file"]
    # print(audio_file.filename)
    audio_file.save(audio_file.filename)
    text=read_sound()

    result = {"text": text}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)