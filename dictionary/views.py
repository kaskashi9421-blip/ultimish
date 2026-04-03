from django.shortcuts import render, redirect, get_object_or_404
from .models import MainWord, Submission, TableGroup
from .forms import SubmissionForm
from django.conf import settings

USER_PASSWORD = "user123"
ADMIN_PASSWORD = "admin123"

def login_view(request):
    if request.method == "POST":
        password = request.POST.get("password")

        if password == ADMIN_PASSWORD:
            request.session['role'] = 'admin'
            return redirect('home')

        elif password == USER_PASSWORD:
            request.session['role'] = 'user'
            return redirect('home')

    return render(request, "login.html")


def home(request):
    words = MainWord.objects.all()
    role = request.session.get('role')
    return render(request, "home.html", {"words": words, "role": role})


def submit(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.type = 'new'
            sub.save()
            return redirect('home')
    else:
        form = SubmissionForm()

    return render(request, "submit.html", {"form": form})


def admin_panel(request):
    if request.session.get('role') != 'admin':
        return redirect('home')

    submissions = Submission.objects.filter(status='pending')
    return render(request, "admin_panel.html", {"subs": submissions})


def approve(request, id):
    sub = get_object_or_404(Submission, id=id)

    table = TableGroup.objects.first()

    if not table:
        table = TableGroup.objects.create(name="Default Table")

    if sub.type == "new":
        MainWord.objects.create(
            serial_number=MainWord.objects.count() + 1,
            ultimish_word=sub.ultimish_word,
            english_translation=sub.suggested_translation,
            table=table
        )

    sub.status = "approved"
    sub.save()

    return redirect('admin_panel')


def reject(request, id):
    sub = get_object_or_404(Submission, id=id)
    sub.status = "rejected"
    sub.save()
    return redirect('admin_panel')