from django import forms

class TodoListForm(forms.Form):
    
    text= forms.CharField(max_length=45,required=True,
        widget=forms.TextInput(
            attrs={'id':'field','placeholder':'Type Here'}))

