import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}

    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalucateTotalImpurePrice(products):
    total_impure_price = 0
    for k, v in products.items():
        total_impure_price += float(v['unit_price']) * int(v['qnt'])
    total_impure_price = round(total_impure_price, 2)
    return total_impure_price

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

