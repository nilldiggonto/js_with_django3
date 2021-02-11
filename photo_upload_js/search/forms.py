from django import forms
from .models import PostUp


class PostUpForm(forms.ModelForm):
    # image= forms.ImageField(widget= forms.ImageField
    #                        (attrs={'class':'some_class','id':'id_image'}))
    class Meta:
        model = PostUp
        fields = ('image','title','content')
    
    def __init__(self, *args, **kwargs):
        super(PostUpForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs = {
            'id': 'id_image',
            'class': 'myCustomClass',
            'name': 'myCustomName',
            'placeholder': 'myCustomPlaceholder'}