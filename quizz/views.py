from django.shortcuts import render
from django.http import HttpResponse
from quizz.models import Quizz # if we had more than one model we could have given *

# Create your views here.


#def hello(request):
 #   return render(request,'main_page.html')
#def add(request):
 #   val1=int(request.POST['num1'])
  #  val2=int(request.POST['num2'])
   # res=(val1)+(val2)
    #return render(request,'addition_result.html',{'result':res})


def home(request):
    if request.method == 'POST':
        #print(request.POST)
        que = Quizz.objects.all()
        score=0
        total = 0
        temp1 = '0'

        for q in que:
            total += 1
            print(q.Question)
            print(q.Correct_Answer)
            print("Hello")
            temp1=str(total)
            print(request.POST.get(temp1))
            if q.Correct_Answer == request.POST.get(temp1):
                score += 1



        context ={
            'score': score,
            'total': total
           }
        return render(request, 'result.html', context)
    else:
        que = Quizz.objects.all()
        context = {
            'que': que
        }
        return render(request, 'index.html', context)


