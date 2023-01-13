from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question

def index(request):
    # 逆順に並び替え
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
    # '''HttpRequestクラスのrequestを受け取る'''
    # # 戻り値はHttpResponse形式になっている
    # return HttpResponse('Hello, World!!')

def detail(request, question_id):
    '''詳細ページ''' 
    # get_object_or_404を使ったショートカットバージョン
    question = get_object_or_404(Question, pk=question_id)
    choice_list = question.choice_set.all()
    context = {'question': question, 'choice_list': choice_list}
    return render(request, 'polls/detail.html', context)
    
    # Http404を使った少し長いバージョン
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # 404エラーを送出
        raise Http404("Question does not exist")
    choice_list = question.choice_set.all()
    context = {'question': question, 'choice_list': choice_list}
    return render(request, 'polls/detail.html', context)
    
    # # 質問のクエリセットを全て取得する
    # questions = Question.objects.all()
    # # 並び替え
    # questions = Question.objects.order_by('question_text')
    # # 条件を満たす
    # questions = Question.objects.filter(question_text='質問1')
    # # 条件から除外する
    # questions = Question.objects.exclude(question_text='質問1')
    # # 条件に合うものが1つであるとわかっている場合: クエリセットではなく、1つのインスタンスが得られる
    # question = Question.objects.get(question_text='質問1')
    # # Choice: Questionに対応するChoiceだけ抜き出すには...以下のようにする
    # choices = question.choice_set.exclude(choice_text='答え1')
    
    # print(choices)
    # context = {'question_id': question_id}
    # return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # response = "You are looking at the results of question %s."
    # return HttpResponse(response % question_id)