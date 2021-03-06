from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.forms import Form, EmailField
from django.db.transaction import atomic


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass


class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass


class SignUpForm(SubmittableForm, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

    email = EmailField(required=True)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        result = super().save(commit)
        if commit:
            result.save()
        return result


