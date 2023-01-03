from core.models import Subject

def get_subjects(request):
    subjects = Subject.objects.all()
    return {
        'subjects':subjects
    }