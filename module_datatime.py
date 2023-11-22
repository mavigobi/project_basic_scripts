# autora: mavigobi

from datetime import datetime as dtime
import pytz

def main():
    zonas = ['Asia/Tokyo', 'Europe/Madrid', 'America/Argentina/Buenos_Aires', 'US/eastern', 'US/Pacific', 'UTC']
    ciudades = ['Tokyo', 'Madrid', 'Buenos Aires', 'New York', 'California', 'UTC']
    for (zonas, ciudades) in zip(zonas,ciudades):
        hora_actual = dtime.now(pytz.timezone(zonas))
        print(f'Fecha en {ciudades} - {hora_actual}')

if __name__ == '__main__':
    main()