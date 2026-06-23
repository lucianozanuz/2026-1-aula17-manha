"""Calculo do total do pedido feature tests."""

from order import calculate_total

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/order_total.feature', 'Somar os valores dos itens')
def test_somar_os_valores_dos_itens():
    """Somar os valores dos itens."""


@given('que o pedido possui os itens 10, 20 e 30', target_fixture="order_items")
def order_items():
    return [10, 20, 30]


@when('o sistema calcula o valor total', target_fixture="total")
def calculate(order_items):
    return calculate_total(order_items)


@then('o resultado deve ser 60')
def check_total(total):
    assert total == 60