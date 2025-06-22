from django.db import models

class ApplicationsManager(models.Manager):
    def active(self):
        return self.filter(
            state = True
        ).order_by(
            'id'
        )
    
    def desactive(self):
        return self.filter(
            state = False
        ).order_by(
            'id'
        )