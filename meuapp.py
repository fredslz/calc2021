
def soma(num1, num2):
    
    if is_number(num1) and is_number(num2):
        return float(a) + float(b)
    else:
        return None
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
