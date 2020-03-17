# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CirclipForm
from .models import CirclipModel
from .restore import restore_data
import json
import os
import pandas as pd
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = pd.read_excel(os.path.join(BASE_DIR, 'circlip\\Latin_TABLE.xlsx'), header=0)
input_x = file[
    ['circlip_thickness', 'delta_outer_radius', 'delta_tooling_diameters', 'inner_diameters', 'tip_type']]
output_y_stress = file[['max_stress']]
output_y_diameters = file[['deformed_diameters']]


def forms(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CirclipForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # circlip_diameters = float(form.cleaned_data['inner_diameters'])
            # tooling_diameters = float(form.cleaned_data['tooling_diameters'])
            # delta_tooling_diameters = tooling_diameters - circlip_diameters
            # circlip_width = float(form.cleaned_data['circlip_width'])
            # circlip_thickness = float(form.cleaned_data['circlip_thickness'])
            # tip_type = int(form.cleaned_data['tip_type'])
            circlip_diameters = form.cleaned_data['inner_diameters']
            tooling_diameters = form.cleaned_data['tooling_diameters']
            delta_tooling_diameters = tooling_diameters - circlip_diameters
            circlip_width = form.cleaned_data['circlip_width']
            circlip_thickness = form.cleaned_data['circlip_thickness']
            tip_type = form.cleaned_data['tip_type']

            # Calculation
            data = [[circlip_thickness, circlip_width, delta_tooling_diameters, circlip_diameters, tip_type]]
            def_diameters = restore_data(data, input_x, output_y_diameters, 7)
            mises = restore_data(data, input_x, output_y_stress, 8)

            #xiuzheng
            if def_diameters < circlip_diameters:
                def_diameters = circlip_diameters

            # save to db
            CirclipModel(
                inner_diameters=circlip_diameters,
                tooling_diameters=tooling_diameters,
                circlip_width=circlip_width,
                circlip_thickness=circlip_thickness,
                tip_type=tip_type,
                circlip_mises=mises,
                circlip_deformed_diameters=def_diameters,
            ).save()

            latest_model = CirclipModel.objects.latest('id')
            latest_id = latest_model.id
            return HttpResponseRedirect('../report/%s' % latest_id)
        else:
            return HttpResponse('form is invalid')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CirclipForm()

    database = CirclipModel.objects.all()
    return render(request, 'circlip/forms.html', {'form': form, 'database':database})


def reports(request, report_id=None):
    if report_id is None:
        database = CirclipModel.objects.all()
        return render(request, 'circlip/tables.html', {'database': database})
    else:
        database = CirclipModel.objects.get(id=report_id)
        return render(request, 'circlip/report.html', {
            'database': database,
        })


def blank(request):
    # form = CirclipForm()
    database = CirclipModel.objects.all()
    return render(request, 'circlip/test.html', {'database': database})


def base(request):
    # return render(request, 'base.html')
    return HttpResponse('hello')

