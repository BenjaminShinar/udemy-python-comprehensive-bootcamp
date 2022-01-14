from tkinter import Tk
#Button, Label, Scrollbar, Listbox, StringVar, Entry, END
from tkinter import ttk, StringVar
import tkinter


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

    app.elements["list_box"] = list_box
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

    makeButton(app, "View All Books", 15, 1, "red", "white", lambda a: (a))
    makeButton(app, "Clear", 15, 2, "maroon", "white", lambda: ())
    makeButton(app, "Exit App", 15, 3, "black", "white", lambda a: (a))
    makeButton(app, "Modify Book", 15, 4, "purple", "white", lambda a: (a))
    makeButton(app, "Delete Book", 15, 5, "red", "white", lambda a: (a))

    setupListBox(app)


def addBook(app):
    print(app.elements)
    pass


def main():
    root = Tk()
    root.title("Books Display")
    root.configure(bg="light green")
    root.geometry("950x500")
    root.resizable(width=False, height=False)
    root.elements = dict()

    setup(root)

    root.mainloop()


if __name__ == "__main__":
    main()