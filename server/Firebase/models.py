
class FirebaseSubmission:        
    id = ""
    title = ""
    selftext = ""
    comment_ids = ""
    url = ""
    created_utc = ""
    info = {}

    def __init__(self, submission):
        self.from_praw(submission)

    def to_dict(self):
        return self.__dict__
    
    def from_praw(self, submission):
        self.id = submission.id
        self.title = submission.title
        self.selftext = submission.selftext
        self.url = submission.url
        self.created_utc = submission.created_utc

            
class FirebaseComment:
    # refactor to look like submission!!
    def __init__(self, id : str, body : str, **kwargs):
        self.id = id
        self.body = body
        self.info = {}
        for (arg, val) in kwargs.items():
            self.info.update({arg: val})

    def to_dict(self):
        dict = {}
        for attribute in self.__dict__.keys():
            if attribute[:2] != '__':
                value = getattr(self, attribute)
                if not callable(value):
                    dict.update({attribute: value})
        return dict