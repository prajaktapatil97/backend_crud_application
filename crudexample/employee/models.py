from django.db import models

# Create your models here.
from django.db import models  
class userTable(models.Model):  
    user_id = models.CharField(max_length=256)  
    user_name = models.CharField(max_length=256)  
    user_email = models.EmailField()  
    is_deleted = models.BooleanField(default=False)
    class Meta:  
        db_table = "userTable"