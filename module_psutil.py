# autora: mavigobi

import psutil

if __name__ == '__main__':
    cpu_info = psutil.cpu_percent(interval=1, percpu=True)
    size_busy = float(psutil.virtual_memory().used * 1024 / psutil.virtual_memory().total)
    s_busy = round(size_busy,3)
    size_free = int(psutil.virtual_memory().free*100 / psutil.virtual_memory().total)
    print(f'Estado actual de la memoria de la CPU: {cpu_info}')
    print(f'Porcentaje de memoria de la CPU ocupada: {s_busy}')
    print(f'Porcentaje de memoria de la CPU libre: {size_free}')