from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib.auth import get_user_model
from ..models import Question, Answer
from django.contrib.auth.hashers import check_password

@login_required(login_url='common:login')
def info(request, pk):
    context = {}
    if request.method == 'POST':
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST.get("new_password")
            user.set_password(new_password)
            user.save()
            return redirect('pybo:index')
        else:
            context.update({'error': "현재 비밀번호가 일치하지 않습니다."})
    else:
        user = get_object_or_404(get_user_model(), pk=pk)

        # 질문
        question_list = Question.objects.order_by('-create_date')

        # 답변
        answer_list = Answer.objects.order_by('-create_date')

        context.update({'question_list': question_list, 'answer_list': answer_list, 'user': user})

    return render(request, 'pybo/info_form.html', context)
