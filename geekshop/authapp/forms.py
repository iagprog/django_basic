from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta :
        model = ShopUser
        fields = ('username' , 'password')
    def __init__ (self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("You are too young!")
        return data

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "password1", "password2", "email", "age", "avatar")
