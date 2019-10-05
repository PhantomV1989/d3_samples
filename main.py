from flask import Flask, send_from_directory
app = Flask(__name__)


@app.route('/<path:path>')
def html(path):
    return send_from_directory('./', path)

@app.route('/lib/<path:path>')
def lib(path):
    return send_from_directory('./lib', path)

@app.route('/data/<path:path>')
def data(path):
    return send_from_directory('./data', path)

if __name__ == "__main__":
    app.run()
