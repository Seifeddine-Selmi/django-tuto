#-*- coding: utf-8 -*
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ('author','slug', 'nb_views')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    from_email = forms.EmailField(label="Votre adresse mail")
    resend = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')

        if subject and message:
            if "pizza" in subject and "pizza" in message:
               # raise forms.ValidationError("Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !" )
              msg = "Vous parlez déjà de pizzas dans le sujet, n'en parlez plus dans le message !"
              self.add_error("message", msg)

        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK


class NewContactForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()



class NewDocumentForm(forms.Form):
    name = forms.CharField()
    file = forms.FileField()