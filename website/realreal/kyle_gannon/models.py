import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Menu(models.Model):
    menu_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def _str_(self):
        return self.menu_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        
class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    submenu_text = models.CharField(max_length=200)
    
    def _str_(self):
        return self.submenu_text
