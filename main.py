import mysql.connector

bd = mysql.connector.connect(user='edgar', password='12345678', database='nopalito')

cursor = bd.cursor()

while True:
    print("1) Agregar usuario")
    print("2) Mostrar usuarios")
    print("0) Salir")

    opc = input("Opcion: ")

    if opc == '1':
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        contra = input("Contraseña: ")

        consulta = "INSERT INTO usuario(nombre, apellidos, contraseña) " \
                    "VALUES (%s,%s,%s)"
        cursor.execute(consulta, (nombre,apellidos,contra))
        bd.commit()

        if cursor.rowcount:
            print("Se agrego usuario")
        else:
            print("No se agrego usuario")

    elif opc == '2':
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("Id: ",row[0])
            print("Nombre: ",row[1])
            print("Apellidos: ",row[2])
            print("Contraseña: ",row[3])

    elif opc == '0':
        break
    else:
        print("Opcion incorrecta")
