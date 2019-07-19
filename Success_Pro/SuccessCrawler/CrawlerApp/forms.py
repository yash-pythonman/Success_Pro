from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Enter your url like: https://www.success4.us','size':50}))
    depth = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Depth no. like: 1'}))