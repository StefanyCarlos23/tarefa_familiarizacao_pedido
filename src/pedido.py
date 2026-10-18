def calcular_total_pedido(subtotal, distancia_km, cliente_vip=False):
    """Calcula o valor final de um pedido.

    A implementação inicial contém defeitos e deve ser corrigida
    de acordo com os requisitos descritos no README.
    """

    if subtotal < 0:
        raise ValueError("Subtotal não pode ser negativo")
    if distancia_km < 0:
        raise ValueError("Distância não pode ser negativa")

    subtotal_com_desconto = subtotal * 0.9 if cliente_vip else subtotal

    if subtotal_com_desconto >= 100:
        frete = 0
    else:
        frete = 8 + 1.5 * distancia_km

    total = subtotal_com_desconto + frete
    return total
