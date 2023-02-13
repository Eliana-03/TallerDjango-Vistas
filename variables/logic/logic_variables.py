from ..models import Variable

def get_variables():
    variables = Variable.objects.all()
    return variables