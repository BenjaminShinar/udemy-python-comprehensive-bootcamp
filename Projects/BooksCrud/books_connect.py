from sql_config import dbConfig
import pyodbc


class BookDB:

    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()

    def __del__(self):  #destructor
        self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, title, author, isbn):
        sql = ("INSERT INTO books(title, author, isbn) VALUES (?,?,?)")
        values = [title, author, isbn]
        self.cursor.execute(sql, values)
        self.con.commit()
        #messagebox.showinfo(title="Books Database", message = "New book added to database")

    def update(self, id, title, author, isbn):
        sql = (
            "UPDATE books SET title = ? , author = ?, isbn = ? WHERE id = ?")
        values = [id, title, author, isbn]
        self.cursor.execute(sql, values)
        self.con.commit()
        #messagebox.showinfo(title="Books Database", message="Book updated")

    def delete(self, id):
        sql = ("DELETE FROM books WHERE id = ?")
        values = [id]
        self.cursor.execute(sql, values)
        self.con.commit()
        #messagebox.showinfo(title="Books Database", message="Book deleted")


def addBook(db: BookDB):
    title = input("book title")
    author = input("book author")
    isbn = int(input("book isbn"))
    db.insert(title, title, author, isbn)


def main():
    print("starting")
    print(dbConfig)
    con = pyodbc.connect(**dbConfig)  #pass all contents a
    print(con)
    db = BookDB(con)
    i = int(input("choose\n"))
    while i != 0:
        if i == 1:
            print("read")
            print(db.view())
        elif i == 2:
            print("add")
            addBook(db)
        print(i)
        i = int(input("choose\n"))


if __name__ == "__main__":
    main()