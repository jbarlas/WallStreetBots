from flask import Flask, jsonify
from flask_cors import CORS
from submissions import add_submissions_by_day, submission_history, recent_submission
from praw_utils import comment_stream

app = Flask(__name__)
CORS(app)


@app.route('/')
def test():
    return 'Flask server running!'

@app.route('/add-submissions/<day_utc>')
def submissions_by_day(day_utc):
    """
    Gather top submissions for 24hr after given utc in unix format

    Parameters:
    -----------
    day_utc: str;
        start time in utc (read as str, cast as int)

    Returns: 
    -------
    {
        data: Submission[],
        next_utc: number # utc for following day
    }
    """
    return add_submissions_by_day(int(day_utc)), 200

@app.route('/recent-submission')
def recent():
    return jsonify(recent_submission()), 200

@app.route('/submission-history')
def gather_submission_history():
    return jsonify(submission_history()), 200

@app.route('/update-comments')
def update_comments():
    comment_stream()
    return {'status': 'success'}, 200

@app.route('/get-submission/<id>')
def get_submission(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)