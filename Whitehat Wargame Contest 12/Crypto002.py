import brainfuck, base64

brainfck = '\053\053\053\053\053\040\053\053\053\133\055\040\076\053\053\053\053\040\053\053\053\053\074\040\135\076\053\053\053\040\053\053\053\053\053\040\053\053\053\056\053\040\053\053\056\074\053\040\053\053\133\055\076\040\053\053\053\074\135\040\076\053\056\074\053\040\053\053\053\133\055\015\012\076\055\055\055\055\040\074\135\076\055\055\040\056\053\053\053\053\040\053\053\053\056\056\040\053\053\053\053\053\040\053\056\074\053\053\040\053\053\053\133\055\040\076\055\055\055\055\040\055\074\135\076\055\040\055\055\055\055\055\040\055\055\056\074\053\040\053\053\053\133\055\015\012\076\053\053\053\053\040\074\135\076\053\053\040\053\053\053\056\053\040\053\053\053\053\053\040\053\056\055\055\055\040\055\055\055\055\055\040\056\056\053\053\053\040\053\053\053\053\056\040\074\053\053\053\133\040\055\076\053\053\053\040\074\135\076\053\053\040\053\056\055\055\055\015\012\055\055\056\055\055\040\055\055\055\055\056\040\055\056\053\053\053\040\053\056\074\053\053\040\053\053\053\133\055\040\076\055\055\055\055\040\055\074\135\076\055\040\055\055\055\055\056\040\074\053\053\053\053\040\053\053\133\055\076\040\053\053\053\053\053\040\053\074\135\076\056\015\012\074\053\053\053\053\040\133\055\076\055\055\040\055\055\074\135\076\040\056\074\053\053\053\040\133\055\076\053\053\040\053\074\135\076\053\040\053\056\074\053\053\040\053\133\055\076\055\040\055\055\074\135\076\040\055\055\055\055\055\040\056\056\074\053\053\040\053\133\055\076\053\015\012\053\053\074\135\076\040\053\053\056\074\053\040\053\053\053\053\133\040\055\076\055\055\055\040\055\055\074\135\076\040\055\056\074\053\053\040\053\053\133\055\076\040\053\053\053\053\074\040\135\076\053\053\053\040\056\055\056\074\053\040\053\053\053\133\055\040\076\055\055\055\055\015\012\074\135\076\055\055\040\055\056\074\053\053\040\053\053\053\133\055\040\076\053\053\053\053\040\053\074\135\076\053\040\053\053\053\056\055\040\055\055\055\055\055\040\055\056\074\053\053\040\053\133\055\076\053\040\053\053\074\135\076\040\053\053\053\056\074\040\053\053\053\133\055\015\012\076\055\055\055\074\040\135\076\055\055\055\040\056\074\053\053\053\040\053\133\055\076\053\040\053\053\053\074\135\040\076\056\074\053\053\040\053\053\053\053\133\040\055\076\055\055\055\040\055\055\055\074\135\040\076\055\056\074\053\040\053\053\053\133\055\040\076\053\053\053\053\015\012\074\135\076\056\074\040\053\053\053\133\055\040\076\053\053\053\074\040\135\076\053\053\053\040\053\053\056\074\053\040\053\053\053\053\133\040\055\076\055\055\055\040\055\055\074\135\076\040\055\055\055\055\056\040\074\053\053\053\053\040\133\055\076\053\053\040\053\053\074\135\076\015\012\053\053\053\053\053\040\056\053\053\053\056\040\055\055\055\055\055\040\056\074\053\053\053\040\053\133\055\076\055\040\055\055\055\074\135\040\076\055\055\055\055\040\055\056\055\055\056\040\074\053\053\053\053\040\053\053\133\055\076\040\053\053\053\053\053\040\053\074\135\076\053\015\012\053\056\055\055\055\040\055\055\056\053\056\040\074\053\053\053\053\040\053\133\055\076\055\040\055\055\055\055\074\040\135\076\055\055\055\040\055\055\055\055\055\040\055\056\074\053\053\040\053\053\133\055\076\040\053\053\053\053\074\040\135\076\053\053\053\040\053\053\053\053\056\015\012\056\074\053\053\053\040\133\055\076\053\053\040\053\074\135\076\053\040\053\053\053\056\074\040\053\053\053\053\053\040\133\055\076\055\055\040\055\055\055\074\135\040\076\055\055\055\055\040\055\055\055\055\055\040\055\056\074\053\053\040\053\053\053\053\133\040\055\076\053\053\053\015\012\053\053\053\074\135\040\076\056\074\053\053\040\053\053\133\055\076\040\055\055\055\055\074\040\135\076\056\074\053\040\053\053\133\055\076\040\053\053\053\074\135\040\076\053\053\053\056\040\074\053\053\053\053\040\133\055\076\055\055\040\055\055\074\135\076\040\056\055\056\053\053\015\012\053\053\053\056\055\040\055\055\055\055\056\040\074\053\053\053\053\040\133\055\076\053\053\040\053\053\074\135\076\040\056\053\053\053\053\040\056\074\053\053\053\040\133\055\076\055\055\040\055\074\135\076\055\040\055\055\055\056\053\040\053\053\053\053\053\040\053\053\056\055\055\015\012\055\055\055\055\055\040\056\074\053\053\053\040\133\055\076\053\053\040\053\074\135\076\053\040\053\053\056\055\055\040\055\055\055\055\055\040\055\055\056\055\055\040\055\056\074\053\053\040\053\133\055\076\053\040\053\053\074\135\076\040\053\053\053\053\053\040\056\074\053\053\053\015\012\053\133\055\076\055\040\055\055\055\074\135\040\076\055\055\055\056\040\074\053\053\053\053\040\133\055\076\055\055\040\055\055\074\135\076\040\055\055\055\056\074\040\053\053\053\053\053\040\133\055\076\053\053\040\053\053\053\074\135\040\076\053\053\056\074\040\053\053\053\053\053\015\012\133\055\076\055\055\040\055\055\055\074\135\040\076\055\055\056\074\040\053\053\053\053\053\040\133\055\076\053\053\040\053\053\053\074\135\040\076\053\053\053\056\040\053\053\056\055\055\040\055\055\055\055\056\040\053\053\056\055\055\040\055\055\056\053\053\040\053\053\053\053\053\015\012\053\053\056\053\053\040\053\053\053\053\053\040\053\056\074\053\053\040\053\053\053\053\133\040\055\076\055\055\055\040\055\055\055\074\135\040\076\055\055\055\056\040\074\053\053\053\053\040\053\133\055\076\053\040\053\053\053\053\074\040\135\076\053\053\053\040\053\053\053\053\053\015\012\053\053\056\055\055\040\055\055\055\055\055\040\056\053\053\053\053\040\056\074\053\053\053\040\053\053\133\055\076\040\055\055\055\055\055\040\074\135\076\055\055\040\055\055\055\055\056\040\074\053\053\053\053\040\133\055\076\053\053\040\053\053\074\135\076\040\053\053\056\074\053\015\012\053\053\053\133\055\040\076\055\055\055\055\040\074\135\076\055\055\040\055\056\053\056\074\040\053\053\053\053\133\040\055\076\053\053\053\040\053\074\135\076\053\040\053\053\053\053\053\040\053\056\074\053\053\040\053\053\133\055\076\040\053\053\053\053\074\040\135\076\056\074\053\015\012\053\053\133\055\076\040\055\055\055\074\135\040\076\055\055\056\053\040\053\053\053\053\053\040\053\056\074\053\053\040\053\133\055\076\055\040\055\055\074\135\076\040\055\055\055\055\055\040\056\055\056\074\053\040\053\053\053\133\055\040\076\055\055\055\055\040\074\135\076\055\055\015\012\055\056\074\053\053\040\053\053\053\133\055\040\076\053\053\053\053\040\053\074\135\076\053\040\053\053\053\053\053\040\056\055\055\055\055\040\055\055\055\056\074\040\053\053\053\133\055\040\076\053\053\053\074\040\135\076\053\053\053\040\056\074\053\053\053\040\133\055\076\055\055\015\012\055\074\135\076\055\040\055\055\055\055\056\040\074\053\053\053\053\040\133\055\076\055\055\040\055\055\074\135\076\040\055\055\055\055\055\040\056\074\053\053\053\040\053\133\055\076\053\040\053\053\053\074\135\040\076\053\053\053\053\040\053\053\056\055\055\040\055\055\055\055\056\015\012\055\055\056\074\053\040\053\053\133\055\076\040\053\053\053\074\135\040\076\053\053\056\074\040\053\053\053\133\055\040\076\055\055\055\074\040\135\076\055\055\056\040\074\053\053\053\133\040\055\076\053\053\053\040\074\135\076\053\053\040\056\055\055\056\074\040\053\053\053\133\055\015\012\076\055\055\055\074\040\135\076\055\055\056\040\074\053\053\053\053\040\133\055\076\053\053\040\053\053\074\135\076\040\053\053\053\053\053\040\053\053\053\056\074\040\053\053\053\053\133\040\055\076\055\055\055\040\055\074\135\076\055\040\055\055\055\055\056\040\074\053\053\053\053\015\012\133\055\076\055\055\040\055\055\074\135\076\040\055\055\056\074\053\040\053\053\133\055\076\040\053\053\053\074\135\040\076\053\053\056\056\040\056\074'.decode('utf-8')
b32 = brainfuck.to_function(brainfck)()
b64 = base64.b32decode(b32)
print base64.b64decode(b64).decode('rot13')