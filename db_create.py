from app import db
from models import BlogPost

# create the database and the  db tables
db.create_all()

# insert
db.session.add(BlogPost("Bad", "I\'m bad."))
db.session.add(BlogPost("Mad", "I\'m mad."))

# commit the changes
db.session.commit()