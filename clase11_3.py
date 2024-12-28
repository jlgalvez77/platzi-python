is_member = True
age = 15

if is_member:
    if age >= 15:
        print('Tienes acceso ya que eres miembro y tienes 15 años o más')
    else:
        print('No tienes acceso ya que eres miembro pero tienes menos de 15 años')
else:
    print('No tienes acceso ya que no eres miembro')