from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from directions.all.forms import PromoActionFilterForm
from entities.models.events import PromoAction

from entities.edit_forms.promo_action import EditPromoActionTitleForm, EditPromoActionDirectionsForm, \
    EditPromoActionCitiesForm, EditPromoActionDescriptionForm, EditPromoActionNoteForm, EditPromoActionImageForm, \
    EditPromoActionVideoForm, EditPromoActionDatesForm, EditPromoActionStatusForm, \
    EditPromoActionEventDanceClassesForm, EditPromoActionLinksForm, EditPromoActionPolicyForm


def promo_action(request, instance_id, direction_title=None, city_title=None):
    current_promo_action = get_object_or_404(PromoAction, pk=instance_id)
    title = '%s' % (current_promo_action.title,)

    form = PromoActionFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_promo_action,
        'form': form
    }
    return render(request, 'entities/promo_action/promo-action-single.html', context)


def edit_promo_action(request, instance_id, city_title=None, direction_title=None):
    current_promo_action = get_object_or_404(PromoAction, pk=instance_id)
    title = '%s' % (current_promo_action.title,)

    context = {
        'title': title,
        'instance': current_promo_action,
    }
    return render(request, 'entities/promo_action/promo-action-edit.html', context)


def edit_promo_action_attr(request, instance_id, attribute=None, city_title=None, direction_title=None):
    current_instance = get_object_or_404(PromoAction, pk=instance_id)
    title = '%s' % (current_instance.title,)

    attr = attribute
    html_template_path = 'entities/promo_action/edit/edit-' + attribute + '.html'

    if attribute == 'title':
        form = EditPromoActionTitleForm(request.POST or None, initial={'title': current_instance.title})
    if attribute == 'directions':
        form = EditPromoActionDirectionsForm(request.POST or None, initial={'directions': current_instance.directions.all()})
    if attribute == 'cities':
        form = EditPromoActionCitiesForm(request.POST or None, initial={'cities': current_instance.cities.all()})
    if attribute == 'description':
        form = EditPromoActionDescriptionForm(request.POST or None, initial={'description': current_instance.description})
    if attribute == 'note':
        form = EditPromoActionNoteForm(request.POST or None, initial={'note': current_instance.note})
    if attribute == 'image':
        if request.method == 'POST':
            form = EditPromoActionImageForm(request.POST, request.FILES)
        else:
            form = EditPromoActionImageForm(None, initial={'image': current_instance.image})
    if attribute == 'video':
        form = EditPromoActionVideoForm(request.POST or None, initial={'video': current_instance.video})
    if attribute == 'dates':
        form = EditPromoActionDatesForm(request.POST or None, initial={'start_date': current_instance.start_date,
                                                                 'end_date': current_instance.end_date})
        attr = 'end_date'
    if attribute == 'status':
        form = EditPromoActionStatusForm(request.POST or None, initial={'_status': current_instance._status})
        attr = '_status'
    if attribute == 'event-dance-classes':
        form = EditPromoActionEventDanceClassesForm(request.POST or None,
                                              initial={'dance_directions':
                                                        current_instance.local_classes.dance_directions.all(),
                                                       'dance_styles': current_instance.local_classes.dance_styles.all()})
    if attribute == 'promo-action-links':
        form = EditPromoActionLinksForm(request.POST or None, initial={'links': current_instance.links.all()})
        attr = 'links'
    if attribute == 'policy':
        form = EditPromoActionPolicyForm(request.POST or None, initial={'owners': current_instance.owners.all(),
                                                                  'contributors': current_instance.contributors.all(),
                                                                  'author': current_instance.author})
        attr = 'author'

    if form.is_valid():
        if attribute == 'image':
            if 'image' in request.FILES:
                new_attr = request.FILES['image']
            else:
                new_attr = None
        elif attribute == 'dates':
            start_date = form.cleaned_data.get('start_date')
            setattr(current_instance, 'start_date', start_date)
            new_attr = form.cleaned_data.get(attr)
        elif attribute == 'event-dance-classes':
            dance_styles = form.cleaned_data.get('dance_styles')
            setattr(current_instance.local_classes, 'dance_styles', dance_styles)
            dance_directions = form.cleaned_data.get('dance_directions')
            setattr(current_instance.local_classes, 'dance_directions', dance_directions)
            new_attr = None
        elif attribute == 'policy':
            owners = form.cleaned_data.get('owners')
            setattr(current_instance, 'owners', owners)
            contributors = form.cleaned_data.get('contributors')
            setattr(current_instance, 'contributors', contributors)
            new_attr = form.cleaned_data.get(attr)
        else:
            new_attr = form.cleaned_data.get(attr)
        setattr(current_instance, attr, new_attr)
        current_instance.save()
        return HttpResponseRedirect('/promo-action-%s/edit/%s' %
                                    (current_instance.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'instance': current_instance,
        'form': form
    }
    return render(request, html_template_path, context)
