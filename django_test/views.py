from django.shortcuts import render
from django.core.serializers import serialize
from django_test.models import Student
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')  # Render the index.html template

def add_students(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        image = request.FILES.get('image')

        # Create a new student
        student = Student(name=name, surname=surname, image=image)
        student.save()

        return JsonResponse({
            'name': student.name,
            'surname': student.surname,
            'image': student.image.url if student.image else None
        })

    if request.method == 'GET':
        students = Student.objects.all()
        students_data = [
            {'name': student.name, 'surname': student.surname, 'image': student.image.url if student.image else None}
            for student in students
        ]
        return JsonResponse({'students': students_data}, safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

