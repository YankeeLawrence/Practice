from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Questionnaire

def questionnaire_list(request):
    data = []
    qs = Questionnaire.objects.all().order_by('-create_time')

    for q in qs:
        data.append({
            'id': q.id,
            'title': q.title,
            'description': q.description,
            'create_time': q.create_time.strftime('%Y-%m-%d')
        })

    return JsonResponse({'code': 0, 'data': data})

from .models import Question

def questionnaire_detail(request, qid):
    q = Questionnaire.objects.get(id=qid)

    questions = []
    for item in q.questions.all():
        questions.append({
            'id': item.id,
            'content': item.content
        })

    return JsonResponse({
        'code': 0,
        'data': {
            'title': q.title,
            'description': q.description,
            'questions': questions
        }
    })
