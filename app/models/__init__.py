from .names import Names
from .patients import Patients
from .turns import Turns
from .caregivers import Caregivers
from .alerts import Alerts
from .recipes import Recipes
from .drugs import Drugs
from .medication_schedules import MedicationSchedules
from .panels import Panels

# Exportar todos los modelos
__all__ = [
    'Names',
    'Patients',
    'Turns',
    'Caregivers',
    'Alerts',
    'Recipes',
    'Drugs',
    'MedicationSchedules',
    'Panels'
]