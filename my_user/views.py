from .models import User
from rest_framework import decorators, response, status
from rest_framework.renderers import JSONRenderer
from .serializers import UserCreateSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text



@decorators.api_view(['POST'])
@decorators.renderer_classes([JSONRender])
def register(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    user.is_active = False
    user.save()
    current_site = get_current_site(request)
    mail_subject = 'Active your account'
    to_email = user.Email
    message = render_to_string('confirmation.html', 
                                {
                                    'user': user,
                                    'domain': current_site,
                                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                    'token':
                                })
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    ) 
