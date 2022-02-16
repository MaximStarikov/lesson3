# Изучаем отступы (1. Сначала идет условие после чего в условие вкладываются данные посредством отступа (TAB).
# 2. Новое условие или команда на выполнение уже пишется с новой строки.

x = 0
while x < 10:
    print(x)
    x = x + 1

# Изучаем функции


def discounted(price, discount):
    price = abs(price)
    discount = abs(discount)
    if discount > 100:
        price_with_discount = price - (price * discount / 100)
    else:
        return price_with_discount


price_discounted = discounted(100, 50)
print(price_discounted)

