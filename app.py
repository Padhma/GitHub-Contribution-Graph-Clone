from flask import Flask, render_template, json
import spreadsheet

app = Flask(__name__)

@app.route("/")

def main():
    data = spreadsheet.getLevel()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=5000, threaded=True)
