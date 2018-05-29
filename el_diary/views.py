from django.shortcuts import render
from college.models import Post, Teacher
from el_diary.forms import AddTeacherForm


# TODO: Написать авторизацию
def index(request):
    post = Post.objects.order_by('date')[:5]
    context = {
        'posts': post
    }
    return render(request, 'index.html', context)


def teachers(request):
    context = {
        'teachers': Teacher.objects.order_by('name')
    }
    return render(request, 'teachers.html', context)


def add_teacher(request):
    form = AddTeacherForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            tchr = form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            print('Created teacher:', tchr)
            return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'forms/add_teacher.html', {'form': form})
