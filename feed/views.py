from django.shortcuts import render, get_object_or_404

from algoritms.instances_directions import instances_directions
from directions.dance.forms import DanceStyleFilterForm
from entities.models.posts import Article, DanceStyle


def articles(request, city_title=None, direction_title=None):
    title = 'Статьи'
    current_articles = Article.objects.all()
    context = {
        'title': title,
        'articles': current_articles
    }
    return render(request, 'feed/articles.html', context)


def article(request, article_id, city_title=None, direction_title=None):
    current_article = get_object_or_404(Article, pk=article_id)
    title = '%s' % (current_article.title,)
    context = {
        'title': title,
        'article': current_article
    }
    return render(request, 'feed/article-single.html', context)


def links(request, city_title=None, direction_title=None):
    title = 'Полезные ссылки'

    context = {
        'title': title,
    }
    return render(request, 'feed/links.html', context)


def organizations(request, city_title=None, direction_title=None):
    title = 'Организации и компании'

    context = {
        'title': title,
    }
    return render(request, 'feed/organizations.html', context)


def persons(request, city_title=None, direction_title=None):
    title = 'Персоны и личности'

    context = {
        'title': title,
    }
    return render(request, 'feed/persons.html', context)


def dance_styles(request, city_title=None, direction_title=None):
    title = 'Танцевальные стили'

    filters = None
    form = DanceStyleFilterForm(request.POST or None)
    if form.is_valid():
        titles = form.cleaned_data.get('titles')
        directions = form.cleaned_data.get('directions')
        count_types = form.cleaned_data.get('count_types')
        distance_types = form.cleaned_data.get('distance_types')
        average_prices = form.cleaned_data.get('average_prices')
        attendee_ages = form.cleaned_data.get('attendee_ages')
        if titles or directions or count_types or distance_types or average_prices or attendee_ages:
            filters = {}
            if titles:
                filters['titles'] = titles
            if directions:
                filters['directions'] = directions
            if count_types:
                filters['count_types'] = count_types
            if distance_types:
                filters['distance_types'] = distance_types
            # if average_prices:
            #     filters['average_prices'] = average_prices
            # if attendee_ages:
            #     filters['attendee_ages'] = attendee_ages
    #
    styles_directions = instances_directions(DanceStyle, filters=filters)

    context = {
        'title': title,
        'styles_directions': styles_directions,
        'form': form,
    }
    return render(request, 'feed/dance-styles.html', context)


def dance_style(request, dance_style_id, city_title=None, direction_title=None):
    current_dance_style = get_object_or_404(DanceStyle, pk=dance_style_id)
    title = '%s' % (current_dance_style.title,)
    form = DanceStyleFilterForm(request.POST or None)
    context = {
        'title': title,
        'instance': current_dance_style,
        'form': form
    }
    return render(request, 'feed/dance-style-single.html', context)
