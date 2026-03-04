from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message


@login_required
def room_list(request):
    rooms = Room.objects.all().order_by('name')
    return render(request, 'chat/room_list.html', {'rooms': rooms})


@login_required
def room_detail(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    messages = room.messages.select_related('user').order_by('timestamp')[:50]
    return render(request, 'chat/room_detail.html', {
        'room': room,
        'messages': messages,
    })