import json
import requests

from .models import Neuron

from django.shortcuts import render
from django.views.generic import TemplateView, View


class Home(TemplateView):
    template_name = "base.html"

class DisplayData(View):
    def get(self, request):
        url = "http://neuromorpho.org/api/neuron/select?q=species:monkey"
        data = json.loads(requests.get(url).text)['_embedded']['neuronResources']

        for item in data:
            neuron = Neuron(age_scale=item['age_scale'],
                            age_classification=item['age_classification'],
                            gender=item['gender'],
                            species=item['species'],
                            strain=item['strain'],
                            scientific_name=item['scientific_name'],
                            slicing_direction=item['slicing_direction'],
                            reconstruction_software=item['reconstruction_software'],
                            objective_type=item['objective_type'],
                            original_format=item['original_format'],
                            domain=item['domain'],
                            attributes=item['attributes'],
                            magnification=item['magnification'],
                            shrinkage_reported=item['shrinkage_reported'],
                            protocol=item['protocol'],
                            stain=item['stain'],
                            shrinkage_corrected=item['shrinkage_corrected'],
                            physical_Integrity=item['physical_Integrity'],
                            note=item['note'],
                            upload_date=item['upload_date'],
                            deposition_date=item['deposition_date'],
                            reported_value=item['reported_value'],
                            reported_xy=item['reported_xy'],
                            reported_z=item['reported_z'],
                            corrected_value=item['corrected_value'],
                            # DecimalFieldcorrected_xy=item.get(['DecimalFieldcorrected_xy'], ),
                            corrected_z=item['corrected_z'],
                            soma_surface=item['soma_surface'],
                            surface=item['surface'],
                            volume=item['volume'],
                            slicing_thickness=item['slicing_thickness'],
                            min_age=item['min_age'],
                            max_age=item['max_age'],
                            min_weight= item['min_weight'] if item['min_weight'] != 'Not Reported' else 0,
                            max_weight=item['max_weight'] if item['max_weight'] != 'Not Reported' else 0,
                            png_url=item['png_url'])
            neuron.save()
        print(len(data))
        return render(request, template_name="core/neuron_list.html", context={'neuron_list': data})
