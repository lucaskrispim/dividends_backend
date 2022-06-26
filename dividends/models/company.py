from django.db import models

# Create your models here.

class Company(models.Model):
  id = models.IntegerField('id')
  name = models.CharField('name',max_length=30)
  abbreviation = models.CharField('abbreviation',primary_key=True,max_length=30)
  sector = models.CharField('setor',max_length=30)
  dy = models.DecimalField('dy',max_digits=12, decimal_places=2,null=True)
  price = models.DecimalField('price',max_digits=12, decimal_places=2,null=True)

  def __str__(self):
    return f"id:{self.id}, name: {self.name}, abbreviation: {self.abbreviation}, sector: {self.sector}, dy: {self.dy}, price: {self.price}"

