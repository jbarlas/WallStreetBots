"""Logic for generating comment data"""

from firebase import comments
from datetime import datetime, timedelta

def get_comments():
    time_offset = datetime.timestamp(datetime.now() - timedelta(minutes=1))
    return [comment.to_dict() for comment in comments.where(u'created_utc', u'>=', time_offset).stream()]