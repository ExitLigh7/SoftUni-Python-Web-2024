from django import forms
from Exam_27_10.authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['info', 'image_url']
        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "pets_number": "Pets Number:",
        }

    def __init__(self, *args, **kwargs):
        super(AuthorCreateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name...'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name...'})
        self.fields['passcode'].widget = forms.PasswordInput()
        self.fields['passcode'].widget.attrs.update({'placeholder': 'Enter 6 digits...'})
        self.fields['pets_number'].widget.attrs.update({'placeholder': 'Enter the number of your pets...'})

class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['passcode']
        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "pets_number": "Pets Number:",
            "image_url": "Profile Image URL:",
        }
