def feat(a, b):
    return a + b

def open_long(size, price):
    amount_notional = size * price
    return f"Opening long position of size {size} at price {price} | total notional: {amount_notional}"