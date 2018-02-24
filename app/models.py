from . import db


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	userip = db.Column(db.String(20), unique = True, index = True)
	userdetails = db.relationship('Detail', backref='user')
	
	def __repr__(self):
		return '<User %r>' % self.userip


class Detail(db.Model):
	__tablename__ = 'details'
	id = db.Column(db.Integer, primary_key = True)
	detailtime =  db.Column(db.String(20))
	detailed = db.Column(db.String(20))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	
	def __repr__(self):
		return '<User %r>' % self.name
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

