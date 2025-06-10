from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            name = contact.full_name
            phone = contact.phone_number 
            send_mail(
                "Запись на детейлинг",
                f"ФИО клиента: {name}\n Номер телефона клиента: {phone}",
                "azamat.mambetov.2014@mail.ru",
                ["azamat.mambetov.2014@gmail.com"]
            )
            contact.save()
            return redirect("home")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
