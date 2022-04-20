from matplotlib.pyplot import title
from ksiegarnia import db
from ksiegarnia.models import BookModel


def import_data(dict):
    if 'items' in dict:
        for v in dict['items']:
            exists = db.session.query(db.exists().where(
                BookModel.book_api_id == v['id'])).scalar()

            if exists:
                continue

            else:
                book_record = {}

                if "title" in v['volumeInfo']:
                    book_record["title"] = v['volumeInfo']['title']
                else:
                    book_record["title"] = ""

                if "authors" in v['volumeInfo']:
                    book_record["authors"] = v['volumeInfo']['authors'][0]
                else:
                    book_record["authors"] = ""

                if "publishedDate" in v['volumeInfo']:
                    book_record["publishedDate"] = int(
                        v['volumeInfo']['publishedDate'][:4])
                else:
                    book_record["publishedDate"] = 0

                if "industryIdentifiers" in v['volumeInfo']:
                    book_record["identifier"] = v['volumeInfo']['industryIdentifiers'][0]['identifier']
                else:
                    book_record["identifier"] = ""

                if "pageCount" in v['volumeInfo']:
                    book_record["pageCount"] = str(
                        v['volumeInfo']['pageCount'])
                else:
                    book_record["pageCount"] = ""

                if "imageLinks" in v['volumeInfo']:
                    book_record["imageLinks"] = v['volumeInfo']['imageLinks']['thumbnail']
                else:
                    book_record["imageLinks"] = ""

                if "language" in v['volumeInfo']:
                    book_record["language"] = v['volumeInfo']['language']
                else:
                    book_record["language"] = ""

                book_record["book_api_id"] = v['id']

                book_to_add = BookModel(title=book_record["title"],
                                        authors=book_record["authors"],
                                        publishedDate=book_record["publishedDate"],
                                        identifier=book_record["identifier"],
                                        pageCount=book_record["pageCount"],
                                        imageLinks=book_record["imageLinks"],
                                        language=book_record["language"],
                                        book_api_id=book_record["book_api_id"],
                                        )
                db.session.add(book_to_add)
                db.session.commit()
