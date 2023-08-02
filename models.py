from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone



class Advertisement(models.Model):
    title = models.CharField('НАЗВАНИЕ', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def created_date(self):
        if self.created_at.date()== timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:green; font-weigh:bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%y в %H:%M:%S')

    def check_update(self):
        if self.updated_at.date() == timezone.now().date():
            created_date = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:blue; font-weigh:bold;"> Сегодня в {} </span>', created_date
            )
        return self.updated_at.strftime('%d.%m.%y в %H:%M:%S')
    
    def __str__(self): 
        return f"Advertisemenet(id={str(self.id)}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
