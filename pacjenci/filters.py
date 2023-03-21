import django_filters 
from .models import *
from django_filters import DateFilter

class PacjentFilter(django_filters.FilterSet):
    class Meta:
        model = Pacjent
        fields = '__all__'
        # exclude = [ 'content','date']


# content = models.CharField(max_length=100,null=True,blank=True)
# date = models.DateTimeField()   #input type="data"
# lekarz = models.ForeignKey(Lekarz,on_delete=models.SET_NULL,null=True)
# oddział = models.ForeignKey(Oddział,on_delete=models.CASCADE)
# pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)