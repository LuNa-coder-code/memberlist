#forms.py
from django import forms
from memberlist.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
      }
