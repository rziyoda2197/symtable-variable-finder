import symtable

def top_o_zgaruvchilar(kod):
    table = symtable.symtable(kod, "<string>", "exec")
    o_zgaruvchilar = []
    
    for sym in table.get_symbols():
        if sym.get_name() and sym.get_name().isidentifier():
            o_zgaruvchilar.append(sym.get_name())
    
    return o_zgaruvchilar

kod = """
x = 5
y = 10
z = x + y
"""

print(top_o_zgaruvchilar(kod))
```

Kodni o'zgartirib, quyidagicha yozing:

```python
import symtable

def top_o_zgaruvchilar(kod):
    table = symtable.symtable(kod, "<string>", "exec")
    o_zgaruvchilar = []
    
    for sym in table.get_symbols():
        if sym.get_name() and sym.get_name().isidentifier():
            o_zgaruvchilar.append(sym.get_name())
    
    return o_zgaruvchilar

kod = """
x = 5
y = 10
z = x + y
"""

print(top_o_zgaruvchilar(kod))
