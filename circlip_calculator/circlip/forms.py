# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, IntegerField, Textarea, CharField
from .models import CirclipModel
from django.utils.translation import ugettext_lazy as _


class CirclipForm(ModelForm):
    class Meta:
        model = CirclipModel
        fields = ['inner_diameters', 'tooling_diameters', 'circlip_width', 'circlip_thickness', 'tip_type']

    widgets = {
        'inner_diameters': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Dimensions'}),
        'tooling_diameters': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Dimensions'}),
        'circlip_width': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Dimensions'}),
        'circlip_thickness': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Dimensions'}),
        'tip_type': forms.Select(attrs={'class': 'form-control', })
    }
