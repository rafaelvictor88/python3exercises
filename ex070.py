total_shop = more_than_K = cheapless_item = count = 0
name_of_cheapless_item = ' '

while True:
    item = str(input('Nome do Produto: '))
    price = float(input('Preço: R$ '))
    count += 1
    total_shop += price
    if price > 1000:
        more_than_K += 1
    if count == 1:
        cheapless_item = price
        name_of_cheapless_item = item
    else:
        if price < cheapless_item:
            cheapless_item = price
            name_of_cheapless_item = item

    answer = ' '
    while answer not in 'SN':
        answer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if answer == 'N':
        break

print(f'O valor total gasto na compra foi R${total_shop:.2f}.')
print(f'Você comprou {more_than_K} produtos mais caros que R$1000.00.')
print(f'O produto mais barato foi {name_of_cheapless_item} que custou R${cheapless_item:.2f}.')
# totalShop = moreThenK = moreShipItem = count = 0
# nameMoreShipItem = ' '
#
# while True:
#     item = str(input('Nome do produto: '))
#     price = float(input('Preço: R$ '))
#     count += 1
#     totalShop += price
#
#     if price > 1000:
#         moreThenK += 1
#
#     if count == 1 or price < moreShipItem:
#         moreShipItem = price
#         nameMoreShipItem = item
#     # else:
#     #     if price < moreShipItem:
#     #         moreShipItem = price
#     #         nameMoreShipItem = item
#
#     stop = ' '
#     while stop not in 'SN':
#         stop = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if stop == 'N':
#         break
#
# print(f'O total gasto na compra foi: R${totalShop:.2f}.')
# print(f'O total de produtos mais caros que R$1000.00: {moreThenK}.')
# print(f'O produto mais barato foi {nameMoreShipItem} que custa {moreShipItem:.2f}.')