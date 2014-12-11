from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat}

    # https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources=%27web%2Bimage%2Bvideo%2Bnews%2Bspell%27
    # 69RYAs7haBiOm3wuG4wxpcq2k1Xujoh5rzzIISYlbmU Primary Key for Bing API