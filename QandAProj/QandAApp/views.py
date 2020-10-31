from django.shortcuts import render
from QandAApp.models import QandAModel
# Create your views here.
from QandAApp.forms import NewQnadAForm
def index(request):
    my_dict={'insert_content': "HELLO IM FROM QNADAAPP!"}
    return render(request, 'QandAApp/index.html', context=my_dict)


#poniżej nie jestem pewnien
def QandAView(request):

    form = NewQnadAForm()

    if request.method == "POST":
        form = NewQnadAForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request) #return index page afterwards
        else:
            print("ERROR FORM INVALID")
    return render(request, 'QandAApp/QandApage.html', {'form': form})
