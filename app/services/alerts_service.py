from ..models.alerts import Alerts
from ..models.patients import Patients
from ..models.names import Names
from .. import db
from sqlalchemy.orm import joinedload

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

def fetch_active_alerts_by_caregiver(caregiver_id: int) -> list[dict]:
    """
    Trae todas las alertas activas de un cuidador (state=1),
    cargando paciente y su nombre en un único JOIN.
    """
    alerts = (
        Alerts.query
              .options(
                  # 1) Carga el paciente (Alerts.patient)
                  joinedload(Alerts.patient)
                  # 2) Y dentro de ese paciente, carga Names (Patients.names)
                  .joinedload(Patients.names)
              )
              .filter_by(caregiver_id=caregiver_id, state=1)
              .all()
    )

    resultado = []
    for a in alerts:
        p = a.patient   # usa la relación .patient
        n = p.names     # usa la relación .names
        resultado.append({
            'alert_id':    a.alert_id,
            'alert_type':  a.alert_type,
            'description': a.description,
            'state':       a.state,
            'created_at':  a.created_at.isoformat(),
            'updated_at':  a.updated_at.isoformat() if a.updated_at else None,
            'patient': {
                'patient_id':       p.patient_id,
                'cuarto':           p.cuarto,
                'fecha_nacimiento': p.fecha_nacimiento.isoformat(),
                'sexo':             p.sexo,
                'is_active':        p.is_active,
                'name': {
                    'name_id':          n.name_id,
                    'first_name':       n.first_name,
                    'middle_name':      n.middle_name,
                    'last_name':        n.last_name,
                    'second_last_name': n.second_last_name,
                }
            }
        })

    return resultado