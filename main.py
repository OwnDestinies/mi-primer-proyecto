import time

# ---- PLANTA ----
temp = 70.0
ambiente = 22.0

k_perdidas = 0.02
potencia_max = 20.0

# ---- CONTROL PI ----
setpoint = 75.0
Kp = 0.06
Ki = 0.02

integral = 0.0
dt = 0.5

while True:
    error = setpoint - temp

    # Integrador
    integral += error * dt

    # PI
    u = Kp * error + Ki * integral

    # Limitar a 0..1
    salida = max(0.0, min(1.0, u))

    # Anti-windup (simple): si saturado, no acumules más en esa dirección
    if (salida == 1.0 and error > 0) or (salida == 0.0 and error < 0):
        integral -= error * dt

    # ---- PLANTA ----
    temp += (ambiente - temp) * k_perdidas
    temp += potencia_max * salida

    print(f"Temp: {temp:6.2f} °C | Salida: {salida*100:5.1f}% | Error: {error:7.2f}")

    time.sleep(dt)