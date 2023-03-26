import wtforms as wtforms
from wtforms.validators import DataRequired

from models import Entry


class EntryForm(wtforms.Form):
    title = wtforms.StringField('Title', validators=[DataRequired()])
    content = wtforms.TextAreaField('Content', validators=[DataRequired()])
    status = wtforms.SelectField('Status',
                                 choices=((Entry.STATUS_PUBLIC, 'Public'),
                                          (Entry.STATUS_DRAFT, 'Draft')),
                                 coerce=int)

    def save_entry(self, entry):
        self.populate_obj(entry)
        entry.generate_slug()
        return entry
