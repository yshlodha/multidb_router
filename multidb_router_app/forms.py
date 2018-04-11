from django import forms

from .data_handler import  get_user_dbs

PRODUCT_CATEGORY = (('sports', 'sports'),
                    ('electronics', 'electronics'),
                    ('fashion', 'fashion'))

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=100,
                               widget=forms.PasswordInput())

    def clean(self):
        """
        """
        self.cleaned_data = super(LoginForm, self).clean()
        try:
            user_name = self.cleaned_data['username']
        except KeyError:
            self._errors['username'] = self.error_class(["This field can't be empty."])
        try:
            password = self.cleaned_data['password']
        except KeyError:
            self._errors['password'] = self.error_class(["This field can't be empty."])

        return self.cleaned_data

class AddProductForm(forms.Form):
    """
    """
    product_name = forms.CharField(label="Product Name", max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'product_name'}))
    product_category = forms.ChoiceField(choices=PRODUCT_CATEGORY, label="Product Category", initial='', widget=forms.Select(), required=True)
    database = forms.ChoiceField(choices=[], label="Select Database")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['database'].choices = [(x, x) for x in get_user_dbs(self.request.user)]

    def clean(self):
        """
        :return:
        """
        self.cleaned_data = super(AddProductForm, self).clean()
        try:
            product_name = self.cleaned_data['product_name']
        except KeyError:
            self._errors['product_name'] = self.error_class(["This field can't be empty."])
        return self.cleaned_data


class AdminAddUserProductForm(AddProductForm):
    """
    """

    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        self.request = kwargs.pop('request', None)
        dbuser = kwargs.pop('dbuser', None)
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['database'].choices = [(x, x) for x in get_user_dbs(dbuser.user)]