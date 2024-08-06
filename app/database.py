from typing import Dict
from app.models import Container, FeeRecord

# In-memory databases
containers_db: Dict[str, Container] = {}
fees_db: Dict[str, FeeRecord] = {}
