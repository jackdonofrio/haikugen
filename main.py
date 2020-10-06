from flask import Flask, render_template
from haiku import Haiku

app = Flask(__name__)

@app.route('/')
def main():
    haiku = Haiku()
    return render_template(
        'index.html',
        line_1=haiku.line_generator(),
        line_2=haiku.line_generator(7),
        line_3=haiku.line_generator()
    )

if __name__ == '__main__':
    app.run(debug=True)