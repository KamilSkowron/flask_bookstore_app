from dataclasses import dataclass
from ksiegarnia import db


@dataclass
class BookModel(db.Model):
    id: int
    title: str
    authors: str
    publishedDate: int
    identifier: str
    pageCount: str
    imageLinks: str
    language: str
    book_api_id: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    authors = db.Column(db.String(100), nullable=False)
    publishedDate = db.Column(db.Integer, nullable=False)
    identifier = db.Column(db.String(100), nullable=False)
    pageCount = db.Column(db.String(10), nullable=False)
    imageLinks = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    book_api_id = db.Column(db.String(100))

    # def __repr__(self):
    #     return f"Book(title={self.title}, authors={self.authors}, publishedDate={self.publishedDate}, identifier={self.identifier}, pageCount={self.pageCount}, imageLinks={self.imageLinks}, language={self.language})"


db.create_all()
