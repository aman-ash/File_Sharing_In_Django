from django import forms
from Upload.models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title', 'purpose', 'files']
