from django.shortcuts import render
from QandAApp.models import QandAModel
# Create your views here.
def index(request):
    my_dict={'insert_content': "HELLO IM FROM QNADAAPP!"}
    return render(request, 'QandAApp/index.html', context=my_dict)

def QandAView(request):
    question_list= QandAModel.objects.order_by('question')
    question_dict = {'questions': question_list}
