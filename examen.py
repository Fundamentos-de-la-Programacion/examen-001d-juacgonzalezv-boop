def mostra_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")
def opciones_():
    while True:
        opcion = int(input("ingrese una opcion: "))
        try:
            if opcion < 1 and opcion > 6:
                return opcion
            else:
                print("error de seleccion")
                mostra_menu
        except ValueError:
            print( "error de elecion")
            mostra_menu
def leer_enteros(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("error ingrese un nuemro entero")

def buscar_codigo(codigo,planes):
    codigo = codigo.strip().lower()
    for clave in planes:
        if clave.strip().lower() == codigo:
            return True
    return False
def clave(codigo,planes):
    codigo = codigo.strip().lower()
    for clave in planes:
        if clave.strip().lower() == codigo:
            return True
    return None
def tipo_cupos(tipos,planes,inscripciones,):
    total = 0
    tipos =tipos.strip().lower()
    for codigo ,datos in planes.items():
        if datos[1].strip().lower() == tipos:
            total = inscripciones[codigo][1]
            return total 
def opcion_cupos(planes,inscripciones):
    tipos= input("ingrese el tipo de plane")
    total = tipo_cupos(tipos,planes,inscripciones)  
    print("cupos diponibles es {total}")   
def busacr_rango(precio_min, precio_max,planes,inscripciones):
    resultado = []
    for codigo , datos in planes.items():
        precio =inscripciones[codigo][0]
        if precio_min <= precio <= precio_max:
            nombre = datos[0]
            resultado.append(f"{nombre}, {codigo}")
        return resultado 
    
def opcion_busqueda(planes,inscripciones):
    precio_min= leer_enteros("ingrese el presio minimo: ")
    precio_max = leer_enteros("ingrese el presio maximo: ")
    encontrados =  busacr_rango(precio_min, precio_max,planes,inscripciones)

def actualizar_planes(nuevo_plan,codigo,planes,inscripciones ):
    if not buscar_codigo(codigo,planes):
        return False
    clave_real = clave(codigo,planes)
    inscripciones[clave_real][0]= nuevo_plan
    return True

def opcion_actualizat(planes,inscripciones):
    while True:
        codigo = int(input("ingerese el nuevo plan: "))
        nuevo_plan = leer_enteros("ingrese nuevo plan: ")
        actualizar = actualizar_planes(nuevo_plan,codigo,planes,inscripciones)
        if actualizar:
            print("plan actualizado")
        else:
            print("el plan no se pudo actualizar")




def eliminar_plan(codigo, planes, inscripciones):
    if not buscar_codigo(codigo,planes):
        return False
    clave_real = obtener_clave(codigo,planes)
    del planes[clave_real]
    del inscripciones[clave_real]
    return True
def opcion_eleiminar(planes, inscripciones):
    codigo = input("ingrese el codigo del plan")
    if eliminar_plan(codigo, planes, inscripciones):
        print("elimado el plan")
    else:
        print("el codigo no existe")
    
def main():
        planes = {
            'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
            'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
            'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
            'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
            'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
            'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
        }    
        inscripciones = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15],
        } 
        mostra_menu()
        opciones_()
        if opciones_ ==1:
            opcion_cupos(planes, inscripciones)
        elif opciones_==2:
            opcion_busqueda(planes, inscripciones)
        elif opciones_==3:
            opcion_actualizat(planes, inscripciones)
        elif opciones_ == 4:
        elif opciones_== 5:
            opcion_eleiminar(planes,inscripciones)
        elif opciones_== 6:
            print("fin del programa")
            break   

main()