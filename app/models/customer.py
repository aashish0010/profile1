from django.db import models



class Customer(models.Model):
    image = models.ImageField(upload_to='upload')
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False



