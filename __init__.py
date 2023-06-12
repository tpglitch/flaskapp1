from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = '123savesum4me'

@app.route('/')
def home():
  return jsonify({"Message":"Teating"})

if __name__ == '__main__':
  app.run()
