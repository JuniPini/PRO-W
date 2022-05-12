cadena = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

Usuarios = {}

#for linea in cadena.split("\n") [1:]:
    #dato = linea.split(";")

    #Usuarios.setdefault(dato[0],{'nombre' : dato[1], 'email' : dato[2], 'teléfono' : dato[3],'descuento' : dato[4]})

for linea in cadena.split("\n")[1:]:
    dato = linea.split(";")
    
    nif = dato[0]

    nombre = dato[1]

    email = dato[2]
    
    teléfono = dato[3]

    descuento = dato[4]

    usuario = {}

    usuario.setdefault("nombre", nombre)
    usuario.setdefault("email", email)
    usuario.setdefault("teléfono", teléfono)
    usuario.setdefault("descuento", descuento)

    Usuarios.setdefault(nif, usuario)

print(Usuarios)
    
    #Usuarios.setdefault(nif, {"nombre":dato[1]; "email":dato[2]; })