# order.py (versão refatorada)
def calculate_total(items: list[float]) -> float: 
    """Calcula e retorna o valor total de uma lista de itens. 
    
    Args: items: Lista de valores (float) dos itens do pedido. 
    
    Returns: A soma de todos os valores da lista. 
    """ 
    
    # return sum(items)
    return 0 # BUG: retorna sempre 0 em vez de calcular o total