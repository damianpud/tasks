import re
from datetime import date

from django.forms import CharField, DateField, Textarea, ModelForm
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit, Button

from blog_app.models import Post


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title'),
            ),
            'body',
            Row(
                Submit('submit', 'Dodaj post', css_class="btn-success"),
                Button('cancel', 'Anuluj', css_class="btn-outline-danger")
            ),
        )

    class Meta:
        model = Post
        exclude = ['author', 'slug', 'created', 'updated']

    title = CharField(validators=[capitalized_validator])
    body = CharField(widget=Textarea, required=True)

    def clean_description(self):
        initial = self.cleaned_data['body']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
        self.cleaned_data['body'] = cleaned
        return cleaned
