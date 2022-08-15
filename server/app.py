from flask import Flask, jsonify
from flask_cors import CORS
from routes.submissions import add_submissions_by_day, submission_history, recent_submission
from PRAW.praw_utils import comment_stream

app = Flask(__name__)
CORS(app)


@app.route('/')
def test():
    return 'Flask server running!'

@app.route('/add-submissions/<day-utc>')
def submissions_by_day(day_utc):
    """
    Gather top submissions for 24hr after given utc in unix format
        Returns: 
            {
                data: Submission[],
                next_utc: number # utc for following day
            }
    """
    return add_submissions_by_day(day_utc), 200

@app.route('/recent-submission')
def recent():
    return recent_submission(), 200

@app.route('/submission-history')
def gather_submission_history():
    return jsonify(submission_history()), 200

@app.route('/update-comments')
def update_comments():
    comment_stream()
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(debug=True)