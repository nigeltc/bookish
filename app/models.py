from flask_appbuilder import Model
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who

"""

assoc_book_author = Table("book_author",
                          Model.metadata,
                          Column("id", Integer, primary_key=True),
                          Column("book_id", Integer, ForeignKey("book.id")),
                          Column("author_id", Integer, ForeignKey("author.id")))

class Location(Model):
    """
    A location is a place where books are stored - a box, a bookshelf, etc
    A location contains many books
    A book can only be in one location
    """
    id = Column(Integer, primary_key=True)
    description = Column(String(128), index=True, nullable=False)

    def __repr__(self):
        return self.description


class Book(Model):
    """
    A book is a book!
    A book can be in a single location
    A book can have many authors
    """
    id = Column(Integer, primary_key=True)
    title = Column(String(128), index=True, nullable=False)
    location_id = Column(Integer, ForeignKey("location.id"), nullable=False)
    location = relationship("Location")
    authors = relationship("Author", secondary=assoc_book_author, backref="author")

    def __repr__(self):
        return self.title


class Author(Model):
    """
    A book can have many authors
    An author can write many books
    """
    id = Column(Integer, primary_key=True)
    last_name = Column(String(128), index=True, nullable=False)
    first_name = Column(String(128), index=True, nullable=False)
    display_name = Column(String(128), index=True, nullable=False)
    books = relationship("Book", secondary=assoc_book_author, backref="book")

    def __repr__(self):
        return self.display_name


