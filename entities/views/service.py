from django.shortcuts import get_object_or_404, render

from directions.all.forms import CustomerServicesFilterForm
from entities.models import CustomerServices


def service(request, service_id, direction_title=None, city_title=None):
    current_services = get_object_or_404(CustomerServices, pk=service_id)
    title = '%s' % (current_services.title,)

    form = CustomerServicesFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_services,
        'form': form
    }
    return render(request, 'map/service/service-single.html', context)
