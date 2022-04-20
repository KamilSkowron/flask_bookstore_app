from ksiegarnia import app, render_template, db, api, Resource, fields
from ksiegarnia.forms import AddItemForm, EditItemForm, EditBookForm, DeleteBookForm, SearchForm
from ksiegarnia.models import BookModel
from flask import jsonify, request, redirect, url_for, flash
import requests
from ksiegarnia.functions import import_data
import json

BASE = "http://127.0.0.1:5000/"


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/import', methods=['GET', 'POST'])
def import_page():
    if request.method == "POST":
        # Import Books Logic
        look = request.form['text'].replace(" ", "-")
        url = 'https://www.googleapis.com/books/v1/volumes?q='
        response = requests.get(url+look)
        dict = response.json()
        import_data(dict)
        flash(f'Sukces! Zaimportowałeś książki do repozytorium!',
              category='success')

        return render_template('import.html')

    if request.method == "GET":
        books = BookModel.query
        return render_template('import.html', books=books)


@app.route('/base_books', methods=['GET', 'POST'])
def base_books():
    edit_form = EditBookForm()
    delete_form = DeleteBookForm()
    form = SearchForm()
    books = BookModel.query

    if request.method == "POST":

        # Search Book Logic
        if form.is_submitted() and request.form.get('edit_book') == None and request.form.get('delete_book') == None:
            t = "%" + str(form.title.data) + "%"
            a = "%" + str(form.authors.data) + "%"
            po = form.publishedDateOD.data
            if form.publishedDateOD.data == "":
                po = 0
            pd = form.publishedDateDO.data
            if form.publishedDateDO.data == "":
                pd = float("inf")
            pl = "%" + str(form.language.data) + "%"

            books = BookModel.query.filter(
                BookModel.title.like(t),
                BookModel.authors.like(a),
                BookModel.language.like(pl),
                BookModel.publishedDate >= po,
                BookModel.publishedDate <= pd
            ).all()

            print(books)
            return render_template('base_books.html',
                                   form=form,
                                   books=books,
                                   edit_form=edit_form,
                                   delete_form=delete_form)

        # Edit Book Logic
        if edit_form.validate_on_submit() and request.form.get('edit_book'):
            edit_book = request.form.get('edit_book')

            return redirect(url_for('edit_book_page', book_id=edit_book))

        # Delete Book Logic
        if delete_form.validate_on_submit() and request.form.get('delete_book'):
            delete_book = request.form.get('delete_book')
            BookModel.query.filter_by(id=delete_book).delete()
            db.session.commit()

        return redirect(url_for("base_books"))

    if request.method == "GET":
        books = BookModel.query
        return render_template('base_books.html',
                               books=books,
                               edit_form=edit_form,
                               delete_form=delete_form,
                               form=form)


@app.route('/add_new', methods=['GET', 'POST'])
def add_book_page():
    form = AddItemForm()
    if form.validate_on_submit():
        book_to_add = BookModel(title=form.title.data,
                                authors=form.authors.data,
                                publishedDate=form.publishedDate.data,
                                identifier=form.identifier.data,
                                pageCount=form.pageCount.data,
                                imageLinks=form.imageLinks.data,
                                language=form.language.data)

        db.session.add(book_to_add)
        db.session.commit()
        flash(f'Sukces! Dodałeś nową książkę do repozytorium!',
              category='success')
        return redirect(url_for("base_books"))
    return render_template('add_new.html', form=form)


@app.route('/edit_book/<book_id>', methods=['GET', 'POST'])
def edit_book_page(book_id):
    BookModel.query.filter_by(id=book_id).delete()
    form = EditItemForm()
    if form.validate_on_submit():
        book_to_add = BookModel(id=book_id,
                                title=form.title.data,
                                authors=form.authors.data,
                                publishedDate=form.publishedDate.data,
                                identifier=form.identifier.data,
                                pageCount=form.pageCount.data,
                                imageLinks=form.imageLinks.data,
                                language=form.language.data)

        db.session.add(book_to_add)
        db.session.commit()
        flash(f'Sukces! Edytowałeś książkę z repozytorium!', category='success')
        return redirect(url_for("base_books"))
    return render_template('edit_book.html', form=form)

#-------------------------- Api ------------------------ #


@api.route('/books_api/')
class Books(Resource):
    def get(self):
        users = BookModel.query.all()
        return jsonify(users)


class BookSearch(Resource):
    def get(self, search_term):
        results = BookModel.query.filter(BookModel.title.like(
            '%'+search_term+'%')).all()

        return jsonify(results)
        # serialize and return items...


api.add_resource(BookSearch, '/books_api/search/<search_term>')

