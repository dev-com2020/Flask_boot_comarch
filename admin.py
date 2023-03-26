from flask import g
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import Entry, Tag, User


class AdminAuth(object):
    def is_accessible(self):
        return g.user.is_authenticated and g.user.is_admin()


class BlogFileAdmin(AdminAuth, FileAdmin):
    pass


class BaseModelView(AdminAuth, ModelView):
    pass


class EntryModelView(ModelView):
    _status_choices = [(choice, label) for choice, label in [
        (Entry.STATUS_PUBLIC, 'Public'),
        (Entry.STATUS_DRAFT, 'Draft'),
        (Entry.STATUS_DELETED, 'Deleted'),
    ]]

    column_choices = {'status': _status_choices}

    column_list = ('title', 'status', 'tease', 'tag_list', 'created_timestamp')
    column_searchable_list = ('title', 'content')
    column_filters = ('created_timestamp', 'status')


admin = Admin(app, name='FlaskApp', template_mode='bootstrap3')
admin.add_view(EntryModelView(Entry, db.session))
admin.add_view(ModelView(Tag, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(BlogFileAdmin(app.config['STATIC_DIR']))
