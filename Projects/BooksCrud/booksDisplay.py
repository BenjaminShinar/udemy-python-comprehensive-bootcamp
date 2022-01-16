from glob import glob
from tkinter import Tk
#Button, Label, Scrollbar, Listbox, StringVar, Entry, END
from tkinter import ttk, StringVar
import tkinter
from turtle import up
from sql_config import dbConfig
#import pypyodbc


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


dbBooks = [(11, "bells", "hemingway", 55), (12, "bells2", "heminzgway", 56)]


def makeLabel(app, title, r, c, stick):
    """create a Title Widget"""
    title_label = ttk.Label(app,
                            text=title,
                            background="light green",
                            font=("TKDfaultFont", 16))
    title_label.grid(row=r, column=c, sticky=stick)
    app.elements[title] = title


def makeEntry(app, prefix, r, c, stick):
    """create an Entry Widget"""
    entry_str = StringVar()
    entry_widget = ttk.Entry(app, width=24, textvariable=entry_str)
    entry_widget.grid(row=r, column=c, stick=stick)
    app.elements[f"{prefix}_text"] = entry_str
    app.elements[f"{prefix}_entry"] = entry_widget


def makeButton(app, btnCaption, r, c, bgc, fgc, action):
    """create a Button Widget"""
    btn = tkinter.Button(app,
                         text=btnCaption,
                         bg=bgc,
                         fg=fgc,
                         font="helvetica 10 bold",
                         command=action)
    btn.grid(row=r, column=c)
    app.elements[f"btn_{btnCaption}"] = btn


def setupListBox(app):
    """the scroll bar and the list itself"""
    scroll_bar = tkinter.Scrollbar(app)
    scroll_bar.grid(row=1, column=8, rowspan=14, sticky=tkinter.W)

    list_box = tkinter.Listbox(app,
                               height=16,
                               width=40,
                               font="helvetica 13",
                               bg="light blue",
                               yscrollcommand=scroll_bar.set)

    list_box.grid(row=3,
                  column=1,
                  columnspan=14,
                  sticky=tkinter.W + tkinter.E,
                  pady=40,
                  padx=15)

    scroll_bar.configure(command=list_box.yview)

    app.list_box = list_box
    app.elements["scroll_bar"] = scroll_bar


def setup(app):
    """create Widgets"""
    makeLabel(app, "Book Title", 0, 0, tkinter.W)
    makeEntry(app, "book_title", 0, 1, tkinter.W)
    makeLabel(app, "Book Author", 0, 2, tkinter.W)
    makeEntry(app, "book_author", 0, 3, tkinter.W)
    makeLabel(app, "Book ISBN", 0, 4, tkinter.W)
    makeEntry(app, "book_isbn", 0, 5, tkinter.W)

    makeButton(app, "Add Book", 0, 6, "blue", "white", lambda: addBook(app))

    makeButton(app, "View All Books", 15, 1, "red", "white",
               lambda: view_records(app))
    makeButton(app, "Clear Screen", 15, 2, "maroon", "white",
               lambda: clear_screen(app))
    makeButton(app, "Exit App", 15, 3, "black", "white", exit)
    makeButton(app, "Modify Book", 15, 4, "purple", "white",
               lambda: update_records(app))
    makeButton(app, "Delete Book", 15, 5, "red", "white",
               lambda: delete_records(app))

    setupListBox(app)


def get_delete_entry(app, el):
    """helper function"""
    v = app.elements[el].get()
    app.elements[el].delete(0, 'end')
    return v


def get_selected_row(event):
    app = root
    global selected_tuple  # reference a global variable
    index = app.list_box.curselction()[0]
    selected_tuple = app.list_box.get(index)

    def update(entry, value):
        entry.delete(0, 'end')
        entry.insert('end', value)

    update(app.elements["book_title_entry"], selected_tuple[1])
    update(app.elements["book_author_entry"], selected_tuple[2])
    update(app.elements["book_isbn_entry"], selected_tuple[3])


def delete_records(app):
    pass
    #db.delete(selected_tuple[0])
    #con.commit()


def addBook(app):

    title = get_delete_entry(app, "book_title_entry")
    author = get_delete_entry(app, "book_author_entry")
    isbn = get_delete_entry(app, "book_isbn_entry")
    dbBooks.append((title, author, isbn))
    #db.insert(title_text.get(), author_text.get(), isbn_text.get())
    app.list_box.delete(0, 'end')
    app.list_box.insert('end', (title, author, isbn))
    #con.commit()


def update_records(app):
    title = get_delete_entry(app, "book_title_entry")
    author = get_delete_entry(app, "book_author_entry")
    isbn = get_delete_entry(app, "book_isbn_entry")

    #db.update(selected_tuple[0], title, author,isbn)
    #con.commit()


def view_records(app):
    app.list_box.delete(0, 'end')
    for row in dbBooks:
        app.list_box.insert('end', row)


def clear_screen(app):
    app.list_box.delete(0, 'end')
    app.elements["book_title_entry"].delete(0, 'end')
    app.elements["book_author_entry"].delete(0, 'end')
    app.elements["book_isbn_entry"].delete(0, 'end')


def main():
    global root
    root = Tk()
    root.title("Books Display")
    root.configure(bg="light green")
    root.geometry("950x500")
    root.resizable(width=False, height=False)
    root.elements = dict()

    setup(root)

    # con = pypyodbc.connect(**dbConfig)  #pass all contents as parameters
    ##cursor = con.cursor()

    root.mainloop()


if __name__ == "__main__":
    main()