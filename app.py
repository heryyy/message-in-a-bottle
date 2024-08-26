from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def lyrics():
    return render_template('lyrics.html', title="")

if __name__ == '__main__':
    app.run(debug=True)