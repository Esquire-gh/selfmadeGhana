from django import forms
from .models import Comment, Subscriber

class CommentForm(forms.ModelForm):
	message = forms.CharField( widget = forms.Textarea(attrs={'class': 'form-control comment-form-input', 
				'placeholder':'Add Your Comment:', 'required':'true', 'cols':3, 'rows':3
				}), label='')
	class Meta:
		model = Comment
		fields = ('message',)
        

class ContactForm(forms.Form):
	sender = forms.EmailField(max_length = 225, required =True, label = '',
		widget = forms.EmailInput(attrs={'class': 'form-control contact_form_element', 'placeholder':'Sender', 'required':'true'}))
	
	subject = forms.CharField(max_length = 100, required =True, label='',
		widget = forms.TextInput(attrs={'class': 'form-control contact_form_element', 'placeholder':'Subject', 'require':'true'}))
	
	message = forms.CharField(widget = forms.Textarea(attrs={
		'class': 'form-control contact_form_element text_area_input', 'placeholder':'Enter your Message', 'required':'true'
		}), 
		required =True, label='')


class SubscriberForm(forms.ModelForm):
	email = forms.EmailField(max_length = 225, required =True, label = '',
		widget = forms.EmailInput(attrs={'class': 'form-control contact_form_element', 'placeholder':'Sender', 'required':'true'}))

	class Meta:
		model = Subscriber
		fields = ('email',)