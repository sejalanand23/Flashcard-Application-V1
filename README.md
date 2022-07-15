# Flashcard Application with Flask

## Package Requirements
- Flask==2.0.1
- Flask-SQLAlchemy==2.5.1

## Files and Folder Structure
- `app.py` contains the application and controllers
- `models.py` contains all database models
- `database.sqlite3` is the database file
- `static` default `static` files folder. It serves at '/static' path.
- `templates` - Default flask templates folder

```python
├── app.py
├── models.py
├── database.sqllite3
├── static
│  └── home.jpeg
├── templates
│  ├── add_cards.html
│  ├── create_deck.html
│  ├── dashboard.html
│  ├── edit_deck.html
│  ├── home.html
│  ├── login.html
│  ├── quiz_ans.html
│  ├── quiz.html
│  ├── result.html
   └── signup.html
```
