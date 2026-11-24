import logging
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

logger = logging.getLogger(__name__)

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'notes/ticket_list.html', {'tickets': tickets})

def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            logger.info("Создана заявка: %s", ticket.title)
            return redirect('ticket_list')
        else:
            logger.warning("Ошибка при заполнении формы заявки")
    else:
        form = TicketForm()

    return render(request, 'notes/ticket_form.html', {'form': form})
