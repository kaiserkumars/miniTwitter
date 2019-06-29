from django import forms
from django.forms import ModelForm

from .models import TwitterData



class DateInput(forms.DateInput):
	input_type = 'date'

class TwitterDataForm(ModelForm):

	class Meta:
		model = TwitterData
		fields = ['screen_name', 'org_name', 'tweet','tweet_id','date','profile_url']
		widgets = {
			'date': DateInput(),
		}

# class DateForm(forms.Form):
# 	date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])