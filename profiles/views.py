from django.shortcuts import render, get_object_or_404

from entities.models.userprofile import UserProfile


def profile(request, profile_id, city_title=None, direction_title=None):
    user_profile = get_object_or_404(UserProfile, pk=profile_id)
    title = '%s' % (user_profile.user.username,)
    context = {
        'title': title,
        'instance': user_profile,
    }
    return render(request, 'profiles/profile-single.html', context)
