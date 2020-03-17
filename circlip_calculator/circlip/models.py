# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class CirclipModel(models.Model):
    inner_diameters =models.DecimalField(max_digits=4, decimal_places=2)
    tooling_diameters =models.DecimalField(max_digits=4, decimal_places=2)
    circlip_width =models.DecimalField(max_digits=4, decimal_places=2)
    circlip_thickness =models.DecimalField(max_digits=4, decimal_places=2)
    circlip_mises =models.DecimalField(max_digits=8, decimal_places=2, null=True)
    circlip_deformed_diameters =models.DecimalField(max_digits=4, decimal_places=2, null=True)
    tip_type = models.IntegerField()
    datetime = models.DateField(auto_now=True)

