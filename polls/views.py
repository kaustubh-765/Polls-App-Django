from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Choice
from .forms import PollForm, ChoiceForm

def index(request):
    polls = Poll.objects.all()
    return render(request, 'polls/index.html', {'polls': polls})

def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        # print("Printing Form_1:", form)
        if form.is_valid():
            poll = form.save()
            return redirect('add_choices', poll_id=poll.id)
    else:
        form = PollForm()
        # print("Printing Form_2:", form)
    return render(request, 'polls/create_poll.html', {'form': form})

def add_choices(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.poll = poll
            choice.save()
            return redirect('add_choices', poll_id=poll.id)
    else:
        form = ChoiceForm()
    choices = poll.choices.all()
    return render(request, 'polls/add_choices.html', {'poll': poll, 'form': form, 'choices': choices})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, id=choice_id)
        choice.votes += 1
        choice.save()
        return redirect('results', poll_id=poll.id)
    return render(request, 'polls/vote.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
