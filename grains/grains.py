def validate(num):
    if num < 1 or num > 64:
        raise ValueError("Invalid range")

def on_square(num):
    validate(num)
    return 2**(num-1)

def total_after(num):
    validate(num)
    return (1<<num)-1
