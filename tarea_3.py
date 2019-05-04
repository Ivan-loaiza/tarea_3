from functools import cmp_to_key

agenda_hospital = []

persona = ('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')

agenda_hospital.append(persona)

persona = ('Ana', 'Jiminez', 32415116, 50, 46261266, 'consulta')

agenda_hospital.append(persona)

persona = [('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta'),
           ('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor'),
           ('Felipe', 'Perez', 12243151, 42, 65151111, 'documento'),
           ('Melissa', 'Alvaro', 734114144, 10, 87421612, 'dolor'),
           ('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')]

agenda_hospital.extend(persona)

print("El total de Pacientes es: {0}".format(len(agenda_hospital)))

cantidad_pacientes_dolor = 0
for paciente in agenda_hospital:
    if paciente[5] == 'dolor':
        cantidad_pacientes_dolor += 1

print("EL total de Pacientes con dolor es: {0}".format(cantidad_pacientes_dolor))

def cmp_tuplas(a, b):
    if a[3] >= b[3]:
        return -1
    else:
        return 1


clave_ordenacion = cmp_to_key(cmp_tuplas)

agenda_hospital = sorted(agenda_hospital, key=clave_ordenacion)

for paciente in agenda_hospital:
    print(paciente)

personas_menores = 0
personas_mayores = 0

for persona in agenda_hospital:
    if persona[3] >= 18:
        personas_mayores += 1
    else:
        persona[3] <= 18
        personas_menores += 1

print('las personas mayores son: ', personas_mayores)
print('las personas menores son: ', personas_menores)

