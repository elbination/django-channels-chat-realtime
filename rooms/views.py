from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Message


# Create your views here.
@login_required
def get_rooms(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'rooms/list.html', context)


@login_required
def get_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    context = {
        'room': room,
        'messages': messages
    }

    return render(request, 'rooms/detail.html', context)
