from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from .forms import TemplateForm
from django.http import JsonResponse, HttpResponse

class TemplView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST.dict()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP

        user_agent = request.META.get('HTTP_USER_AGENT')
        received_data['user_agent'] = user_agent

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            name = form.cleaned_data.get("name")  # Получили очищенные данные
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")

            return JsonResponse(received_data)
        return render(request, 'landing/index.html', context={"form": form})
