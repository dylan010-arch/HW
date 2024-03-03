from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

    def clean_email(self):
        email= self.cleaned_data['email']
        if not " example.com " in email:
            raise forms.ValidationError("Используйте свой адрес электронной почты")
        return email