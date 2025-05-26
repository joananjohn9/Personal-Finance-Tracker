from dataclasses import dataclass


@dataclass
class Investment:
    Name :str
    Type : str
    Current : float
    PL : float
    ROI : float

@dataclass
class Transaction:
    Transaction_id : str
    Date: str
    Amount : float
    Category : str
    Type :str