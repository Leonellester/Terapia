from django import forms
from .models import Terapia


class CrudForm(forms.ModelForm):

		class Meta:
			model = Terapia

			fields = [
				'id_terapia',
				'id_paciente',
				'id_cita',
				'recibida',
			]

			labels = {
				'id_terapia': 'id_terapia',
				'id_paciente': 'id_paciente',
				'id_cita': 'id_cita',
				'recibida': 'recibida',
			}

			widgets = {
				'id_terapia': forms.TextInput(attrs={'class':'form-control'}),
				'id_paciente': forms.TextInput(attrs={'class':'form-control'}),
				'id_cita': forms.TextInput(attrs={'class':'form-control'}),
				'recibida': forms.TextInput(attrs={'class':'form-control'}),
			}

