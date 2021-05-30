from app import db
from datetime import datetime


class CollectionMV(db.Model):
    __tablename__ = 'mv_collection'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text())
    path_image = db.Column(db.Text())
    image = db.Column(db.Text())
    is_exist = db.Column(db.Boolean, default=False, nullable=False)
    ord_publication = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum('A', 'D', 'E', name='status'), default='A',
                       nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
        return False

    def get_all():
        return CollectionMV.query.limit(60).all()

    def check(pk):
        data = CollectionMV.query.filter_by(id=pk).first()
        if data is None:
            return False
        data.is_exist = False if data.is_exist is True else True
        db.session.commit()
        return True
