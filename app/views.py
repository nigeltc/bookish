from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import Location, Book, Author

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

class BookView(ModelView):
    datamodel = SQLAInterface(Book)
    list_columns = ["title", "authors", "location"]

class LocationView(ModelView):
    datamodel = SQLAInterface(Location)
    related_views = [BookView]
    

class AuthorView(ModelView):
    datamodel = SQLAInterface(Author)
    related_views= [BookView]
    list_columns = ["display_name", "books"]




"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
appbuilder.add_view(BookView, "Books", icon="fa-folder-open-o", category="Library")
appbuilder.add_view(AuthorView, "Authors", icon="fa-folder-open-o", category="Library")
appbuilder.add_view(LocationView, "Locations", icon="fa-folder-open-o", category="Library")
