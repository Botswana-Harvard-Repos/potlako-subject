from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import ExitFromStudy


class ExitFromStudyForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    # form_validator_cls

    class Meta:
        model = ExitFromStudy
        fields = '__all__'
