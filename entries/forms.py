import wtforms as wtforms
from wtforms.validators import DataRequired

from models import Entry, Tag


class TagField(wtforms.StringField):
    def _value(self):
        if self.data:
            return ', '.join([tag.name for tag in self.data])
        else:
            return ''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = self.get_tags_from_string(valuelist[0])
        else:
            self.data = []

    def get_tags_from_string(self, tag_string):
        raw_tags = tag_string.split(',')
        tag_names = [name.strip() for name in raw_tags if name.strip()]
        existing_tags = Tag.query.filter(Tag.name.in_(tag_names))
        new_names = set(tag_names) - set([t.name for t in existing_tags])
        new_tags = [Tag(name=name) for name in new_names]
        return list(existing_tags) + new_tags

class ImageForm(wtforms.Form):
    file = wtforms.FileField('Image File')



class EntryForm(wtforms.Form):
    title = wtforms.StringField('Title', validators=[DataRequired()])
    content = wtforms.TextAreaField('Content', validators=[DataRequired()])
    status = wtforms.SelectField('Status',
                                 choices=((Entry.STATUS_PUBLIC, 'Public'),
                                          (Entry.STATUS_DRAFT, 'Draft')),
                                 coerce=int)
    tags = TagField('Tags', description='Separate tags with commas.')

    def save_entry(self, entry):
        self.populate_obj(entry)
        entry.generate_slug()
        return entry
