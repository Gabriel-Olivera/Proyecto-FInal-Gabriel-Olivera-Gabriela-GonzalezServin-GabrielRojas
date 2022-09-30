from django import forms


class CrearPostForm(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=100,
        min_length=5,
    )
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
