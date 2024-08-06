from app.utils.fee_calculator import calculate_demurrage_and_detention_fees

def test_fee_calculation():
    demurrage_fee, detention_fee = calculate_demurrage_and_detention_fees(12, 5)
    assert demurrage_fee == 410
    assert detention_fee == 140

def test_fee_calculation_no_fees():
    demurrage_fee, detention_fee = calculate_demurrage_and_detention_fees(5, 3)
    assert demurrage_fee == 0
    assert detention_fee == 0

def test_fee_calculation_partial_fees():
    demurrage_fee, detention_fee = calculate_demurrage_and_detention_fees(8, 9)
    assert demurrage_fee == 150
    assert detention_fee == 420
