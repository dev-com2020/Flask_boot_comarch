import wtforms as wtforms

from models import Entry

class EntryForm(wtforms.Form):
    title = wtforms.StringField('Title')
    content = wtforms.TextAreaField('Content')
    status = wtforms.SelectField('Status',
                                 choices=((Entry.STATUS_PUBLIC, 'Public'),
                                          (Entry.STATUS_DRAFT, 'Draft')),
                                 coerce=int)
