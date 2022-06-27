from django.db import models

# Create your models here.

class CompanyAndDividends(models.Model):
  id = models.IntegerField('id')
  abbreviation = models.CharField('abbreviation',primary_key=True,max_length=60)
  dy1 = models.DecimalField('dy1',max_digits=12, decimal_places=2,null=False, default=0.0)
  dy3 = models.DecimalField('dy3',max_digits=12, decimal_places=2,null=False, default=0.0)
  dy5 = models.DecimalField('dy5',max_digits=12, decimal_places=2,null=False, default=0.0)
  r1 = models.DecimalField('r1',max_digits=12, decimal_places=2,null=False, default=0.0)
  r3 = models.DecimalField('r3',max_digits=12, decimal_places=2,null=False, default=0.0)
  r5 = models.DecimalField('r5',max_digits=12, decimal_places=2,null=False, default=0.0)
  

  def __str__(self):
    return f"abbreviation: {self.abbreviation}, dy1: {self.dy1}, dy3: {self.dy3}, dy5: {self.dy5}"