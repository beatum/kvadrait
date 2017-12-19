from django.forms import ModelForm, forms
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['txt']
