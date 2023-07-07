

def convert(a):
    b = a.replace(" ",'')
    c = b.replace("INR",'')
    d = c.replace(",",'')
    f = d.replace("₹",'')
    g = int(float(f))
    return g


