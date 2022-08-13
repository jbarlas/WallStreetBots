import requests

from enum import Enum


START_DATE = 1577854800 # January 1 2020

class PushshiftUrl(Enum):
    SUBMISSION = "https://api.pushshift.io/reddit/search/submission"
    COMMENT = "https://api.pushshift.io/reddit/comment/search"
    SUBMISSION_COMMENT = "/reddit/submission/comment_ids/" # {base36-submission-id}

class Query:
    params = {}
    empty_query = {
            "ids": [], # Get specific submissions via their ids
            "q": "", # Search term. Will search ALL possible fields
            "q:not": "", # Exclude search term. Will exclude these terms
            "title": "", # Searches the title field only
            "size": 500, # Number of results to return
            "fields": [], # One return specific fields (comma delimited)
            "sort": "", # Sort results in a specific order
            "sort_type": "", # Sort by a specific attribute
            "subreddit": "", # Restrict to a specific subreddit
            "after": "", # return results after this date
            "before": "", # return results before this date
            "score": "", # Restrict results based on score; Integer or > x or < x (i.e. score=> 100 or score=< 25)
            "num_comments": "", # Restrict results based on number of comments; Integer or > x or < x (i.e. score=> 100 or score=< 25)
        }

    def __init__(self, url : PushshiftUrl):
        self.base_url = str(url.value)
        self.query = self.empty_query

    def set_base_url(self, url : PushshiftUrl):
        self.base_url = str(url.value)
    
    def set_query(self, query : dict):
        for (key, value) in query.items():
            if key in self.query:
                self.query[key] = value
        self.gen_params()
    
    def clear_query(self):
        self.query = self.empty_query
        self.gen_params()

    def gen_params(self):
        self.params = {key:value for (key, value) in self.query.items() if value}
        list_params = ["id"", fields"]
        for p in list_params:
            if p in self.params:
                self.params[p] = ",".join(self.params[p])



class Pushshift:
    def __init__(self, url : PushshiftUrl):
        self.query = Query(url)

    def get_query(self):
        return self.query.query

    def set_query(self, **kwargs):
        self.query.set_query(kwargs)

    def clear_query(self):
        self.query.clear_query()

    def gen_response(self):
        resp = requests.get(self.query.base_url, params=self.query.params)
        if resp.status_code == 200:
            return resp.json()['data']
    
    def gen_submission_ids(self):
        self.set_query(fields=["id"])
        resp_json = self.gen_response()
        self.set_query(fields=[])
        return [value for submission in resp_json for (_, value) in submission.items()]



