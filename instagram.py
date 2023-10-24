from instagrapi import Client

class InstagramAccount:

    def __init__(self, username, password):
        self.cl = Client()
        self.cl.delay_range = [1, 3]
        self.cl.login(username, password)
        self.media_id = None

    def changeMediaID(self, url):

        self.media_id = self.cl.media_id(self.cl.media_pk_from_url(url))

    def like_comment(self, commentID):

        self.cl.comment_like(commentID)

    def GetComments(self):
        if not self.media_id:
            return []
        
        return self.cl.media_comments(self.media_id)

    def RespondToComment(self, message, commentID):

        self.cl.media_comment(self.media_id, message, replied_to_comment_id=commentID)
