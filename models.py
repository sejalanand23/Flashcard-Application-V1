from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'
  user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  username = db.Column(db.String(15), unique = True, nullable = False) 
  password = db.Column(db.String(15), nullable = False)
  deck_user = db.relationship('UserDeckRelation', backref = 'user')

class Card(db.Model):
  __tablename__ = 'card'
  card_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  card_front = db.Column(db.String(100), unique = True, nullable = False)
  card_back = db.Column(db.String(100), nullable = False)
  difficulty = db.Column(db.String(100))
  deck_card = db.relationship('CardDeckRelation', backref = 'card')

class Deck(db.Model):
  __tablename__ = 'deck'
  deck_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  deck_name = db.Column(db.String(100), nullable = False, unique = True)
  deck_total_score = db.Column(db.Integer)
  deck_average_score = db.Column(db.Float)
  card_deck = db.relationship('CardDeckRelation', backref = 'deck')
  user_deck = db.relationship('UserDeckRelation', backref = 'deck')
  
class UserDeckRelation(db.Model):
  __tablename__ = 'user_deck_relation'
  correct = db.Column(db.Integer)
  time = db.Column(db.String(100))
  quiz_count = db.Column(db.Integer)
  user_deck_relation_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  userUCR_foreignid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
  deckUCR_foreignid = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable = False)

class CardDeckRelation(db.Model):
  __tablename__ = 'card_deck_relation'
  card_deck_relation_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  cardCDR_foreignid = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable = False)
  deckCDR_foreignid = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable = False)