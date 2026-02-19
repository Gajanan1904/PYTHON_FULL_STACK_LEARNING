# add_category() --> add books category
# add_book() --> add new book
# borrow_book() --> borrow book
# update_borrow() --> update borrow date
# search_by_date() --> find borrowed books by date
# category_report() --> count borrowed books per category
# set_limit() --> set monthly borrow limit
# limit_alert() --> check if limit exceed

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# database connection
engine = create_engine("sqlite:///SampleProject.db")

# base class
Base = declarative_base()

# session creation
Session = sessionmaker(bind=engine)
session = Session()

# ---------------- CATEGORY TABLE ----------------
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="category")


# ---------------- BOOK TABLE ----------------
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="books")

    borrows = relationship("Borrow", back_populates="book")


# ---------------- BORROW TABLE ----------------
class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True)
    borrow_date = Column(String)

    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="borrows")


# ---------------- LIMIT TABLE ----------------
class Limit(Base):
    __tablename__ = "limits"
    id = Column(Integer, primary_key=True)
    month = Column(String)
    max_books = Column(Integer)
    
    def add_caterogy():
        name=input("category name:")
        session.add((Category(name=name)))
        session.commit()

    def add_book():
        tittle=input("book tittle:")
        author=input("author name:") 
        Category_id=int(input("category id:"))
        session.add(Book(title=title,author=author,Category_id=Category_id))
        session.commit()
        print("Book added")
        
    def borrow_book():
        book_id=int(input("BOOK ID: "))
        date=input("borrow date (YYYY-MM-DD)" )
        #create borrow record
        session.add(Borrow(book_id=book_id,borrow_date=date))
        session.commit()
        print("Book Borrowed")
        
    def update_borrow():
        bid=int(input("Borrow id: "))
        #find borrow record
        borrow=session.query(Borrow).filter(Borrow.id==bid).first()
        if borrow:
            borrow.borrow_date=input("new date:")
            session.commit()
            print("Borrow update:")
        else:
            print("Borrow not found")
            
    def delete_borrow():
        bid=int(input("borrow id:"))
        borrow=session.query(Borrow).filter(Borrow.id==bid).first()
        if borrow:
            session.delete(borrow)
            session.commit()
            print("Borrow deleted")
        else:
            print("Borrow not found")
    def search_by_date():
        date=input("Enter Date: ")
        borrows=session.query(Borrow).filter(Borrow.borrow_date==date).all()
        for b in borrows:
            print(b.book.title,"-",b.borrow_date)
            
        
# create all tables
Base.metadata.create_all(engine)

print("Sample Project tables created successfully")
