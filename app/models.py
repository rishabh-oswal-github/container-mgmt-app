from datetime import date

class Container:
    def __init__(self, container_id: str, arrival_date: date, departure_date: date):
        self._container_id = container_id
        self._arrival_date = arrival_date
        self._departure_date = departure_date
        self._status = "active"

    # Getter for container_id
    @property
    def container_id(self) -> str:
        return self._container_id

    # Setter for container_id
    @container_id.setter
    def container_id(self, value: str):
        if not value:
            raise ValueError("Container ID cannot be empty.")
        self._container_id = value

    # Getter for arrival_date
    @property
    def arrival_date(self) -> date:
        return self._arrival_date

    # Setter for arrival_date
    @arrival_date.setter
    def arrival_date(self, value: date):
        if not isinstance(value, date):
            raise TypeError("Arrival date must be a date object.")
        self._arrival_date = value

    # Getter for departure_date
    @property
    def departure_date(self) -> date:
        return self._departure_date

    # Setter for departure_date
    @departure_date.setter
    def departure_date(self, value: date):
        if not isinstance(value, date):
            raise TypeError("Departure date must be a date object.")
        self._departure_date = value

    # Getter for status
    @property
    def status(self) -> str:
        return self._status

    # Setter for status
    @status.setter
    def status(self, value: str):
        if value not in ["active", "inactive"]:
            raise ValueError("Status must be either 'active' or 'inactive'.")
        self._status = value

class FeeRecord:
    def __init__(self, container_id: str, days_on_terminal: int, days_with_consignee: int,\
                demurrage_fee: float, detention_fee: float):
        self._container_id = container_id
        self._days_on_terminal = days_on_terminal
        self._days_with_consignee = days_with_consignee
        self._demurrage_fee = demurrage_fee
        self._detention_fee = detention_fee
        self._total_fee = demurrage_fee + detention_fee

    # Getter for container_id
    @property
    def container_id(self) -> str:
        return self._container_id

    # Setter for container_id
    @container_id.setter
    def container_id(self, value: str):
        if not value:
            raise ValueError("Container ID cannot be empty.")
        self._container_id = value

    # Getter for days_on_terminal
    @property
    def days_on_terminal(self) -> int:
        return self._days_on_terminal

    # Setter for demurrage_fee
    @days_on_terminal.setter
    def days_on_terminal(self, value: float):
        if value < 0:
            raise ValueError("Days on Terminal cannot be negative.")
        self._days_on_terminal = value

    @property
    def days_with_consignee(self) -> int:
        return self._days_with_consignee

    # Setter for days with consignee
    @days_with_consignee.setter
    def days_with_consignee(self, value: float):
        if value < 0:
            raise ValueError("Days with Consignee cannot be negative.")
        self._days_with_consignee = value

    # Getter for demurrage fee (read-only)
    @property
    def demurrage_fee(self) -> float:
        return self._demurrage_fee
    
    # Getter for detention fee (read-only)
    @property
    def detention_fee(self) -> float:
        return self._detention_fee

    # Getter for total_fee (read-only)
    @property
    def total_fee(self) -> float:
        return self._total_fee
