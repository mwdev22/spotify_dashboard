from ..utils.extenisons import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spotify = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100))
    display_name = db.Column(db.String(40), nullable=False)
    subscription = db.Column(db.String(12), default='free')  
    followers = db.Column(db.Integer)

    def __init__(self,spotify,email,display_name,subscription,followers):
        self.spotify = spotify
        self.email = email
        self.display_name = display_name
        self.subscription = subscription
        self.followers = followers

    # number of users
    @staticmethod
    def count_users():
        return User.query.count()
    
    @staticmethod
    def average_followers():
        total_users = User.query.count()
        total_followers = db.session.query(db.func.sum(User.followers)).scalar()

        if total_users == 0:
            return 0  

        average_followers = total_followers // total_users
        return average_followers
    
