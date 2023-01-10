from social_django.middleware import SocialAuthExceptionMiddleware

class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
       return "It seems that you used a non-Minerva email. Please try again!"