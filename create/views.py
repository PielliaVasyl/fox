from django.shortcuts import render


def create(request, city_title=None, direction_title=None):
    # user_profile = get_object_or_404(UserProfile, pk=profile_id)
    # title = '%s' % (user_profile.user.username,)
    context = {
        # 'title': title,
        # 'instance': user_profile,
    }
    return render(request, 'create/create.html', context)


def create_event(request, city_title=None, direction_title=None):
    # user_profile = get_object_or_404(UserProfile, pk=profile_id)
    # title = '%s' % (user_profile.user.username,)
    context = {
        # 'title': title,
        # 'instance': user_profile,
    }
    return render(request, 'create/create-event.html', context)
