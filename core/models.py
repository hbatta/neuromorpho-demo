from django.db import models


class Neuron(models.Model):
    neuron_id = models.IntegerField(primary_key=True)

    neuron_name = models.CharField(max_length=100)
    archive = models.CharField(max_length=100)
    age_scale = models.CharField(max_length=100)
    age_classification = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    strain = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    slicing_direction = models.CharField(max_length=100)
    reconstruction_software = models.CharField(max_length=100)
    objective_type = models.CharField(max_length=100)
    original_format = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    attributes = models.CharField(max_length=100)
    magnification = models.CharField(max_length=100)
    shrinkage_reported = models.CharField(max_length=100)
    protocol = models.CharField(max_length=100)
    stain = models.CharField(max_length=100)
    shrinkage_corrected = models.CharField(max_length=100, null=True, blank=True)
    physical_Integrity = models.CharField(max_length=100)

    note = models.TextField()

    upload_date = models.DateField()
    deposition_date = models.DateField()

    reported_value = models.FloatField(null=True, blank=True, default=0)
    reported_xy = models.FloatField(null=True, blank=True, default=0)
    reported_z = models.FloatField(null=True, blank=True, default=0)
    corrected_value = models.FloatField(null=True, blank=True, default=None)
    DecimalFieldcorrected_xy = models.FloatField(null=True, blank=True, default=None)
    corrected_z = models.FloatField(null=True, blank=True, default=None)
    soma_surface = models.FloatField(null=True, blank=True, default=None)
    surface = models.FloatField(null=True, blank=True, default=None)
    volume = models.FloatField(null=True, blank=True, default=None)
    slicing_thickness = models.FloatField(null=True, blank=True, default=None)
    min_age = models.FloatField(null=True, blank=True, default=None)
    max_age = models.FloatField(null=True, blank=True, default=None)
    min_weight = models.FloatField(null=True, blank=True, default=None)
    max_weight = models.FloatField(null=True, blank=True, default=None)

    png_url = models.URLField()

    # == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
    # "brain_region": [
    #     "neocortex",
    #     "prefrontal",
    #     "layer 3"
    # ],
    #
    # == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
    # "cell_type": [
    #     "Local projecting",
    #     "pyramidal",
    #     "principal cell"
    # ],

    # == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
    # "experiment_condition": [
    #     "Control"
    # ],

    # "reference_pmid": [
    #     "12204204",
    #     "12902394"
    # ],
    #
    # "reference_doi": [
    #     "10.1016/S0306-4522(02)00305-6",
    #     "10.1093/cercor/13.9.950"
    # ],

    # "_links": {
    #     "self": {
    #         "href": "http://neuromorpho.org/api/neuron/id/1"
    #     },
    #     "measurements": {
    #         "href": "http://neuromorpho.org/api/morphometry/id/1"
    #     },
    #     "persistence_vector": {
    #         "href": "http://neuromorpho.org/api/pvec/id/1"
    #     }
