from django import forms
from .models import Terapia


class CrudForm(forms.ModelForm):

		class Meta:
			model = Terapia

			fields = [
				'id_terapia',
				'nombre',
				'descripcion',
				'limite',
				'estado',
			]

			labels = {
				'id_terapia': 'id_terapia',
				'nombre': 'nombre',
				'descripcion': 'descripcion',
				'limite': 'limite',
				'estado': 'estado',
			}

			widgets = {
				'id_terapia': forms.TextInput(attrs={'class':'form-control'}),
				'nombre': forms.TextInput(attrs={'class':'form-control'}),
				'descripcion': forms.TextInput(attrs={'class':'form-control'}),
				'limite': forms.TextInput(attrs={'class':'form-control'}),
				'estado': forms.Select(attrs={'class':'form-control','id':'Inputestado'}),
			}

