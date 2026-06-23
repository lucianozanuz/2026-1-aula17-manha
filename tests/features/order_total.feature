# tests/features/order_total.feature
Feature: Calculo do total do pedido
    Como cliente do LocalEats, 
    desejo que o sistema calcule o total do meu pedido, 
    para que eu saiba o valor final da compra. 

Scenario: Somar os valores dos itens
Given que o pedido possui os itens 10, 20 e 30
When o sistema calcula o valor total 
Then o resultado deve ser 60