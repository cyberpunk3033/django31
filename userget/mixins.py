from django.utils import translation

from rest_framework.views import APIView
from rest_framework.response import Response


class LanguageMixin:
    def get_language_from_request(self, request):
        # Получаем предпочитаемый язык из параметра запроса или заголовка
        language = request.query_params.get('language')

        if not language:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        return language

    def get_response_in_language(self, request, content):
        # Получаем предпочитаемый язык
        language = self.get_language_from_request(request)

        # Обработка контента на выбранном языке

        # Вернуть контент на выбранном языке
        return content