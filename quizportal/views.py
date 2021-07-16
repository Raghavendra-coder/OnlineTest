from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, TestForm, QuestionForm, OptionForm
from .models import User, Test, Question, Option, UserAttempts, UserResponses
from django.contrib.auth import login, logout
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your views here.

def index(request):
    return render(request, "index.html")


def login_option(request):
    return render(request, "login_option.html")


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            login(request, user)
            role = user.role
            if role == 'A':
                return HttpResponseRedirect(reverse('admin_homepage'))
            else:
                return HttpResponseRedirect(reverse('user_homepage'))
    context = {
        'form': form,
    }
    return render(request, "login_page.html", context)


def signup_page(request):
    role = request.GET.get('role')
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user_role = 'A' if role == 'admin' else 'U'
            user.role = user_role
            user.save()
            return HttpResponseRedirect(reverse('cong'))

    context = {
        'form': form,
    }
    return render(request, "signup_page.html", context)


def admin_homepage(request):
    test = Test.objects.all()
    context = {
        'test': test,
    }
    return render(request, "admin_homepage.html", context)


def cong(request):
    return render(request, 'cong.html')


def schedule_test(request):
    t_form = TestForm()
    test = Test.objects.all()
    question = Question.objects.all()
    option = Option.objects.all()
    q_form = QuestionForm()
    o_form = OptionForm()
    test_slug = request.GET.get('test')
    question_id = request.GET.get('question')
    print("555")
    if test_slug:
        print("777")
        this_test = Test.objects.filter(slug=test_slug).prefetch_related('que').first()
    else:
        this_test = None

    if question_id:
        print("666")
        this_question = Question.objects.filter(id=question_id).prefetch_related('opts').first()
    else:
        this_question = None

    print("111")
    if request.method == 'POST' and 'option-submit' in request.POST:
        o_form = OptionForm(request.POST)
        print("222")
        if o_form.is_valid():
            print("333")
            o_form.save()
            return redirect(request.get_full_path())
        else:
            print(o_form.errors)

    if request.method == 'POST' and 'question-submit' in request.POST:
        q_form = QuestionForm(request.POST, request.FILES)
        url = reverse('schedule_test')
        if q_form.is_valid():
            print("999")
            question = q_form.save()
            params = "?test=" + question.select_test.slug + "&question=" + str(question.id)
            return HttpResponseRedirect(url + params)
        else:
            print(q_form.errors)

    if request.method == 'POST' and 'test-submit' in request.POST:
        t_form = TestForm(request.POST)
        url = reverse('schedule_test')
        print("888")
        if t_form.is_valid():
            print("000")
            test = t_form.save(commit=False)
            test.slug = slugify(t_form.cleaned_data['test_name'])
            test.save()
            params = "?test=" + test.slug
            return HttpResponseRedirect(url + params)
        else:
            print("nnn")
    else:
        print("kkk")


    context = {
        't_form': t_form,
        'test': test,
        'q_form': q_form,
        'question': question,
        'this_test': this_test,
        'this_question': this_question,
        'o_form': o_form
    }
    return render(request, "schedule_test.html", context)


def test_page(request):
    test = Test.objects.all()
    context = {
        'test': test,
    }
    return render(request, 'test_page.html', context)


def start_test(request, pk):
    Test.objects.filter(pk=pk).update(status=True)
    return HttpResponseRedirect(reverse('test_page'))


def pause_test(request, pk):
    pause_test = Test.objects.filter(pk=pk).update(status=False)
    return HttpResponseRedirect(reverse('test_page'))


def delete_test(request, pk):
    remove_test = Test.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('test_page'))


def user_homepage(request):
    test = Test.objects.all()
    context = {
        'test': test,
    }
    return render(request, 'user_homepage.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))


def exam(request, pk):
    test = Test.objects.filter(pk=pk).first()
    attempt, created = UserAttempts.objects.get_or_create(test=test, user=request.user)

    if request.method == 'POST':
        questions = request.POST.getlist('question')
        for q in questions:
            answer = request.POST.get('answer-'+q)
            question = Question.objects.filter(pk=q).first()
            ans = Option.objects.filter(pk=answer).first()
            UserResponses.objects.create(omr_question=question, answer=ans, attempt=attempt)
        return HttpResponseRedirect(reverse('complete'))
    context = {
        'test': test,
        'attempt': attempt,
    }
    return render(request, 'exam.html', context)


def complete(request):
    return render(request, 'complete.html')


def report(request, pk):
    attempts = UserAttempts.objects.filter(test__pk=pk)
    print(attempts)
    context = {

        'attempts': attempts,
    }
    return render(request, 'report.html', context)


def answer(request, pk):
    response = UserResponses.objects.filter(attempt__pk=pk)
    context = {
        'response': response,
    }
    return render(request, 'answer.html', context)
