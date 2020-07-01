from myapp.models import BankDetail 

def run():
    for i in range(1,4000):
        obj=BankDetail.objects.get(id=i)
        obj.delete()