from django.http import JsonResponse

from models import Messages


def get(request):
    try:
        resp = {
            'cities': Messages.count_cities(),
            'users': Messages.count_usernames(),
            'results': 'success',
        }
    except Exception as e:
        resp = {
            'results': 'error',
            'error': str(e),
        }
    return JsonResponse(resp)
