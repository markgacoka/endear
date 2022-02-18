from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import redirect
from allauth.utils import get_user_model
from allauth.account.utils import perform_login
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.signals import pre_social_login
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class MyLoginAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        if request.user.is_authenticated:
            return settings.LOGIN_REDIRECT_URL.format(
                email_address=request.user.email_address)

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        pass

@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    user = get_user_model()
    username = sociallogin.account.extra_data['name']
    email_address = sociallogin.account.extra_data['email']

    # if user exists login
    if user.objects.filter(email=email_address).exists():
        curr_user = user.objects.filter(email=email_address)
        perform_login(request, curr_user[0], email_verification='optional')
    # else them sign up as a new user
    else:
        new_user, created = user.objects.update_or_create(
            email_address = email_address,
            username = username,
            defaults = {
                'first_name': sociallogin.account.extra_data['given_name'],
                'last_name': sociallogin.account.extra_data['family_name'],
                'profile_image': sociallogin.account.extra_data['picture'],
                'is_superuser': False,
                'is_staff': False,
            }
        )

    if created:
        new_user.save()
        raise ImmediateHttpResponse(redirect('dashboard'))
    else:
        raise ImmediateHttpResponse(
            redirect('home')   
        )
