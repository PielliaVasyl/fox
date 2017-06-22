def get_filtered_instances(instances, filters=None):
    if filters is not None:
        for key, value in filters.items():
            if key == 'event_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.types.all()]).isdisjoint(value)]
            if key == 'cities':
                instances = [i for i in instances
                             if not set([str(j.city.pk) for j in i.locations.all() if j.city]).isdisjoint(value)]

            if key == 'dance_styles':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.local_classes.dance_styles.all()]).isdisjoint(value)]

            if key == 'schools' or key == 'shops' or key == 'places':
                instances = [i for i in instances if i and str(i.pk) in value]

            if key == 'price_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.price_types.all()]).isdisjoint(value)]
            if key == 'event_dance_schools':
                instances = [i for i in instances if i.dance_studio and str(i.dance_studio.pk) in value]
            if key == 'experience_levels':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.experience_levels.all()]).isdisjoint(value)]

            if key == 'place_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.types.all()]).isdisjoint(value)]

            if key == 'shop_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.types.all()]).isdisjoint(value)]

            if key == 'titles':
                instances = [i for i in instances if i.pk and str(i.pk) in value]
            if key == 'directions':
                instances = [i for i in instances
                             if i.dance_style.direction and str(i.dance_style.direction.pk) in value]
            if key == 'count_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.count_types.all()]).isdisjoint(value)]
            if key == 'distance_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.distance_types.all()]).isdisjoint(value)]
            # if key == 'average_prices':
            #     instances = [i for i in instances
            #                  if not set([str(j.pk) for j in i.average_prices.all()]).isdisjoint(value)]
    if instances:
        instances = list(set(instances))
    return instances
