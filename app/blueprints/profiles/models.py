from utils.extenisons import db

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String(80), unique=True, nullable=False)
    display_name = db.Column(db.String(40), nullable=False)
    sub = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255))  
    followers = db.Column(db.Integer())

    def __init__(self, spotify_id, followers, display_name, sub=False, image_url=None):
        self.spotify_id = spotify_id
        self.display_name = display_name
        self.sub = sub
        self.image_url = image_url
        self.followers = followers
    
'''
'display_name': 'maciek wojdyna', 'external_urls': {'spotify': 'https://open.spotify.com/user/21lyrpw25xvrgdxnq25q33hky'}, 'href': 'https://api.spotify.com/v1/users/21lyrpw25xvrgdxnq25q33hky', 'id': '21lyrpw25xvrgdxnq25q33hky', 'images': [{'url': 'https://i.scdn.co/image/ab67757000003b82e52ae25ffe35814cbfcbd08d', 'height': 64, 'width': 64}, {'url': 'https://i.scdn.co/image/ab6775700000ee85e52ae25ffe35814cbfcbd08d', 'height': 300, 'width': 300}], 'type': 'user', 'uri': 'spotify:user:21lyrpw25xvrgdxnq25q33hky', 'followers': {'href': None, 'total': 53}, 'country': 'PL', 'product': 'premium', 'explicit_content': {'filter_enabled': False, 'filter_locked': False}, 'email': 'wojdynam@wit.edu.pl'}
'''