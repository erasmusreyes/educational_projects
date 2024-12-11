from dataclasses import dataclass

@dataclass
class Transaction:
    transaction_id: int
    date: str
    type_: str
    description: str
    amount: float

def make_transaction(row):
    return Transaction(row[0], row[1], row[2], row[3], row[4])

