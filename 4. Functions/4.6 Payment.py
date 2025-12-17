def compute_pay(h, r):
    """
    Calculate the pay for an employee based on hours worked and hourly rate.
    Employees are paid regular rate for hours up to 40 per week.
    Hours worked beyond 40 are paid at 1.5 times the regular rate (overtime).
    Args:
        h (float): Hours worked in a week.
        r (float): Hourly rate in dollars.
    Returns:
        float: Total pay amount in dollars.
    Example:
        >>> compute_pay(45, 10)
        475.0
        >>> compute_pay(35, 10)
        350.0
    """
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + (h - 40) * 1.5 * r
    return pay

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

p = compute_pay(hrs, rate)
print("Pay", p)