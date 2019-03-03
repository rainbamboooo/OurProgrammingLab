from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from urllib import parse

from .test_code import OnlineCompile
from .chatmanager import Chatmanager
from .answers import answers_dict

# Create your views here.


chatmgr = Chatmanager()


def index(request):
    return render(request, "oclass/index.html")


def lesson_list(request):
    _lesson_list = [ "Lesson 1", "Lesson 2" ]

    return HttpResponse("%s" % _lesson_list)


@csrf_exempt
def check_msg(request):
    idex = int(request.POST["idex"])

    if chatmgr.is_outdated(idex):
        return JsonResponse(chatmgr.get_last_msg(), safe=False)
    return JsonResponse("", safe=False)


@csrf_exempt
def new_msg(request):
    nmsg = request.POST["nmsg"]
    if new_msg:
        chatmgr.add_msg(nmsg)
    return JsonResponse("", safe=False)


@csrf_exempt
def run_code(request):
    code_str = parse.unquote(request.POST["code"])
    lesson_id = request.POST["lessonid"]
    compiler = OnlineCompile(code_str, "cpp", lesson_id, lesson_id)

    result = compiler.result()
    if result == answers_dict[str(lesson_id)]:
        return JsonResponse("Good job!", safe=False)
    return JsonResponse("""Try again! 
                        Your output:  
                        """ + result + """
                        Answer: 
                        """ + answers_dict[str(lesson_id)], safe=False)


def lessons(request, lesson_id):
    return render(request, "oclass/lesson/%d.html" % lesson_id)

