from django.db import models

class Advertisement(models.Model):
    #create choice field for advertisement type
    class choices(models.TextChoices):
            accepted = "accepted"  
            rejected = "rejected"
            pending = "pending"
            
    id=models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    email = models.EmailField()
    category=models.CharField(max_length=50)
    state=models.CharField(max_length=50,choices=choices.choices,default=choices.pending)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title