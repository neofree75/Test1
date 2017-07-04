from django import forms

from .models import Poziadavka_ee

class OdoslatForm(forms.ModelForm):
	eic = forms.CharField(max_length=16,label='EIC:',
                                 widget=forms.TextInput(
                                 attrs={'class': 'form-control'}),
                                 required=False)
	datum_zaciatku_zmluvy_zmeny = forms.CharField(label='Dátum zmeny dodávateľa od:',
                                 widget=forms.TextInput(
                                 attrs={'class': 'form-control'}
                                 ),required=False)
	id_z_pds_it = forms.CharField(max_length=16,label='Číslo OP z PDS:',
                                 widget=forms.TextInput(
                                 attrs={'class': 'form-control'}),
                                 required=False)
	class Meta:
		model = Poziadavka_ee
		fields = ('eic','datum_zaciatku_zmluvy_zmeny','id_z_pds_it')