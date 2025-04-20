import datetime
from datetime import date
from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Car, Service

class CarForm(forms.ModelForm):
    dibiayai_bank = forms.BooleanField(
        required=False, 
        label='Dibiayai oleh Bank?')

    class Meta:
        model = Car # Link the car model
        fields = ['merk', 'model', 'tahun', 'harga_dasar', 'pinjaman_bank', 'suku_bunga']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Hide the loan if dibiayai_bank is true
        if not self.data.get('dibiayai_bank'):
            self.fields['pinjaman_bank'].widget = forms.HiddenInput()
            self.fields['suku_bunga'].widget = forms.HiddenInput()

class ServiceForm(forms.ModelForm):
    tanggal = forms.DateField(required=True,
                              widget=SelectDateWidget(years=range(datetime.date.today().year + 10, datetime.date.today().year + 1))
                              )
    deskripsi = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'cols': 40,
        'style': 'resize: none;'
    }), required=True)
    biaya = forms.DecimalField(max_digits=12, decimal_places=2, required=True)

    class Meta:
        model = Service
        fields = ['tanggal', 'deskripsi', 'biaya']  # Include the car selection field

