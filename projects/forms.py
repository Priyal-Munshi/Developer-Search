from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input', 'placeholder': 'Add title'})
        # self.fields['title'].widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your order',
            'body': 'Add a comment with your code'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input', 'placeholder': 'Add title'}) 
       
