from flask import Flask, render_template, abort
import os

app = Flask(__name__)

@app.route("/")
def main():
    if 'kakao_javascript_key' not in os.environ:
        return abort(500)
    return render_template("local_map.html", api_key=os.environ.get('kakao_javascript_key', ''))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
