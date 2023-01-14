from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from .forms import *
from .models import Question

def index(request):
    # 逆順に並び替え
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
    # '''HttpRequestクラスのrequestを受け取る'''
    # # 戻り値はHttpResponse形式になっている
    # return HttpResponse('Hello, World!!')

@login_required
def detail(request, question_id):
    '''詳細ページ'''
    user = request.user 
    question = get_object_or_404(Question, pk=question_id)
    
    # ユーザーからのリクエストがPOST
    if request.method == 'POST':
        # リクエストを渡してformオブジェクトを作成
        form = VoteForm(request.POST, question=question)
        if form.is_valid():
            form.save()
            # 正常終了したらredirectが推奨
            return redirect('polls:results', question_id=question.id)
    else:
        # 空のフォームインスタンスを作成
        form = VoteForm(question=question)
    
    context = {'user': user, 'question': question, 'form': form}
    return render(request, "polls/detail.html", context)
    
    
    # # get_object_or_404を使ったショートカットバージョン
    # question = get_object_or_404(Question, pk=question_id)
    # choice_list = question.choice_set.all()
    # context = {'question': question, 'choice_list': choice_list}
    # return render(request, 'polls/detail.html', context)
    
    # # Http404を使った少し長いバージョン
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     # 404エラーを送出
    #     raise Http404("Question does not exist")
    # choice_list = question.choice_set.all()
    # context = {'question': question, 'choice_list': choice_list}
    # return render(request, 'polls/detail.html', context)
    
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

def signup(request):
    '''froms.pyのSignUpFromを処理する'''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'polls/signup.html', context)