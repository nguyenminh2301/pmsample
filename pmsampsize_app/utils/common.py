
def parse_input(input_str, type_func=float):
    """Parses string input into a list of values."""
    if not isinstance(input_str, str):
        return [type_func(input_str)]
    
    input_str = input_str.strip()
    vals = set()
    
    parts = input_str.split(',')
    for part in parts:
        if '-' in part:
            try:
                start, end = map(float, part.split('-'))
                if type_func == int:
                    vals.update(range(int(start), int(end) + 1))
                else:
                    step = 0.01 if (end - start) < 0.2 else 0.05
                    curr = start
                    while curr <= end + 1e-9:
                        vals.add(round(curr, 4))
                        curr += step
            except:
                pass 
        else:
            try:
                vals.add(type_func(part))
            except:
                pass
                
    return sorted(list(vals))
