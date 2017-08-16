from django.shortcuts import render, get_object_or_404

from directions.all.forms import SchoolsFilterForm
from entities.models import Shop


def shop(request, shop_id, direction_title=None, city_title=None):
    current_shop = get_object_or_404(Shop, pk=shop_id)
    title = '%s' % (current_shop.title,)

    form = SchoolsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_shop,
        'form': form
    }
    return render(request, 'map/shop/shop-single.html', context)
