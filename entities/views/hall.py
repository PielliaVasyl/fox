from django.shortcuts import render, get_object_or_404

from directions.all.forms import HallsFilterForm
from entities.models import Hall


def hall(request, hall_id, direction_title=None, city_title=None):
    current_hall = get_object_or_404(Hall, pk=hall_id)
    title = '%s' % (current_hall.title,)

    form = HallsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_hall,
        'form': form
    }
    return render(request, 'map/hall/hall-single.html', context)
