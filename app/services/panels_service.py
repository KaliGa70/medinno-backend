from datetime import datetime, timedelta
from ..models.panels import Panels
from ..models.caregivers import Caregivers
from sqlalchemy.orm import Session

class PanelsService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def count_active_panels_for_caregiver(self, caregiver_id: int) -> int:
        count = (
            self.db.query(Panels)
            .join(Panels.caregivers)
            .filter(Caregivers.caregiver_id == caregiver_id)
            .count()
        )
        return count
