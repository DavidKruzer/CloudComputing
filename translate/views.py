from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Translation
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .translater import translate

# Create your views here.
def index(request):
    latest_question_list = Translation.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request, translation_id):
    translation = get_object_or_404(Translation, pk=translation_id)
    return render(request, 'polls/translation.html', {'translation': translation})
def translation(request):
    original = request.POST.get("original", "");
    translation = translate(original);
    return HttpResponse(translation);
