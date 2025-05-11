from ..models.alerts import Alerts
from .. import db

# Mapa de tipo-de-alerta según el botón

BUTTON_ALERT_MAP = {
    0: "CALL_NURSE",
    1: "EMERGENCY",
    2: "MEDICATION",
    3: "ASSISTANCE",
    4: "PAIN",
    5: "MEAL",
    6: "WATER",
}
def get_all_alerts():
    return Alerts.query.all()

def create_alert(data):
    new_alert = Alerts(
        alert_type=data['alert_type'],
        description=data['description'],
        patients_patient_id=data['patients_patient_id']
    )
    db.session.add(new_alert)
    db.session.commit()
    return new_alert

def create_alert_by_button(button_id: int, state: int, panel) -> Alerts:
    alert_type = BUTTON_ALERT_MAP.get(button_id, "UNKNOWN")
    description = f"Button {button_id} pressed"

    alert = Alerts(
        alert_type   = alert_type,
        description  = description,
        state        = state,
        device_id    = panel.device_id,
        patient_id   = panel.patient_id,
        caregiver_id = panel.caregiver_id,
    )
    db.session.add(alert)
    db.session.commit()
    return alert
