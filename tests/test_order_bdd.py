# tests/test_order_bdd.py
from pytest_bdd import scenarios, given, when, then
from order import calculate_total
 
scenarios("features/order_total.feature")
 
 
@given("que o pedido possui os itens 10, 20 e 30", target_fixture="order_items")
def order_items():
    return [10, 20, 30]
 
 
@when("o sistema calcula o valor total", target_fixture="total")
def calculate(order_items):
    return calculate_total(order_items)
 
 
@then("o resultado deve ser 60")
def check_total(total):
    assert total == 60
