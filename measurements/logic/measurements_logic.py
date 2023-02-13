from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def create_measurement(details):
    variable_id = details["variable"]
    measurement = Measurement(
        variable= Variable.objects.get(pk=variable_id),
        value=details["value"],
        unit=details["unit"],
        place=details["place"]
    )
    measurement.save()
    return measurement

def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)

    variable_id = new_measurement["variable"]
    variable = Variable.objects.get(pk=variable_id)

    measurement.variable = variable
    measurement.value = new_measurement["value"]
    measurement.unit = new_measurement["unit"]
    measurement.place = new_measurement["place"]
    measurement.save()
    return measurement

def delete_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    measurement.delete()