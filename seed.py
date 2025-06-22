from app import db, Book, app

with app.app_context():
    books = [
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=10.99, stock=20),
        Book(title='1984', author='George Orwell', price=8.99, stock=15),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=12.50, stock=30),
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=10.99, stock=20),
        Book(title='1984', author='George Orwell', price=8.99, stock=15),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=12.50, stock=30),
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=10.99, stock=20),
        Book(title='1984', author='George Orwell', price=8.99, stock=15),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=12.50, stock=30),
         Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=10.99, stock=20),
        Book(title='1984', author='George Orwell', price=8.99, stock=15),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=12.50, stock=30),
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=10.99, stock=20),
        Book(title='1984', author='George Orwell', price=8.99, stock=15),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=12.50, stock=30),
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=10.99, stock=20),
        Book(title='1984', author='George Orwell', price=8.99, stock=15),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=12.50, stock=30),
    ]
    db.session.add_all(books)
    db.session.commit()
    print("Sample books added.")
