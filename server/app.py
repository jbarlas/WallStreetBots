from flask import Flask
from routes.submissions import add_submissions
from PRAW.praw_utils import comment_stream

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add-submissions')
def submissions():
    return add_submissions(), 200

@app.route('/update-comments')
def update_comments():
    comment_stream()
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(debug=True)