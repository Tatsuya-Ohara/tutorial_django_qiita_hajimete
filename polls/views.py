from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    '''HttpRequestクラスのrequestを受け取る'''
    # 戻り値はHttpResponse形式になっている
    return HttpResponse('Hello, World!!')

def detail(request, question_id):
    context = {'question_id': question_id}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)