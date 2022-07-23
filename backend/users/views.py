from django.forms import ValidationError
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.conf import settings


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.password_validation import get_password_validators, validate_password, password_changed, password_validators_help_texts

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


from .models import CustomUserModel
from .serializers import CustomUserSerializer



@require_http_methods(['POST'])
def user_login(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)

    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return JsonResponse({
            'success': False,
            'errors': {
                'username': ['This field is required!'],
                'password': ['This field is required!']
            }
        }, status=400)

    user = authenticate(request, username=username, password=password)

    if user==None:
        return JsonResponse({
            'success': False,
            'errors': {
                'password': ['Invalid credentials!'],
                }
        }, status=400)

    login(request, user)
    serializer = CustomUserSerializer(user)

    return JsonResponse({
                'success': True,
                'data': serializer.data
            })


@require_http_methods(['GET'])
@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({
        'success': True
    })


@require_http_methods(['GET'])
@login_required
def user_details(request):
    user = request.user
    serializer = CustomUserSerializer(user)
    return JsonResponse({
                'success': True,
                'data': serializer.data
            })


@require_http_methods(['POST'])
@login_required
def user_change_password(request):
    user:CustomUserModel = request.user
    
    password1 = request.POST.get('password1', None)
    password2 = request.POST.get('password2', None)


    error_message__password1_password2_should_be_same = 'Value of password1 and password2 should be same.'
    help_text__value_same_as_password1 = 'Value should be same as password1 field.'

    # Check passwords are provided and passwords are same
    if password1==None or password2==None:
        return JsonResponse({
                'success': False,
                'help': {
                    'password1': password_validators_help_texts(),
                    'password2': [help_text__value_same_as_password1]
                },
                'errors': {
                    'password1': ['Both password1 and password2 fields are required'],
                    'password2': ['Both password1 and password2 fields are required']
                    }
            }, status=400)
    elif password1!=password2:
        return JsonResponse({
                'success': False,
                'help': {
                    'password1': password_validators_help_texts(),
                    'password2': [help_text__value_same_as_password1]
                },
                'errors': {
                    'password2': [error_message__password1_password2_should_be_same],
                }
            }, status=400)

    # Validate password strength using the django default password validators in settings module
    password_validators = get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
    try:
        validate_password(password=password1, user=user, password_validators=password_validators)
    except ValidationError as validation_error:
        return JsonResponse({
                'success': False,
                'help': {
                    'password1': password_validators_help_texts(),
                    'password2': [help_text__value_same_as_password1]
                },
                'errors': {
                    'password1': validation_error.messages,
                }
            }, status=400)
    
    # Change password
    user.set_password(password1)
    password_changed(password1, user)
    logout(request)
    return JsonResponse({
        'success': True,
    })
