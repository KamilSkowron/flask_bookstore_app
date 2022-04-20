from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class AddItemForm(FlaskForm):
    title = StringField(label='Tytuł:', validators=[
                        DataRequired(), Length(min=2, max=30)])
    authors = StringField(label='Autor:', validators=[DataRequired()])
    publishedDate = IntegerField(
        label='Data publikacji:',
        validators=[DataRequired(), NumberRange(max=9999)])
    identifier = StringField(label='Indentyfikator:',
                             validators=[DataRequired()])
    pageCount = StringField(label='Liczba stron:', validators=[DataRequired()])
    imageLinks = StringField(label='Link do zdjęcia:',
                             validators=[DataRequired()])
    language = StringField(label='Język:', validators=[DataRequired()])
    submit = SubmitField(label='Dodaj książkę!')


class EditItemForm(FlaskForm):
    title = StringField(label='Tytuł:',
                        validators=[DataRequired(), Length(min=2, max=30)])
    authors = StringField(label='Autor:',
                          validators=[DataRequired()])
    publishedDate = IntegerField(label='Data publikacji:',
                                 validators=[DataRequired(), NumberRange(max=4)])
    identifier = StringField(label='Indentyfikator:',
                             validators=[DataRequired()])
    pageCount = StringField(label='Liczba stron:',
                            validators=[DataRequired()])
    imageLinks = StringField(label='Link do zdjęcia:',
                             validators=[DataRequired()])
    language = StringField(label='Język:',
                           validators=[DataRequired()])
    submit = SubmitField(label='Edytuj książkę!')


class EditBookForm(FlaskForm):
    submit = SubmitField(label="Edytuj książkę")


class DeleteBookForm(FlaskForm):
    submit = SubmitField(label="Usuń książkę")


class SearchForm(FlaskForm):
    title = StringField(label='Tytuł:')
    authors = StringField(label='Autor:')
    publishedDateOD = StringField(label='Od daty publikacji:')
    publishedDateDO = StringField(label='Do daty publikacji:')
    language = StringField(label='Język:')
    submit = SubmitField(label="Wyszukaj")
