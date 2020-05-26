from project import db
from project.models import BlogPost

# create the database and the  db tables
# db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good.", 1))
db.session.add(BlogPost("Well", "I\'m well.", 1))
db.session.add(BlogPost("Flask", "discover_flask_dev", 2))
db.session.add(BlogPost("postgres", "set up local postgres", 3))

# commit the changes
db.session.commit()