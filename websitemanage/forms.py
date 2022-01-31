from django import forms


class UserDeactivateForm(forms.Form):
    """
    Form that provides a checkbox that signals deactivation.
    """
    deactivate = forms.BooleanField(required=True)


class UserDeleteForm(forms.Form):
    """
    Form that provides a checkbox that signals deletion.
    """
    delete = forms.BooleanField(required=True)
