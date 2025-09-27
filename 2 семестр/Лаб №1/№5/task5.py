import math

def safe_apply(func, data):
    results = []
    errors = []
    for el in data:
        try:
            results.append(func(el))
        except Exception as e:
            errors.append((el, e.__class__.__name__))
    return results, errors

data = ['4', '16', 'text', '-25', '9.0']
f = lambda x: math.sqrt(float(x))
results, errors = safe_apply(f, data)
print('results:', results)
print('errors:', errors)