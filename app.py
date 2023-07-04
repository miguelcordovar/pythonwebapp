from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def index_get():
  return render_template("base.html")

if __name__ == '__main__':
    app.run()
