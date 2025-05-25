from .names_service import get_all_names, create_name
from .patients_service import get_all_patients, create_patient, get_all_patients_by_caregiver
from .turns_service import get_all_turns, create_turn
from .alerts_service import get_all_alerts, create_alert_by_button, fetch_active_alerts_by_caregiver
from .recipes_service import get_all_recipes, create_recipe
from .drugs_service import get_all_drugs, create_drug
from .medication_schedules_service import get_all_medication_schedules, create_medication_schedule
from .caregivers_service import (
    get_all_caregivers,
    get_caregiver_profile,
    CaregiverAuthService
)
from .panels_service import (
    PanelsService
)

# Exportar todos los servicios
__all__ = [
    'get_all_names', 'create_name',
    'get_all_patients', 'create_patient',
    'get_all_turns', 'create_turn',
    'get_all_caregivers', 'get_all_patients_by_caregiver', 'create_caregiver', 'get_caregiver_profile',
    'get_all_alerts', 'create_alert_by_button', 'fetch_active_alerts_by_caregiver',
    'get_all_recipes', 'create_recipe',
    'get_all_drugs', 'create_drug',
    'get_all_medication_schedules', 'create_medication_schedule',
    'count_active_panels_for_caregiver',
]

register_caregiver = CaregiverAuthService.register_caregiver
authenticate = CaregiverAuthService.authenticate
generate_token = CaregiverAuthService.generate_token
get_caregiver_by_id = CaregiverAuthService.get_caregiver_by_id

count_active_panels_for_caregiver = PanelsService.count_active_panels_for_caregiver
