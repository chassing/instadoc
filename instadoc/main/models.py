
from django.db import models


class Documentation(models.Model):
    item = models.CharField(max_length=254)
    url = models.CharField(max_length=254)
    html = models.TextField(blank=True)
    category = models.ForeignKey("Category", related_name="docs")

    class Meta:
        ordering = ('-item',)

    def __unicode__(self):
        return self.item


class Category(models.Model):
    item = models.CharField(max_length=254)
    url = models.CharField(max_length=254, blank=True)

    class Meta:
        ordering = ('item',)

    def __unicode__(self):
        return self.item
