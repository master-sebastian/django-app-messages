

from django.http import response
from django.shortcuts import redirect
from django.urls import reverse
class ProfileCompletionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.bibliography:
                    if request.path not in [reverse("manager_messages:update_profile"), reverse("users:logout")]:
                        return redirect('manager_messages:update_profile')
        response = self.get_response(request)
        return response