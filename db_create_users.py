from project import db
from project.models import User

# insert data
db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("mike", "mike@herman.com", "tell"))
'''try:
    num_rows_deleted = db.session.query(User).delete()
    print(num_rows_deleted)
    db.session.commit()
except:
    db.session.rollback()'''


# commit the changes
db.session.commit()