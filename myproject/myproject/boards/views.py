from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewTopicForm
from boards.models import Board
from .models import Board,Topic,Post 
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    boards = Board.objects.all()
    # boards_name = list()
    return render(request,'home.html',{'boards':boards})
def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request,'topics.html',{'board':board})
    
def new_topic(request, pk):
    board = Board.objects.get(pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        # subject = request.POST['subject']
        # message = request.POST['message']

        # user = User.objects.first()
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.clean_data.get('message'),
                topic = topic,
                created_by =user
            )
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request,'new_topic.html',{'board':board, 'form':form})     
        # topic = Topic.objects.create(
        #     subject = subject,
        #     board = board,
        #     starter = user
        # )

        # post = Post.objects.create(
        #     message = message,
        #     topic = topic,
        #     created_by = user

        # )
        

    

    

    # for board in boards:
    #     boards_name.append(board.name)

    # response_html = '<br'.join(boards_name)
    # return HttpResponse(response_html)    