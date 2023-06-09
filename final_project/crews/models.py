from django.db import models

# Create your models here.
class Crew(models.Model):
    crew_id = models.AutoField(primary_key = True)
    crew_name = models.CharField(max_length = 50, verbose_name = "crew's name ")
    crew_pic = models.ImageField(upload_to = 'images/crew/')

    def __str__(self) -> str:
        return 'Crew ' + self.crew_name

class Region(models.Model):
    region_id = models.AutoField(primary_key = True)
    region_name = models.CharField(max_length = 50, verbose_name = "region's name ")
    region_pic = models.ImageField(upload_to = 'images/region/')

    def __str__(self) -> str:
        return 'Region ' + self.region_name

class Island(models.Model):
    island_id = models.AutoField(primary_key = True)
    island_name = models.CharField(max_length = 50, verbose_name = "island's name ")
    island_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    island_pic = models.ImageField(upload_to = 'images/island/')

    def __str__(self) -> str:
        return 'Island ' + self.island_name

class Has(models.Model):
    class Meta :
        unique_together = ('crew', 'island')

    has_id = models.AutoField(primary_key = True)
    crew = models.ForeignKey(Crew, on_delete = models.CASCADE)
    island = models.ForeignKey(Island, on_delete = models.CASCADE)

    def __str__(self) -> str :
        cre = self.crew
        tre = self.island
        return cre.__str__() +  ' has seen ' + tre.__str__()