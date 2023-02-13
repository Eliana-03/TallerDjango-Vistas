from .logic import measurements_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):

    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = vl.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')

        else:
            measurements = vl.get_measurements()
            measurements_dto = serializers.serialize('json', measurements)
            return HttpResponse(measurements_dto, 'application/json')
    
    if request.method == 'POST':
        details = json.loads(request.body)
        measurement_dto = vl.create_measurement(details)
        measurement = serializers.serialize('json', [measurement_dto])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'PUT':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = vl.update_measurement(id, json.loads(request.body))
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            return HttpResponse("Error: Measurement ID required (xd)", 'application/text')
    
    if request.method == 'DELETE':
        id = request.GET.get("id", None)
        if id:
            vl.delete_measurement(id)
            return HttpResponse("Measurement Deleted", 'application/text')
        else:
            return HttpResponse("Error: Measurement ID required (xd)", 'application/text')



@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'PUT':
        measurement_dto = vl.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    
    if request.method == 'GET':
        measurement_dto = vl.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    
    if request.method == 'DELETE':
        vl.delete_measurement(pk)
        return HttpResponse("Measurement Deleted", 'application/text')
