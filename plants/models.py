from django.db import models

class Plant(models.Model):
    scientific_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255)
    growth_habit = models.CharField(max_length=50, choices=[
        ('shrub', 'Shrub'),
        ('tree', 'Tree'),
        ('vine', 'Vine'),
        ('perennial', 'Perennial'),
        ('annual', 'Annual'),
    ])
    sun_exposure = models.CharField(max_length=50, choices=[
        ('full_sun', 'Full Sun'),
        ('partial_shade', 'Partial Shade'),
        ('full_shade', 'Full Shade'),
    ])
    water_needs = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ])
    soil_requirements = models.CharField(max_length=100)
    bloom_time = models.CharField(max_length=50, choices=[
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter'),
    ], blank=True, null=True)  # Optional for some plants
    usda_hardiness_zones = models.CharField(max_length=50)
    image = models.ImageField(upload_to='plants/')
    height_cm = models.PositiveIntegerField()  # Height in centimeters
    spread_cm = models.PositiveIntegerField()  # Spread in centimeters
    harvest_time = models.CharField(max_length=50, blank=True, null=True)  # Optional
    plant_spacing_row = models.PositiveIntegerField()  # Spacing between rows (cm)
    plant_spacing_plant = models.PositiveIntegerField()  # Spacing between plants (cm)
    planting_depth = models.PositiveIntegerField()  # Planting depth (cm)
