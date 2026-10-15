from django.db import models

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Zone(AbstractBaseModel):
    name = models.CharField(max_length=120,verbose_name="Название")
    location = models.CharField(max_length=120,verbose_name="Город")
    coordinates = models.CharField(max_length=100,verbose_name="Координаты")
    description = models.TextField(blank=True,verbose_name="Описание")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Zone"
        verbose_name_plural = "Zones"

class Visitors(AbstractBaseModel):
    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name='visitors'
    )
    full_name = models.CharField(max_length=200,verbose_name="ФИО")
    info = models.CharField(blank=True)
    is_allowed = models.BooleanField(default=False,verbose_name="Разрешен ли вход")

    def __str__(self):
        return self.full_name
    