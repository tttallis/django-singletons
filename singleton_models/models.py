from django.db import models

class SingletonModel(models.Model):
    
    class Meta:
        abstract = True
            
    def save(self, *args, **kwargs):
        self.id=1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

        
