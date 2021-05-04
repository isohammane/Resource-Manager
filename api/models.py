from django.db import models
from datetime import date
import string ,random
def unique_code():
    while True:
        code = ''.join(random.choices(string.ascii_letters,k=8))
        if Res.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class Res(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    file = models.FileField(upload_to=f'files/{date.today()}/')
    code = models.CharField(max_length=10,default=unique_code)

    def __str__(self):
        return self.name
    
   