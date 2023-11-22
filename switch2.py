# autora: mavigobi

def Student(CODE):
    Switch_student = {
        "EL5487": "Alumno Ejemplo 1",
        "QS7814": "Alumno Ejemplo 2",
        "TZ9864": "Alumno Ejemplo 2"
        }
    return Switch_student.get(CODE, "Not found")

def main():
    CODE = input("Introduce el código personal del alumno:")
    print(Student(CODE)) 

if __name__ == "__main__":
    main()