from django import forms

from pagedown.widgets import PagedownWidget

from .models import Portofol

class PortoForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget) # widget untuk form date publish

	class Meta:
		model = Portofol
		fields = [
			"title",
			"content",
			"image",
			]
