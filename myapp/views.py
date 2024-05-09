from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from .models import User, Order
from django.shortcuts import render, redirect
from .forms import OrderForm

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success') # Перенаправление на страницу успеха или список заказов
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')


def about(request):
     try:
        result = 1 / 1
     except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
     else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")

def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp/my_template.html", context)

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
        text = ""
        ... # формируем статьи за год
        return HttpResponse(f"Posts from {year}<br>{text}")

class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ... # формируем статьи за год и месяц
        return HttpResponse(f"Posts from{month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
        ... # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
        post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы  задумался над тем, какой способ создания списков в Python работает быстрее..."
        }
        return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})




